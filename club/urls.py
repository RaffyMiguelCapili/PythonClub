from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('members/', views.members, name= 'members'),  
    path('meetingdetail/<int:id>', views.meetingDetail, name='detail'),
    path('newmember/', views.newProduct, name='newmember'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),

]