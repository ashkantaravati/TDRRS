from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_dashboard, name='Dashboard'),
    url(r'^dashboard',views.get_dashboard,name='Dashboard'),
    url(r'^login$',views.do_login,name='login'),
    url(r'^defense-times',views.get_defense_times,name='DefenseTimes'),
    url(r'^user-requests',views.get_user_reservations,name='UserRequests'),    
    url(r'^logout$',views.do_logout,name='logout'),
    url(r'^change-password',views.do_change_password,name='ChangePassword'),   
    url(r'^ajax',views.get_ajax_view,name='AjaxView'),
    url(r'^submit-reservation',views.do_submit_reservation,name='SubmitReservation'),
    
]