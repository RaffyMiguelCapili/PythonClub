from django.contrib import admin
from .models import Meeting, MeetingMinutes, Resource, Event, TypeResource
# Register your models here.

admin.site.register(Meeting)
admin.site.register(MeetingMinutes)
admin.site.register(Resource)
admin.site.register(Event)
admin.site.register(TypeResource)