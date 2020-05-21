import email

from imapclient import IMAPClient

HOST = 'imap.gmail.com'
USERNAME = 'yseth27@gmail.com'
PASSWORD = 'dyberwbzzmyjsece'

with IMAPClient(HOST) as client:
    client.login(USERNAME, PASSWORD)
    client.select_folder('INBOX', readonly=True)

    messages = client.search('ALL')
    for i in range (10):
        uid, message_data = client.fetch(messages, 'RFC822').items()
        email_message = email.message_from_bytes(message_data[b'RFC822'])
        print(uid, email_message.get('From'), email_message.get('Subject'))
