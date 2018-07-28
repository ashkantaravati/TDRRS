from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^student/', include('student.urls')),
    url(r'^', include('public.urls'))
]
