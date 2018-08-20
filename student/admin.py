from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin
from . import models
# Register your models here.

#you need import this for adding jalali calander widget

class DefenseTimeAdmin(admin.ModelAdmin):
    list_filter = (
        ('occurrence_date', JDateFieldListFilter),
    )


# admin.site.index_template = 'admin2/index.html'
# admin.site.login_template = 'admin2/login.html'
# admin.site.logout_template=''
# admin.site.password_change_done_template=''
# admin.site.password_change_template=''
# admin.site.app_index_template = 'admin2/app_index.html'

admin.site.register(models.DefenseTime, DefenseTimeAdmin)
#admin.site.register(BarTime, BarTimeAdmin)
admin.site.register(models.Semester)
admin.site.register(models.DefensePlace)
#admin.site.register(models.DefenseTime)
admin.site.register(models.Major)
admin.site.register(models.Student)
admin.site.register(models.ReservationRequest)
admin.site.register(models.DefenseSession)
admin.site.register(models.Professor)
admin.site.site_header = 'پنل مدیریت سامانه‌ی برنامه‌ریزی اتاق دفاع'
admin.site.site_title = 'پنل مدیریت سامانه‌ی برنامه‌ریزی اتاق دفاع'
admin.site.index_title = 'داشبورد مدیریت'
