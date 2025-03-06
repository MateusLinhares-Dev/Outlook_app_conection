from fastapi import APIRouter, Request, HTTPException, BackgroundTasks
import json
import logging
from fastapi.responses import Response, JSONResponse
from app_pescanova.get_folder_messages import get_attachments, get_complaint, get_messages, get_token_outlook
import os
from .subscription_expiration import consultant_expiration_subscription, reactivate_subscription
from app_pescanova.list_message_by_id import list_message_by_id
from app_pescanova.api.xml_newWorkflowEditData import new_workflow_edit_data, workflow_edit_data_xml, workflow_execute_activity_xml
from app_pescanova.api.instance_newWorkflow import instance_workflow_edit_data
from app_pescanova.api.instance_execute_activity_wf import instance_workflow_activity
from app_pescanova.api.instance_edit_workflow import workflow_edit_data
from app_pescanova.xml_soap.generate_xml_newAttachment import generate_xml_strings
from app_pescanova.api.newAttachment import new_attachment
from app_pescanova.xml_soap.clean_folders import clean_folders
from app_pescanova.api.idp_extract import extract_idp_text
from pydantic import BaseModel
from typing import List, Optional
import re

# Configuração do logger
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    handlers=[logging.StreamHandler()])
logger = logging.getLogger()

# Definição do roteador da API
webhook_router = APIRouter()

BASE_FILE = os.path.abspath(os.path.dirname(__file__))
ACCESS_TOKEN = get_token_outlook()
os.environ['TOKEN_OUTLOOK'] = ACCESS_TOKEN

processed_ids = set()

# Model para validação dos dados da requisição
class ResourceData(BaseModel):
    id: str
    odata_type: Optional[str] = None
    odata_id: Optional[str] = None
    odata_etag: Optional[str] = None

# Ajustando o modelo Notification
class Notification(BaseModel):
    subscriptionId: str
    subscriptionExpirationDateTime: str
    changeType: str
    resource: str
    resourceData: ResourceData
    clientState: Optional[str] = None
    tenantId: str

# WebhookRequest ajustado para conter uma lista de Notification
class WebhookRequest(BaseModel):
    value: List[Notification]

# Função de processamento assíncrono das notificações
async def process_notification(message_id: str):
    try:
        email = get_messages(message_id)
        complaint_email = get_complaint(email)
        get_attachments(complaint_email)

        # Workflow -> Processamento para instanciar wf com os primeiros dados
        message_info_json = list_message_by_id(message_id)
        # gerar o xml da api
        xml = new_workflow_edit_data(
            message_info_json.get('subject', None),
            message_info_json.get('name_sender', None),
            message_info_json.get('sender', None)
        )
        
        record_key = instance_workflow_edit_data(xml)
        logging.info(f"ID do workflow {record_key}")
        
        # Processo os arquivos
        xml_attachments = generate_xml_strings(record_key)
        for xml_index in xml_attachments:
            response_attachments = new_attachment(xml_index)
            logger.info(f"Anexo processado: {response_attachments}")

            file_name = re.search(r'<urn:FileName>(.*?)</urn:FileName>', xml_index)
            if file_name.group(1).endswith('.pdf'):
                response = extract_idp_text(xml_index)
                xml_workflow_edit_data_pdf = workflow_edit_data_xml(record_key, **response['structured_data'])
                response = workflow_edit_data(xml_workflow_edit_data_pdf)
                
        xml_workflow_activity = workflow_execute_activity_xml(record_key)
        response = instance_workflow_activity(xml_workflow_activity)
        print("Instanciando workflow:", response)
        
        logger.info(f"Tarefa para o message_id {message_id} concluída com sucesso.")
        clean_folders()

    except Exception as e:
        logger.error(f"Erro ao processar notificação {message_id}: {str(e)}")

# Rota do webhook
@webhook_router.post("/outlook-webhook")
async def outlook_webhook(request: Request, background_tasks: BackgroundTasks):

    validation_token = request.query_params.get("validationToken")
    if validation_token:
        return Response(content=validation_token, media_type="text/plain")
    
    try:
        # Verifica expiração de assinatura
        if consultant_expiration_subscription():
            with open(os.path.join(BASE_FILE, 'id_subscription.json')) as subscription_file:
                data = json.load(subscription_file)
                reactivate_subscription(data.get('id', None))

        body = await request.json()

        # Log do corpo para verificar como os dados estão chegando
        logger.info("Body recebido: %s", json.dumps(body, indent=2))

        try:
            validated_body = WebhookRequest(**body)
        except Exception as validation_error:
            logger.error(f"Erro na validação do corpo: {str(validation_error)}")
            raise HTTPException(status_code=400, detail=f"Erro na validação do corpo: {str(validation_error)}")
        
        logger.info("Notificação recebida: %s", json.dumps(body, indent=2))

        for notification in validated_body.value:
            if notification.changeType == "created":
                message_id = notification.resourceData.id
                
                if message_id:
                    if message_id in processed_ids:
                        logger.info(f"Notificação {message_id} já foi processada. Ignorando.")
                        continue
                    
                    processed_ids.add(message_id)
                    try:
                        background_tasks.add_task(process_notification, message_id)
                        logger.info(f"Tarefa iniciada para o message_id {message_id}")
                    except Exception as task_error:
                        logger.error(f"Erro ao adicionar tarefa para {message_id}: {task_error}")
        return JSONResponse(status_code=202, content={"message": "Accepted"})
    
    except Exception as e:
        logger.error(f"Erro ao processar requisição: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao processar requisição: {str(e)}")
 