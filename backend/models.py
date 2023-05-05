from django.db import models

#Takes newly added registration and determines if they're waitlisted or registered
def assignStatus():
    currApp = CampApplications.objects.latest('CreationTime')
    print(currApp.Program)
    print(CampApplications.objects.filter(Program=currApp.Program, regstatus=True).count())
    if CampApplications.objects.filter(Program=currApp.Program, regstatus=True).count() < 16:
        currApp.regstatus = True
        currApp.save()
    return

def getEmails(campProgram):
    handler = CampApplications.objects.filter(Program=campProgram)
    list = []

    if handler.count() == 0:
        return list
    
    return handler.values_list('Email')

#Deletes application then determines if a new user can be taken off the waitlist
def deleteApp(objectID, campProgram):
    CampApplications.objects.get(objectID).delete()

    if CampApplications.objects.filter(Program=campProgram).count() < 16 and CampApplications.objects.filter(Program=campProgram, regstatus=False).count() > 0:
        toBeAccepted = CampApplications.objects.filter(Program=campProgram, status=False)
        toBeAccepted.update(status=True)
    
    return

# Create your models here.
class CampApplications(models.Model):
    PROGRAM_CHOICES = (
    ('Biophysical', 'Biophysical'),
    ('Robotics', 'Robotics'),
    ('Cyber Security', 'Cyber Security'),
    ('Cryptography', 'Cryptography'),
    )

    REGISTRATION_CHOICES = (
        ('Registered', 'Registered'),
        ('Paid', 'Paid'),
        ('Waiting List', 'Waiting List')
    )

    id = models.BigAutoField(auto_created=True, primary_key=True)
    ParentName = models.CharField(max_length=20)
    Address = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=12)
    Email = models.CharField(max_length=50)
    CamperName = models.CharField(max_length=20)
    CamperAge = models.IntegerField()
    CamperGrade = models.CharField(max_length=20)
    Program = models.CharField(max_length=25, choices=PROGRAM_CHOICES, default='Biophysical')
    regstatus = models.CharField(max_length=20, choices=REGISTRATION_CHOICES, default='Waiting List')
    CreationTime = models.DateTimeField(auto_now_add=True)

