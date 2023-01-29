from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
def display_topics(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='Cricket')
    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='Cricket')
    QSW=Webpage.objects.exclude(topic_name='Cricket')
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.order_by('-name')
    QSW=Webpage.objects.filter(topic_name='Football').order_by('-name')    
    QSW=Webpage.objects.all().order_by(Length('name'))    
    QSW=Webpage.objects.all().order_by(Length('name').desc())
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(url__startswith='https')
    QSW=Webpage.objects.filter(url__endswith='com')
    
    QSW=Webpage.objects.filter(name__startswith='D')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name__contains='d')    
    QSW=Webpage.objects.filter(name__regex='\w{7}')
    QSW=Webpage.objects.filter(name__in=['dhoni','chinmayii','uma'])
    QSW=Webpage.objects.filter(Q(topic_name='Cricket') | Q(name='ViratKohli'))
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(Q(topic_name='Rugby') & Q(url__startswith='https'))
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)
    
def display_access(request):
    QSA=AccessRecords.objects.all().order_by('date')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date='2001-11-30')    
    QSA=AccessRecords.objects.filter(date__gt='2001-11-30')    
    QSA=AccessRecords.objects.filter(date__gte='2001-11-30') 
    QSA=AccessRecords.objects.filter(date__lte='2001-11-30')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date__year='2001')  
    QSA=AccessRecords.objects.filter(date__month='11')    
    QSA=AccessRecords.objects.filter(date__day='30')   
    QSA=AccessRecords.objects.filter(date__year__gt='2001')
    d={'access':QSA}
    return render(request,'display_access.html',d)


def update_webpage(request):
    #Webpage.objects.filter(name='uma').update(url='https://uma.in')
    #Webpage.objects.filter(topic_name='Cricket').update(name='MSD')
    #Webpage.objects.filter(name='chinmayii').update(topic_name='Cricket')
    #Webpage.objects.filter(name='Geetha').update(topic_name='Hockey')
    #Webpage.objects.update_or_create(name='sandhya',defaults={'url':'https://sandhya.in'})
    #Webpage.objects.update_or_create(name='MSD',defaults={'url':'https://MSD.in'})
    T=Topic.objects.get_or_create(topic_name='Cricket')[0]
    T.save()
    Webpage.objects.update_or_create(name='dhoni',defaults={'topic_name':C,'url':'https://dhoni.in'})

    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)


def delete_webpage(request):
    #Webpage.objects.filter(name='Geetha').delete()
    #Webpage.objects.filter(topic_name='Football').delete()
    #Webpage.objects.filter(name='ViratKholi').delete()
    Webpage.objects.all().delete()
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)

   

