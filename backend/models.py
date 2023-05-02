from django.db import models


def assignStatus():
    currApp = CampApplications.objects.latest('CreationTime')
    print(currApp.Program)
    print(CampApplications.objects.filter(Program=currApp.Program, Status=True).count())
    if CampApplications.objects.filter(Program=currApp.Program, Status=True).count() < 16:
        currApp.Status = True
        currApp.save()
    return



def deleteApp(objectID, campProgram):
    CampApplications.objects.get(objectID).delete()

    if CampApplications.objects.filter(Program=campProgram).count() < 16 and CampApplications.objects.filter(Program=campProgram, Status=False).count() > 0:
        toBeAccepted = CampApplications.objects.filter(Program=campProgram, status=False)
        toBeAccepted.update(status=True)
    
    return

# Create your models here.
class CampApplications(models.Model):
    PROGRAM_CHOICES = (
    ('Bio', 'Biophysical'),
    ('Robotics', 'Robotics'),
    ('Cyber', 'Cyber Security'),
    ('Cryptography', 'Cryptography'),
    )

    id = models.BigAutoField(auto_created=True, primary_key=True)
    ParentName = models.CharField(max_length=20)
    Address = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=12)
    Email = models.CharField(max_length=50)
    CamperName = models.CharField(max_length=20)
    CamperAge = models.IntegerField()
    CamperGrade = models.IntegerField()
    Program = models.CharField(max_length=25, choices=PROGRAM_CHOICES, default='Biophysical')
    Status = models.BooleanField(auto_created=True, default=False)
    CreationTime = models.DateTimeField(auto_now_add=True)