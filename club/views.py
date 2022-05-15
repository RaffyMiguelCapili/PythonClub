from django.shortcuts import render, get_object_or_404
from .models import Resource, TypeResource, Meeting, MeetingMinutes, Event

# Create your views here.
def index(request):
    return render(request, 'club/index.html')


def members(request):
    members_list=Resource.objects.all()
    return render(request, 'club/members.html', {'members_list': members_list})

def meetingDetail(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingdetail.html', {'meetings' : meeting})

    