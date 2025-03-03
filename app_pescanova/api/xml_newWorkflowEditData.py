
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