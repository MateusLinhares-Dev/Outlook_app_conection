from app_pescanova.get_folder_messages import get_messages, get_complaint, get_attachments


def main():

    emails = get_messages()  
    email_response_complaint = get_complaint(emails)
    get_attachments(email_response_complaint)

    


if __name__ == "__main__":
    main()