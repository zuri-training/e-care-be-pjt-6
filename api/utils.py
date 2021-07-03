from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
import json


def json_confirmation(request):
  try:
    data = json.loads(str(request))
  except ValueError:
    return ("error")
  return data

def mail_Function(request):
    data = json_confirmation(request)
    reciever = data["email"]
    subject = data["subject"]
    Body = data["body"]
    send_mail(subject, Body, EMAIL_HOST_USER, [reciever])
    return ("ok")
