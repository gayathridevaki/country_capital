from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def display_country(request):
    QLCO=Country.objects.all()
    d={'country':QLCO}
    return render(request,'display_country.html',d)

def display_capital(request):
    QLAO=Capital.objects.all()
    d={'capital':QLAO}
    return render(request,'display_capital.html',d)


def insert_country(request):
    cn=input('enter country:')
    NCO=Country.objects.get_or_create(Country_Name=cn)[0]
    NCO.save()
    return HttpResponse('country is created')

def insert_capital(request):
    Cn=input('enter country:')
    can=input('enter capital:')
    NAO=Capital.objects.get_or_create(Country_Name=Cn,Capital_Name=can)[0]
    NAO.save()
    return HttpResponse('country is created')
