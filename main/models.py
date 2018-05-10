from django.db import models
from django.contrib.auth.models import User
#CHOICES
SEMESTER_CHOICES=[(1,u'پاییز'),(2,u'بهار'),(3,u'تابستان')]

# Create your models here.
#نیمسال تحصیلی
class Semester(models.Model):
    beginning_year=models.IntegerField(verbose_name='سال شروع')
    ending_year=models.IntegerField(verbose_name='سال پایان')
    semester_type=models.IntegerField(choices=SEMESTER_CHOICES,verbose_name='نوع نیمسال')
    class Meta:
        verbose_name=u'نیمسال تحصیلی'
        verbose_name_plural=u'نیمسال‌های تحصیلی'        
    def __str__(self):
        return u"{} {}-{}".format(self.get_semester_type_display(),self.beginning_year,self.ending_year)
#مکان دفاع
class DefensePlace(models.Model):
    place_name=models.CharField(max_length=50,verbose_name='نام مستعار اتاق دفاع')
    room_name=models.CharField(max_length=50,verbose_name='نام یا شماره اتاق')
    building_name=models.CharField(max_length=50,verbose_name='نام ساختمان')
    semester=models.ForeignKey('Semester',verbose_name='نیمسال تحصیلی')
    class Meta:
        verbose_name=u'محل دفاع'
        verbose_name_plural=u'محل‌های دفاع'
    def __str__(self):
        return "{}-{}-{}".format(self.place_name,self.building_name,self.room_name)
#زمان دفاع
class DefenseTime(models.Model):
    occurrence_date=models.DateField(verbose_name='تاریخ')
    start_time=models.TimeField(verbose_name='زمان شروع')
    end_time=models.TimeField(verbose_name='زمان پایان')
    #dayOfWeek?
    defensePlace=models.ForeignKey('DefensePlace',verbose_name='محل دفاع')
    class Meta:
        verbose_name=u'زمان دفاع'
        verbose_name_plural=u'زمان‌های دفاع'    
    def get_duration(self):
        return self.end_time-self.start_time    
    def __str__(self):
        return u"روز{} از {} تا{}".format(self.occurrence_date,self.start_time,self.end_time)

class Student(models.Model):
    student_number=models.CharField(max_length=12,verbose_name='شماره دانشجویی')


    user_account=models.OneToOneField(User)

class ReservationRequest(models.Model):
