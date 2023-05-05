from rest_framework import serializers
from .models import CampApplications

#Serializer for Registration Submission
class ApplicationSerializer(serializers.ModelSerializer):
    Program = serializers.ChoiceField(choices=CampApplications.PROGRAM_CHOICES)
    regstatus = serializers.ChoiceField(choices=CampApplications.REGISTRATION_CHOICES)

    class Meta:
        model = CampApplications
        fields =('ParentName', 'Address', 'CamperName', 'CamperAge', 
                 'CamperGrade', 'PhoneNumber', 'Email', 'Program', 'regstatus')

#Serializer for All Account Information
class FullInfoSerializer(serializers.ModelSerializer):
    Program = serializers.ChoiceField(choices=CampApplications.PROGRAM_CHOICES)

    class Meta:
        model = CampApplications
        fields =("__all__")

#Serializer used to Delete Account
class DeleteSerializer(serializers.Serializer):
    students = serializers.ListField(child=serializers.DictField())

    def validate(self, data):
        students = data.get('students')
        if not students:
            raise serializers.ValidationError('Missing students data')
        for student in students:
            if not all(key in student for key in ['id', 'Program']):
                raise serializers.ValidationError('Invalid student data')
        return data

class CampApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampApplications
        fields = ['id', 'CamperName', 'CamperAge', 'CamperGrade', 'PhoneNumber', 'Email', 'Program', 'regstatus']
