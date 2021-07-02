from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
import json


def Json_confirmed(request):
  try:
    data = json.loads(str(request))
  except ValueError:
    return ("error")
  return data

def mail_Function(request):
    data = Json_confirmed(request)
    reciever = data["email"]
    subject = data["subject"]
    Body = data["body"]
    send_mail(subject, Body, EMAIL_HOST_USER, [reciever])
    return ("ok")
