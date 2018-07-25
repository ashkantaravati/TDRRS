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