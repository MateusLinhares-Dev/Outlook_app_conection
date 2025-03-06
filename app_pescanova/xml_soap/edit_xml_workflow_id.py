import xml.etree.ElementTree as ET

def update_workflow_id(xml_string, workflow_id):
    """Atualiza o WorkflowID dentro de um XML já gerado."""
    root = ET.fromstring(xml_string)
    
    # Localiza a tag <urn:WorkflowID> e substitui o valor
    ns = {"urn": "urn:workflow"}
    workflow_id_tag = root.find(".//urn:WorkflowID", ns)
    if workflow_id_tag is not None:
        workflow_id_tag.text = workflow_id

    return ET.tostring(root, encoding="utf-8", method="xml").decode('utf-8')