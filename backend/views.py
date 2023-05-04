from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse

# Create your views here.

#GET and POST procedures for the registration
@api_view(['GET', 'POST'])
def registration(request):
    if request.method == 'GET':
        data = CampApplications.objects.all()

        serializer = FullInfoSerializer(data, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ApplicationSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Delete Account Button - Still need frontend delete Button
@api_view(['DELETE'])
def deleteReq(request):
    if request.method == 'DELETE':
        serializer = DeleteSerializer(data=request.data)
        if serializer.is_valid():
            deleteID = serializer.validated_data.get('id')
            deleteProgram = serializer.validated_data.get('Program')
            deleteApp(deleteID, deleteProgram)

# Camp Management Email
@api_view(['POST'])
def send_emails(request):
    camp = request.data.get('camp')
    subject = request.data.get('subject')
    message = request.data.get('message')
    
    if not (camp and subject and message):
        return JsonResponse({'error': 'Missing parameters'})

    # Get the emails for the selected camp from your database or wherever you store them
    emails = getEmails(camp)
    
    for address in emails:
        email_list = address

    if not emails:
        return JsonResponse({'error': 'No emails found for the selected camp'})

    # Send the emails using Django's send_mail function
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=email_list,
        fail_silently=False,
    )

    return JsonResponse({'success': 'Emails sent successfully'})

