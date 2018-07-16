from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
# CHOICES
SEMESTER_CHOICES=[(1,u'پاییز') , (2,u'بهار') , (3,u'تابستان')]
DEGREE_CHOICES=[(1,u'کارشناسی ارشد') , (2,u'دکتری')]
DEFENSE_TIME_STATUS_CHOICES=[(0,u'اختصاص داده شده') , (1,u'آزاد')]
# Weekday 
PERSIAN_WEEKDAY={'0':u'شنبه','1':u'یکشبنه','2':u'دوشنبه','3':u'سه‌شنبه','4':u'چهارشنبه','5':u'پنجشنبه','6':u'جمعه'}

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
    occurrence_date=jmodels.jDateField(verbose_name='تاریخ')
    start_time=models.TimeField(verbose_name='زمان شروع')
    end_time=models.TimeField(verbose_name='زمان پایان')
    status=models.IntegerField(choices=DEFENSE_TIME_STATUS_CHOICES,verbose_name='وضعیت')
    defense_place=models.ForeignKey('DefensePlace',verbose_name='محل دفاع')
    class Meta:
        verbose_name=u'زمان دفاع'
        verbose_name_plural=u'زمان‌های دفاع'    
    def get_duration(self):
        return self.end_time-self.start_time    
    @property
    def weekday(self):
        return PERSIAN_WEEKDAY[str(self.occurrence_date.weekday())]
    def __str__(self):
        return u"روز{} از {} تا{}".format(str(self.occurrence_date),self.start_time,self.end_time)

class Student(models.Model):
    student_number=models.CharField(max_length=12,verbose_name='شماره دانشجویی')
    major=models.ForeignKey('Major',verbose_name='رشته‌ی تحصیلی')
    degree=models.IntegerField(choices=DEGREE_CHOICES,verbose_name='مقطع تحصیلی')
    father_name=models.CharField(verbose_name='نام پدر',max_length=10)
    national_id=models.CharField(verbose_name='شماره ملی',max_length=10)
    #...
    user_account=models.OneToOneField(User,verbose_name='حساب کاربری', related_name='student')
    class Meta:
        verbose_name=u'دانشجو'
        verbose_name_plural=u'دانشجویان'  
    def get_info_from_user(self):
        return u"{} {}".format(self.user_account.first_name,self.user_account.last_name)
    def __str__(self):
        return u"{} دانشجوی {} رشته‌ی {}".format(self.get_info_from_user(),self.get_degree_display(),self.major)

class ReservationRequest(models.Model):
    requested_defense_time=models.ForeignKey('DefenseTime',verbose_name='زمان درخواستی')
    request_date_time=jmodels.jDateTimeField(verbose_name='زمان ثبت درخواست')
    requesting_student=models.ForeignKey('Student',verbose_name='دانشجوی درخواست‌کننده')
    class Meta:
        verbose_name=u'درخواست رزرو'
        verbose_name_plural=u'درخواست‌های رزرو' 
    #def __str__(self):


class Major(models.Model):
    major_name=models.CharField(max_length=100,verbose_name='نام رشته')
    class Meta:
        verbose_name=u'رشته‌ی تحصیلی'
        verbose_name_plural=u'رشته‌‌های تحصیلی'
    def __str__(self):
        return self.major_name