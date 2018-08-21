from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.get_home,name='home'),
   url(r'^defense-schedule', views.get_schedule,name='defense_schedule'),
   url(r'^defense-announcement/(?P<dsid>[0-9]+)/$',views.get_announcement,name='defense_announcement'),
   url(r'^guide',views.guide,name='guide'),
   url(r'^test', views.test,name='test'),

]