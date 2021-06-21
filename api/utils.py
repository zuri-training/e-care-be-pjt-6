from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from django.core.mail import send_mail
from rest_framework import status


@api_view(['POST'])
@parser_classes([JSONParser])
def mail_view(request, format=None):
    return (request.data)


class SendMail:
    @staticmethod
    def verification_mail(request):

        mail = mail_view(request)

        subject = mail["subject"]
        message = mail["message"]
        email = mail["email"]

        try:
            send_mail(subject, message, EMAIL_HOST_USER,
                      [email])

        # to protect the app from hackers trying to insert bad email headers
        except BadHeaderError:
            # not sure of th error that is suppodsed to be here
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
