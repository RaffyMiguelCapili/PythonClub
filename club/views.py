from django.shortcuts import render, get_object_or_404

from club.forms import ProductForm
from .models import Resource, TypeResource, Meeting, MeetingMinutes, Event
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'club/index.html')


def members(request):
    members_list=Resource.objects.all()
    return render(request, 'club/members.html', {'members_list': members_list})

def meetingDetail(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingdetail.html', {'meetings' : meeting})

def newMember(request):
    form=ProductForm

    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ProductForm()
    else:
        form=ProductForm()
    return render(request, 'club/newMember.html', {'form': form})

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')
