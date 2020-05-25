import imaplib
import email
import os
from lib.eml2html import EmailtoHtml
from lib.html2image import HtmltoImage

EMAIL_ADDRESS = 'yseth27@gmail.com'
EMAIL_PSWD = 'ybjbkfmzhxfwytdn'
EMAIL_MAILBOX = 'INBOX'
IMAP_SERVER = 'imap.gmail.com'


class EmailHelper(object):
    def __init__(self, IMAP_SERVER, EMAIL_ADDRESS,
                 EMAIL_PSWD, EMAIL_MAILBOX):
        # logs in to the desired account and navigates to the inbox
        self.mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        self.mail.login(EMAIL_ADDRESS, EMAIL_PSWD)
        self.mail.select()

    def get_emails(self):
        uids = self.mail.uid('SEARCH', 'ALL')[1][0].split()
        return uids

    def get_email_message(self, email_id):
        _, data = self.mail.uid('FETCH', email_id, '(RFC822)')
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        return email_message


email_helper = EmailHelper(IMAP_SERVER, EMAIL_ADDRESS,
                           EMAIL_PSWD, EMAIL_MAILBOX)
email_to_html_convertor = EmailtoHtml()
html_to_image_convertor = HtmltoImage()
uids = email_helper.get_emails()

dir_path = os.path.dirname(os.path.realpath(__file__))
output_dir = os.path.join(dir_path, "images")

for uid in uids[:10]:
    email_message = email_helper.get_email_message(uid)
    html = email_to_html_convertor.convert(email_message)
    filename = uid.decode() + ".jpg"
    pdf_path = html_to_image_convertor.save_image(
        html.encode(), output_dir, filename)
    print(pdf_path)

