from django.core.mail import EmailMessage


def sendEmail(to,sub,body):
    email = EmailMessage(sub,body,to = ['usamak552@gmail.com','ravikantiwar.21910235@viit.ac.in','rohit.21910004@viit.ac.in'])
    email.send()
    print("email send")