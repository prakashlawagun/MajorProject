from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Email
from .serializers import EmailSerializer
from account.models import User
def EmailView(request):
        return render(request,'send_email.html')


class SendEmailView(APIView):
    def post(self, request):
        subject = request.data['subject']
        message = request.data['message']

        # Save the message to the database
        message_obj = Email.objects.create(subject=subject, message=message)
        serializer = EmailSerializer(data =request.data)
        if serializer.is_valid():
             data=serializer.save()

        # Get the list of users from the User model
        recipient_list = User.objects.values_list('email', flat=True)

        # Send the email
        send_mail(data.subject, data.message, settings.EMAIL_HOST_USER , recipient_list, fail_silently=False)

        return Response({'message': 'Email sent successfully'})
