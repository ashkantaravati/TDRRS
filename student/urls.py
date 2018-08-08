from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_dashboard, name='dashboard'),
    url(r'^dashboard',views.get_dashboard,name='dashboard'),
    url(r'^login',views.do_login, name='login'),
    url(r'^defense-times',views.defense_times, name='defense_times'),
    #url(r'^user-requests',views.get_user_reservations, name='user_requests'),    
    url(r'^logout$',views.do_logout, name='logout'),
    url(r'^change-password',views.do_change_password, name='change_password'),   
    # url(r'^ajax',views.get_ajax_view, name='AjaxView'),
    # url(r'^submit-reservation',views.do_submit_reservation, name='submit_reservation'),
    url(r'^cancel-reservation',views.do_submit_cancellation, name='cancel_reservation'),
]
