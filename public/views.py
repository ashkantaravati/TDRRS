from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from student.models import *

# Create your views here.
def get_home(request):
    return render(request,'public/index.html')
def get_schedule(request):
    schedules=DefenseSession.objects.all()
    #TODO filter to current semester
    return render(request,'public/defense_schedule.html',{'schedules':schedules})
