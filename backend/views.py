from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.

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
            assignStatus()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['DELETE'])
def deleteReq(request):
    if request.method == 'DELETE':
        serializer = DeleteSerializer(data=request.data)
        if serializer.is_valid():
            deleteID = serializer.validated_data.get('id')
            deleteProgram = serializer.validated_data.get('Program')
            deleteApp(deleteID, deleteProgram)

class RegistrationView(generics.CreateAPIView):
    queryset = CampApplications.objects.all()
    serializer_class = ApplicationSerializer