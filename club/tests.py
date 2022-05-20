from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, TypeResource, Resource, Event
import datetime

# Create your tests here.

class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle= 'Bobs')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Bobs')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Meeting')

class TypeResourceTest(TestCase):
    def setUp(self):
        self.type=TypeResource(typeresourcename= 'Members')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Members')

    def test_tablename(self):
        self.assertEqual(str(TypeResource._meta.db_table), 'ResourceType')

class ResourceTest(TestCase):
    def setUp(self):
        self.resourcetype=Resource(resourcename= 'Members')
        self.resourceuserid=User(username='Joe')
        self.resource= Resource(resourcename= 'Joe Bamba', resourcedateentered=datetime.date(2022,5,10), resourceurl='http://www.google.com', resourcedescription='N/A', resourceuserid=self.resourceuserid)

    def test_string(self):
        self.assertEqual(str(self.resource), 'Joe Bamba')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'Resource')

class EventTest(TestCase):
    def setUp(self):
        self.type=Event(eventtitle= 'Test Event')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Test Event')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'Event')

class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.meetingid=Meeting(meetingtitle= 'Test Event')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'MeetingMinutes')


