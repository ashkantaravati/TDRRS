from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
import datetime

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect('login')
   # return render(request, 'index.html', {'current_time': now})
    

def login(request):
   # return render(request, 'index.html', {'current_time': now})
    return render(request, 'login.html')
   

def simple(request):
    return HttpResponse('<h1>salam</h1> <h2>{}</h2>'.format(request.GET.get('q','')))

def readAllTimes():
    return ''