from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .models import Camp

@api_view(['POST'])
def send_emails(request):
    camp = request.data.get('camp')
    subject = request.data.get('subject')
    message = request.data.get('message')

    if not (camp and subject and message):
        return JsonResponse({'error': 'Missing parameters'})

    # Get the emails for the selected camp from your database or wherever you store them
    # Here we assume that you have a Camp model with an email field
    emails = [camp.email for camp in Camp.objects.filter(name=camp)]

    if not emails:
        return JsonResponse({'error': 'No emails found for the selected camp'})

    # Send the emails using Django's send_mail function
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=emails,
        fail_silently=False,
    )

    return JsonResponse({'success': 'Emails sent successfully'})