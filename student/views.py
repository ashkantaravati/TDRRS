from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template.loader import get_template
import datetime
from .models import DefenseTime,ReservationRequest,DefenseSession,Semester
from student.forms import myForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required
def get_dashboard(request):
    current_user=request.user
    if current_user.is_authenticated:
        if current_user.student==None: #TODO doesn't do anything. handle it!
            return HttpResponse('پرونده دانشجویی معتبر ندارید!')
        current_student=current_user.student
        reservation_requests=ReservationRequest.objects.filter(requesting_student=current_student).order_by('-status')
        current_defense=current_student.defensesession_set.get(is_archived=False)
        if current_defense==None:
            return HttpResponse('مجاز به استفاده از سیستم نیستید!')
        current_context={
            'reservation_requests': reservation_requests,
            'current_defense':current_defense
        }
        return render(request, 'student/dashboard.html',current_context)
    else:
        return HttpResponseRedirect('login')
@login_required
def defense_times(request):
    if request.method=='GET':
        queried_defense_times = DefenseTime.objects.filter(status=1)
        current_semester = Semester.current_semester()
        #TODO filter to current_semester
        page = request.GET.get('page', 1)
        paginator = Paginator(queried_defense_times, 5)
        try:
            page_defense_times = paginator.page(page)
        except PageNotAnInteger:
            page_defense_times = paginator.page(1)
        except EmptyPage:
            page_defense_times = paginator.page(paginator.num_pages)
        print(current_semester)
        return render(request, 'student/defense_times.html', {
            'defense_times': page_defense_times,
            'current_semester': current_semester
            })
    if request.method=='POST':
        result={}
        current_student=request.user.student
        if current_student.has_active_request:
            result['msg']='درخواست فعال دارید!'
        else:
            defense_time_id=request.POST.get('id',None)
            defense_time=DefenseTime.objects.get(id=defense_time_id)
            try:
                if defense_time.status==1:
                    defense_time.status=0
                    defense_time.save()

                    reservereq=ReservationRequest.objects.create(
                        requested_defense_time=defense_time,
                        request_date_time=datetime.datetime.now(),
                        requesting_student=current_student,
                        tracing_code=get_random_string(length=12),
                        status=0,
                        )
                    current_student.has_active_request=True
                    current_student.save()
                    current_defense=current_student.defensesession_set.get(is_archived=False)
                    current_defense.designated_defense_time=defense_time 
                    current_defense.save()      
                    result['msg']='درخواست شما: {} با موفقیت ثبت شد'.format(str(defense_time))
                else:
                    result['msg']='متاسفانه رزرو شده است'
            except Exception as err:
                result['msg']='خطا {}'.format(err)
                #TODO if failed before inserting record, revert status to 1 
        return JsonResponse(result)

@login_required
def do_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def do_login(request):
    redir=''
    if request.method=='GET':
        redir=request.GET.get('next')
        return render(request,'student/login.html')        
    elif request.method=='POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if redir:
                return HttpResponseRedirect(redir)
            return HttpResponseRedirect('dashboard')
        else:
            request.session['error']='کاربری با این مشخصات وجود ندارد'
            return render(request,'student/login.html')

# def do_submit_reservation(request):
#     result={}
#     current_student=request.user.student
#     if request.method=='POST':
#         if current_student.has_active_request:
#             result['msg']='درخواست فعال دارید!'
#         else:
#             defense_time_id=request.POST.get('id',None)
#             defense_time=DefenseTime.objects.filter(id=defense_time_id).first()
#             try:
#                 reservereq=ReservationRequest.objects.create(
#                     requested_defense_time=defense_time,
#                     request_date_time=datetime.datetime.now(),
#                     requesting_student=current_student,
#                     tracing_code=get_random_string(length=12),
#                     status=0,
#                     )
#                 current_student.has_active_request=True
#                 current_student.save()
#                 result['msg']='درخواست شما: {} با موفقیت ثبت شد'.format(str(defense_time))
#             except Exception as err:
#                 result['msg']='خطا {}'.format(err)
#     #
#     return JsonResponse(result)
@login_required
@csrf_exempt
def do_submit_cancellation(request):
    if request.method=='POST':
        current_student=request.user.student
        result={}
        reservation_request_id=request.POST.get('id',None)
        reservation_request=ReservationRequest.objects.get(id=reservation_request_id)
        if reservation_request.requesting_student==current_student:
            if reservation_request.status==0:
                submitted_defense_time=reservation_request.requested_defense_time
                current_defense=current_student.defensesession_set.get(is_archived=False)
                try:
                    current_defense.designated_defense_time=None
                    current_defense.save()
                    current_student.has_active_request=False
                    current_student.save()
                    submitted_defense_time.status=1
                    submitted_defense_time.save()
                    reservation_request.status=1
                    reservation_request.save()
                    result['msg']='درخواست شما: {} با موفقیت حذف شد. F5 بزنید'.format(str(reservation_request))
                except Exception as err:
                    result['msg']='خطا {}'.format(err)
            else:
                result['msg']='امکان لغو وجود ندارد'
        else:
            result['msg']='عملیات غیر مجاز!'
        return JsonResponse(result)

# def get_ajax_view(request):
    
#     if request.method=='GET':
#         mf=myForm()
#         return render(request,'student/ajax.html',{'form':mf})
#     if request.method=='POST':
#         data={}
#         data['user']=request.user.__str__()
#         #data['fn']=mf.firstName
#         data['firstName']=request.POST['firstName']        
#         data['time']=datetime.datetime.now()
#         print(request.POST)
#         print(data)
#         return JsonResponse(data)
@login_required    
def do_change_password(request):
    # request.session['result']=''
    # if request.method=='GET':
    #     request.session['result']=''    
    #     return render(request,'student/change_password.html')
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
    