from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template.loader import get_template
import datetime
from .models import DefenseTime,ReservationRequest,DefenseSession
from student.forms import myForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.crypto import get_random_string

# TODO authorization
def get_dashboard(request):
    current_user=request.user
    if current_user.is_authenticated:
        current_student=current_user.student
        reservation_requests=ReservationRequest.objects.filter(requesting_student=current_student).order_by('-status')
        current_defense=current_student.defensesession_set.get(is_archived=False)
        current_context={
            'reservation_requests': reservation_requests,
            'current_defense':current_defense
        }
        return render(request, 'student/dashboard.html',current_context)
    else:
        return HttpResponseRedirect('login')

def get_defense_times(request):
    queried_defense_times = DefenseTime.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(queried_defense_times, 5)
    try:
        page_defense_times = paginator.page(page)
    except PageNotAnInteger:
        page_defense_times = paginator.page(1)
    except EmptyPage:
        page_defense_times = paginator.page(paginator.num_pages)
    return render(request, 'student/defense_times.html', {'defense_times': page_defense_times})


def do_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def do_login(request):
    if request.method=='GET':
        return render(request,'student/loginBs.html')        
        #return render(request,'student/login.html')
    elif request.method=='POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('dashboard')
            
        else:
            return render(request,'student/loginBs.html')        
            #return render(request,'student/login.html')
            
def do_submit_reservation(request):
    result={}
    current_student=request.user.student
    if request.method=='POST':
        if current_student.has_active_request:
            result['msg']='درخواست فعال دارید!'
        else:
            defense_time_id=request.POST.get('id',None)
            defense_time=DefenseTime.objects.filter(id=defense_time_id).first()
            try:
                reservereq=ReservationRequest.objects.create(
                    requested_defense_time=defense_time,
                    request_date_time=datetime.datetime.now(),
                    requesting_student=current_student,
                    tracing_code=get_random_string(length=12),
                    status=0,
                    )
                current_student.has_active_request=True
                current_student.save()
                result['msg']='درخواست شما: {} با موفقیت ثبت شد'.format(str(defense_time))
            except Exception as err:
                result['msg']='خطا {}'.format(err)
    #
    return JsonResponse(result)

def do_submit_cancellation(request):
    pass

def get_ajax_view(request):
    
    if request.method=='GET':
        mf=myForm()
        return render(request,'student/ajax.html',{'form':mf})
    if request.method=='POST':
        #mf=myForm(request.POST)
        data={}
        data['user']=request.user.__str__()
        #data['fn']=mf.firstName
        data['firstName']=request.POST['firstName']        
        data['time']=datetime.datetime.now()
        print(request.POST)
        print(data)
        return JsonResponse(data)
        
def do_change_password(request):
    request.session['result']=''
    if request.method=='GET':
        request.session['result']=''    
        return render(request,'student/change_password.html')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'student/change_password.html', {
        'form': form
    })
    