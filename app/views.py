from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    tn=input('enter a topic name')  
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('Topic created successfully')
def insert_Webpages(request):
    tn=input('enter a topic name')  
    name=input('Enter name of')
    url=input('Enter url')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpages.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    return HttpResponse('Webpages created successfully')
def insert_AccessRecords(request):
    tn=input('enter a topic name')
    name=input('Enter name of')
    url=input('Enter url')
    date=input('Enter date')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpages.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    A=AccessRecords.objects.get_or_create(name=W,date=date)[0]
    A.save()
    return HttpResponse('Accessrecords created successfully')
