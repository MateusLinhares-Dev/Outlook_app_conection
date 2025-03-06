
def new_workflow_edit_data(title, name_sender, email_sender) -> str:

    xml = f'''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:workflow">
    <soapenv:Header/>
    <soapenv:Body>
        <urn:newWorkflowEditData>
            <!--You may enter the following 6 items in any order-->
            <urn:ProcessID>MERC-GR</urn:ProcessID>
            <urn:WorkflowTitle>{title}</urn:WorkflowTitle>
            <urn:EntityList>
                <!--Zero or more repetitions:-->
                <urn:Entity>
                <urn:EntityID>PNMERC</urn:EntityID>
                <!--Optional:-->
                <urn:EntityAttributeList>
                    <!--Zero or more repetitions:-->
                    <urn:EntityAttribute>
                        <!--You may enter the following 2 items in any order-->
                        <urn:EntityAttributeID>texto4</urn:EntityAttributeID>
                        <urn:EntityAttributeValue>{name_sender}</urn:EntityAttributeValue>
                    </urn:EntityAttribute>
                    <urn:EntityAttribute>
                        <!--You may enter the following 2 items in any order-->
                        <urn:EntityAttributeID>texto23</urn:EntityAttributeID>
                        <urn:EntityAttributeValue>{email_sender}</urn:EntityAttributeValue>
                    </urn:EntityAttribute>
                </urn:EntityAttributeList>
                <!--Optional:-->
                </urn:Entity>
            </urn:EntityList>
        </urn:newWorkflowEditData>
    </soapenv:Body>
    </soapenv:Envelope>
    '''

    return xml

def workflow_edit_data_xml(wf_id, **kwargs) -> str:

    xml = f'''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:workflow">
    <soapenv:Header/>
    <soapenv:Body>
        <urn:editEntityRecord>
            <!--You may enter the following 5 items in any order-->
            <urn:WorkflowID>{wf_id}</urn:WorkflowID>
            <urn:EntityID>PNMERC</urn:EntityID>
            <!--Optional:-->
            <urn:EntityAttributeList>
                <urn:EntityAttribute>
                <!--You may enter the following 2 items in any order-->
                <!--Expediente-->
                    <urn:EntityAttributeID>texto1</urn:EntityAttributeID>
                    <urn:EntityAttributeValue>{kwargs.get('EXPEDIENTE')}</urn:EntityAttributeValue>
                </urn:EntityAttribute>
                <urn:EntityAttribute>
                <!--FECHA-->
                    <urn:EntityAttributeID>texto2</urn:EntityAttributeID>
                    <urn:EntityAttributeValue>{kwargs.get('FECHA')}</urn:EntityAttributeValue>
                </urn:EntityAttribute>
                <urn:EntityAttribute>
                <!--TIENDA-->
                    <urn:EntityAttributeID>texto3</urn:EntityAttributeID>
                    <urn:EntityAttributeValue>{kwargs.get('TIENDA')}</urn:EntityAttributeValue>
                </urn:EntityAttribute>
                <urn:EntityAttribute>
                <!--POBLACIÓN (PROVINCIA)-->
                    <urn:EntityAttributeID>texto5</urn:EntityAttributeID>
                    <urn:EntityAttributeValue>{kwargs.get('POBLACIÓN (PROVINCIA)')}</urn:EntityAttributeValue>
                </urn:EntityAttribute>
                <urn:EntityAttribute>
                <!--DENOMINACIÓN-->
                    <urn:EntityAttributeID>texto6</urn:EntityAttributeID>
                    <urn:EntityAttributeValue>{kwargs.get('DENOMINACIÓN')}</urn:EntityAttributeValue>
                </urn:EntityAttribute>
                <urn:EntityAttribute>
                <!--CÓDIGO-->
                    <urn:EntityAttributeID>texto7</urn:EntityAttributeID>
                    <urn:EntityAttributeValue>{kwargs.get('CÓDIGO')}</urn:EntityAttributeValue>
                </urn:EntityAttribute>
                <urn:EntityAttribute>
                <!--FORMATO-->
                    <urn:EntityAttributeID>texto8</urn:EntityAttributeID>
                    <urn:EntityAttributeValue>{kwargs.get('FORMATO')}</urn:EntityAttributeValue>
                </urn:EntityAttribute>
                <urn:EntityAttribute>
                <!--PROVEEDOR-->
                    <urn:EntityAttributeID>texto9</urn:EntityAttributeID>
                    <urn:EntityAttributeValue>{kwargs.get('PROVEEDOR')}</urn:EntityAttributeValue>
                </urn:EntityAttribute>
                <urn:EntityAttribute>
                <!--BL LOGISTICO-->
                    <urn:EntityAttributeID>texto10</urn:EntityAttributeID>
                    <urn:EntityAttributeValue>{kwargs.get('BL LOGISTICO')}</urn:EntityAttributeValue>
                </urn:EntityAttribute>
                <urn:EntityAttribute>
                <!--LOTE-->
                    <urn:EntityAttributeID>texto11</urn:EntityAttributeID>
                    <urn:EntityAttributeValue>{kwargs.get('LOTE')}</urn:EntityAttributeValue>
                </urn:EntityAttribute>
                <urn:EntityAttribute>
                <!--FECHA CADUCIDAD-->
                    <urn:EntityAttributeID>texto12</urn:EntityAttributeID>
                    <urn:EntityAttributeValue>{kwargs.get('FECHA CADUCIDAD')}</urn:EntityAttributeValue>
                </urn:EntityAttribute>
                <urn:EntityAttribute>
                <!--UNIDADES AFECTADAS-->
                    <urn:EntityAttributeID>texto13</urn:EntityAttributeID>
                    <urn:EntityAttributeValue>{kwargs.get('UNIDADES AFECTADAS')}</urn:EntityAttributeValue>
                </urn:EntityAttribute>
                <urn:EntityAttribute>
                <!--R21-->
                    <urn:EntityAttributeID>texto14</urn:EntityAttributeID>
                    <urn:EntityAttributeValue>{kwargs.get('R21')}</urn:EntityAttributeValue>
                </urn:EntityAttribute>
                <urn:EntityAttribute>
                <!--DESCRIPCIÓN DEL INPUT-->
                    <urn:EntityAttributeID>parrafo1</urn:EntityAttributeID>
                    <urn:EntityAttributeValue>{kwargs.get('DESCRIPCIÓN DEL INPUT')}</urn:EntityAttributeValue>
                </urn:EntityAttribute>
            </urn:EntityAttributeList>
        </urn:editEntityRecord>
    </soapenv:Body>
    </soapenv:Envelope>
    '''

    return xml

def workflow_execute_activity_xml(workflow_id):

    xml = f'''
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:workflow">
        <soapenv:Header/>
        <soapenv:Body>
            <urn:executeActivity>
                <!--You may enter the following 5 items in any order-->
                <urn:WorkflowID>{workflow_id}</urn:WorkflowID>
                <urn:ActivityID>DT-REC</urn:ActivityID>
                <urn:ActionSequence>1</urn:ActionSequence>
            </urn:executeActivity>
        </soapenv:Body>
        </soapenv:Envelope>    
    '''

    return xml