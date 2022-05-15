from django.shortcuts import render
from .models import Resource, TypeResource, Meeting, MeetingMinutes, Event

# Create your views here.
def index(request):
    return render(request, 'club/index.html')


def members(request):
    members_list=Resource.objects.all()
    return render(request, 'club/members.html', {'members_list': members_list})
    