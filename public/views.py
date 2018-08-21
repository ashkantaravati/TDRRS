from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from student.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_tables2 import RequestConfig
from .tables import SessionTable

def get_home(request):
    return render(request,'public/index.html')
def get_schedule(request):
    queried_schedules=DefenseSession.objects.filter(is_archived=False)
    #TODO filter to current semester -- is_scheduled=True
    page = request.GET.get('page', 1)
    paginator = Paginator(queried_schedules, 5)
    try:
        page_schedules = paginator.page(page)
    except PageNotAnInteger:
        page_schedules = paginator.page(1)
    except EmptyPage:
        page_schedules = paginator.page(paginator.num_pages)
    return render(request,'public/defense_schedule.html',{'schedules':page_schedules})
def test(request):
    table = SessionTable(DefenseSession.objects.filter(is_archived=False))
    RequestConfig(request).configure(table)
    return render(request,'public/anon2.html',{'table':table})
def get_announcement(request,dsid):
    session=DefenseSession.objects.get(pk=dsid)
    return render(request,'public/announcement.html',{'session':session})

def guide(request):
    return render(request,'public/guide.html')