from djoser.email import PasswordResetEmail
from django.core.mail import send_mail

def send_email(special, context, to):    
    PasswordResetEmail(special,context).send(to)

def sender(subject,message,from_email, receiver):
    
    send_mail(subject, message, from_email, receiver)
