from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction


# Create your views here.

# GET and POST procedures for the registration
@api_view(['GET', 'POST'])
def registration(request):
    if request.method == 'GET':
        data = CampApplications.objects.all()
        serializer = FullInfoSerializer(data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_students(request):
    if request.method == 'DELETE':
        serializer = DeleteSerializer(data=request.data)
        if serializer.is_valid():
            students_to_delete = serializer.validated_data.get('students')
            for student in students_to_delete:
                student_id = student.get('id')
                student_program = student.get('Program')
                CampApplications.objects.filter(id=student_id, Program=student_program).delete()
            return Response("Successfully deleted")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def update_status(request):
    students = request.data.get('students')
    print(request.data)

    if not isinstance(students, list):
        return Response({'error': 'Invalid format for students data'}, status=status.HTTP_400_BAD_REQUEST)

    student_objs = []
    errors = []

    with transaction.atomic():
        for student in students:
            try:
                obj = CampApplications.objects.get(id=student['id'])
                obj.regstatus = student['regstatus']
                student_objs.append(obj)
            except CampApplications.DoesNotExist:
                errors.append({'id': student['id'], 'message': 'Student does not exist'})
            except Exception as e:
                errors.append({'id': student['id'], 'message': str(e)})

        if errors:
            return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

        CampApplications.objects.bulk_update(student_objs, ['regstatus'])

    updated_students = CampApplicationSerializer(student_objs, many=True).data
    return Response({'updated_students': updated_students}, status=status.HTTP_200_OK)


# Camp Management Email
@api_view(['POST'])
def send_emails(request):
    camp = request.data.get('camp')
    subject = request.data.get('subject')
    message = request.data.get('message')

    if not (camp and subject and message):
        return Response({'error': 'Missing parameters'}, status=status.HTTP_400_BAD_REQUEST)

    # Get the emails for the selected camp from your database or wherever you store them
    emails = getEmails(camp)

    if not emails:
        return Response({'error': 'No emails found for the selected camp'}, status=status.HTTP_400_BAD_REQUEST)

    # Send the emails using Django's send_mail function
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=emails,
        fail_silently=False,
    )

    return Response({'success': 'Emails sent successfully'}, status=status.HTTP_200_OK)


