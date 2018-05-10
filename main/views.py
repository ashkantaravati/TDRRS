from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template.loader import get_template
import datetime
from .models import DefenseTime
from main.forms import myForm


def get_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return HttpResponseRedirect('login')
   # return render(request, 'dashboard.html', {'current_time': now})
    

def get_defense_times(request):
    
    #defenseTimeRepo = DefenseTime()
    #defenseTimeRepo.save()

    defenseTimes = DefenseTime.objects.all()

    return render(request, 'defenseTimes.html', {'defenseTimes': defenseTimes})


def do_logout(request):
    logout(request)
    return HttpResponseRedirect('login')

def do_login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('Dashboard')
            
        else:
            return render(request,'login.html')

def get_user_reservations(request):
    return render(request, 'myRequests.html')

def do_submit_reservation(request):
    result={}
    if request.method=='POST':
        defense_time_id=request.POST.get('id',None)
        # some validations...
        defense_time=DefenseTime.objects.filter(id=defense_time_id).first()
        # check 
    #
    #
        result['msg']='درخواست شما: {}'.format(str(defense_time))
    return JsonResponse(result)

def get_ajax_view(request):
    
    if request.method=='GET':
        mf=myForm()
        return render(request,'ajax.html',{'form':mf})
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
        return render(request,'changePassword.html')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('changePassword')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changePassword.html', {
        'form': form
    })
    # elif request.method=='POST':
    #     oldPasswd=request.POST['oldPasswd']
    #     confPasswd=request.POST['confPasswd']
    #     newPasswd=request.POST['newPasswd']
    #     if oldPasswd==confPasswd:
    #         currentUser=request.user
    #         if currentUser.password==oldPasswd:
    #             currentUser.password=newPasswd
    #             currentUser.save()
    #             request.session['result']='با موفقیت انجام شد'
    #         else:
    #             request.session['result']='اطلاعات وارد شده صحیح نمی‌باشد'
    #     else:
    #         request.session['result']='تکرار گذرواژه درست نیست'       
    #     return render(request,'changePassword.html')
