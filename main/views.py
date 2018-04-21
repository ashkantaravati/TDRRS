from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
import datetime
from .models import DefenseTime
from django.contrib.auth import authenticate,logout,login

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect('login')
   # return render(request, 'index.html', {'current_time': now})
    


def simple(request):
    return HttpResponse('<h1>salam</h1> <h2>{}</h2>'.format(request.GET.get('q','')))

def readAllDefenseTimes(request):
    
    #defenseTimeRepo = DefenseTime()
    #defenseTimeRepo.save()

    defenseTimes = DefenseTime.objects.all()

    return render(request, 'defenseTimes.html', {'defenseTimes': defenseTimes})


def doLogout(request):
    logout(request)
    return HttpResponseRedirect('login')

def doLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('index')
        
    else:
        return HttpResponse('failed')