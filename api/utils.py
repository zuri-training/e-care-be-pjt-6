from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

def send_mail_to(request):
    sender = EMAIL_HOST_USER
    reciever = request["email"]
    subject = request["subject"]
    body = request["body"]
    send_mail(subject, body, sender, [reciever])
