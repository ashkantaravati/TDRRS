from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.
def get_home(request):
    return render(request,'public/index.html')
def get_schedule(request):
    return render(request,'public/defense_schedule.html')
