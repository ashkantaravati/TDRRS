from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from student.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def get_home(request):
    return render(request,'public/index.html')
def get_schedule(request):
    queried_schedules=DefenseSession.objects.all()
    #TODO filter to current semester
    page = request.GET.get('page', 1)
    paginator = Paginator(queried_schedules, 5)
    try:
        page_schedules = paginator.page(page)
    except PageNotAnInteger:
        page_schedules = paginator.page(1)
    except EmptyPage:
        page_schedules = paginator.page(paginator.num_pages)
    return render(request,'public/defense_schedule.html',{'schedules':page_schedules})
def get_announcement(request,dsid):
    session=DefenseSession.objects.get(pk=dsid)
    return render(request,'public/announcement.html',{'session':session})
