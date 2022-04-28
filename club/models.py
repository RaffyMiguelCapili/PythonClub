from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Create model classes for the python club database. These should include:
#Meeting which will have fields for meeting title, meeting date, meeting time, location, Agenda
#Meeting Minutes which will have fields for meeting id (a foreign key), attendance (a many to many field with User), Minutes text
#Resource which will have fields for resource name, resource type, URL, date entered, user id (foreign key with User), and description
#Event which will have fields for event title, location, date, time, description and the user id of the member that posted it
#register the models in admin.py
#Create and troubleshoot the models, and then make migrations and migrate
#Create a superuser and open the admin site
#Upload the code to GitHub and post the url in canvas



class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.DateTimeField(auto_now=False, auto_now_add=False)
    meetinglocation=models.TextField(null=True, blank=True)
    meetingagenda=models.CharField(max_length=255)

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='Meeting'


class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    meetingattendance=models.ManyToManyField(User)
    meetingminutestext=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingid

    class Meta:
        db_table='MeetingMinutes'


class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.ForeignKey(MeetingMinutes, on_delete=models.DO_NOTHING)
    resourceurl=models.URLField()
    resourcedateentered=models.DateField()
    resourceuserid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='Resource'


class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.TextField(null=True, blank=True)
    eventdate=models.DateField()
    eventtime=models.DateTimeField()
    eventdescription=models.TextField(null=True, blank=True)
    eventuserid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='Event'







