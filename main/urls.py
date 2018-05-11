from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_dashboard, name='Dashboard'),
    url(r'^app/dashboard',views.get_dashboard,name='Dashboard'),
    url(r'^app/login$',views.do_login,name='login'),
    url(r'^app/defense-times',views.get_defense_times,name='DefenseTimes'),
    url(r'^app/user-requests',views.get_user_reservations,name='UserRequests'),    
    url(r'^app/logout$',views.do_logout,name='logout'),
    url(r'^app/change-password',views.do_change_password,name='ChangePassword'),   
    url(r'^app/ajax',views.get_ajax_view,name='AjaxView'),
    url(r'^app/submit-reservation',views.do_submit_reservation,name='SubmitReservation'),
    url(r'^app/cancel-reservation',views.do_submit_cancellation,name='CancelReservation'),
]