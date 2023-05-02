from rest_framework import serializers
from .models import CampApplications

class ApplicationSerializer(serializers.ModelSerializer):
    Program = serializers.ChoiceField(choices=CampApplications.PROGRAM_CHOICES)

    class Meta:
        model = CampApplications
        fields =('ParentName', 'Address', 'PhoneNumber', 'CamperName', 'CamperAge', 
                 'CamperGrade', 'Program')

class FullInfoSerializer(serializers.ModelSerializer):
    Program = serializers.ChoiceField(choices=CampApplications.PROGRAM_CHOICES)

    class Meta:
        model = CampApplications
        fields =("__all__")

class DeleteSerializer(serializers.ModelSerializer):
    Program = serializers.ChoiceField(choices=CampApplications.PROGRAM_CHOICES)
    
    class Meta:
        model = CampApplications
        fields =('id', 'Program')