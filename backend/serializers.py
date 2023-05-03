from rest_framework import serializers
from .models import CampApplications

#Serializer for Registration Submission
class ApplicationSerializer(serializers.ModelSerializer):
    Program = serializers.ChoiceField(choices=CampApplications.PROGRAM_CHOICES)

    class Meta:
        model = CampApplications
        fields =('ParentName', 'Address', 'PhoneNumber', 'CamperName', 'CamperAge', 
                 'CamperGrade', 'Program')

#Serializer for All Account Information
class FullInfoSerializer(serializers.ModelSerializer):
    Program = serializers.ChoiceField(choices=CampApplications.PROGRAM_CHOICES)

    class Meta:
        model = CampApplications
        fields =("__all__")

#Serializer used to Delete Account
class DeleteSerializer(serializers.ModelSerializer):
    Program = serializers.ChoiceField(choices=CampApplications.PROGRAM_CHOICES)
    
    class Meta:
        model = CampApplications
        fields =('id', 'Program')
