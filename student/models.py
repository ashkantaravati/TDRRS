from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
import jdatetime
# CHOICES
SEMESTER_CHOICES=[(1,u'پاییز') , (2,u'بهار') , (3,u'تابستان')]
DEGREE_CHOICES=[(1,u'کارشناسی ارشد') , (2,u'دکتری')]
DEFENSE_TIME_STATUS_CHOICES=[(0,u'اختصاص داده شده') , (1,u'آزاد')]
RESERVATION_REQUEST_STATUS_CHOICES=[(0,u'ثبت شد') , (1,u'لغو از طرف دانشجو'),(2,u'لغو از طرف دانشگاه')]
PROFESSOR_RANK_STATUS_CHOICES=[(1,u'مربی') , (2,u'استادیار'),(3,u'دانشیار'),(4,u'استاد تمام')]
# Weekday 
PERSIAN_WEEKDAY={'0':u'شنبه','1':u'یکشبنه','2':u'دوشنبه','3':u'سه‌شنبه','4':u'چهارشنبه','5':u'پنجشنبه','6':u'جمعه'}
GENDER_CHOICES=[(0,u'سرکار خانم'),(1,u'جناب آقای')]
PROF_TITLE_CHOICES=[(0,u'مهندس'),(1,u'دکتر'),(3,u'پروفسور')]
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
        ordering = ['occurrence_date', 'start_time', 'defense_place']
    def get_duration(self):
        return self.end_time-self.start_time    
    @property
    def weekday(self):
        return PERSIAN_WEEKDAY[str(self.occurrence_date.weekday())]
    def __str__(self):
        return u"روز{} از {} تا {}".format(str(self.occurrence_date),format_time(self.start_time),format_time(self.end_time))


class Student(models.Model):
    first_name=models.CharField(verbose_name='نام',max_length=30)
    last_name=models.CharField(verbose_name='نام خانوادگی',max_length=30)
    student_number=models.CharField(max_length=12,verbose_name='شماره دانشجویی')
    major=models.ForeignKey('Major',verbose_name='رشته‌ی تحصیلی')
    degree=models.IntegerField(choices=DEGREE_CHOICES,verbose_name='مقطع تحصیلی')
    father_name=models.CharField(verbose_name='نام پدر',max_length=30)
    gender=models.IntegerField(choices=GENDER_CHOICES,verbose_name='جنسیت')
    national_id=models.CharField(verbose_name='شماره ملی',max_length=10)
    has_active_request=models.BooleanField(default=False,verbose_name='درخواست فعال دارد')
    #...
    user_account=models.OneToOneField(User,verbose_name='حساب کاربری', related_name='student')
    class Meta:
        verbose_name=u'دانشجو'
        verbose_name_plural=u'دانشجویان'  
    def get_info_from_user(self):
        return u"{} {}".format(self.user_account.first_name,self.user_account.last_name)
    @property
    def info_from_self(self):
        return u"{} {}".format(self.first_name,self.last_name)
    @property
    def full_name(self):
        return u"{} {} {}".format(self.get_gender_display(),self.first_name,self.last_name)
    def __str__(self):
            return u"{} دانشجوی {} رشته‌ی {}".format(self.full_name,self.get_degree_display(),self.major)



class ReservationRequest(models.Model):
    requested_defense_time=models.ForeignKey('DefenseTime',verbose_name='زمان درخواستی')
    request_date_time=jmodels.jDateTimeField(verbose_name='زمان ثبت درخواست')
    requesting_student=models.ForeignKey('Student',verbose_name='دانشجوی درخواست‌کننده')
    tracing_code=models.CharField(max_length=12,verbose_name='کد رهگیری')
    status=models.IntegerField(choices=RESERVATION_REQUEST_STATUS_CHOICES,verbose_name='وضعیت درخواست')
    class Meta:
        verbose_name=u'درخواست رزرو'
        verbose_name_plural=u'درخواست‌های رزرو' 
    def __str__(self):
        rep=u'{} توسط {} در تاریخ {}'
        return rep.format(self.requested_defense_time,self.requesting_student,format_datetime(self.request_date_time))
    @property
    def formatted_request_datetime(self):
        return format_datetime(self.request_date_time)
class Major(models.Model):
    major_name=models.CharField(max_length=100,verbose_name='نام رشته')
    class Meta:
        verbose_name=u'رشته‌ی تحصیلی'
        verbose_name_plural=u'رشته‌‌های تحصیلی'
    def __str__(self):
        return self.major_name

class Professor(models.Model):
    name=models.CharField(max_length=80,verbose_name='نام و نام خانوادگی')
    code=models.CharField(max_length=15,verbose_name='شناسه استاد')
    description=models.CharField(max_length=200,verbose_name='توضیحات',null=True,blank=True)
    gender=models.IntegerField(choices=GENDER_CHOICES,verbose_name='جنسیت')
    title=models.IntegerField(choices=PROF_TITLE_CHOICES,verbose_name='عنوان')
    is_visiting=models.BooleanField(verbose_name='استاد مدعو است')
    major=models.ForeignKey('Major',verbose_name='رشته‌ی تحصیلی')
    rank=models.IntegerField(choices=PROFESSOR_RANK_STATUS_CHOICES,verbose_name='مرتبه')
    class Meta:
        verbose_name=u'استاد'
        verbose_name_plural=u'اساتید' 
    def __str__(self):
        return u"{} {} {} {} ".format(self.get_gender_display(), self.get_title_display(),
        self.name,self.get_rank_display(),self.major)


class DefenseSession(models.Model):
    subject=models.CharField(max_length=500,verbose_name='موضوع')
    supervisor=models.ForeignKey('Professor',verbose_name='استاد راهنما',null=True, related_name='supervisor')
    advisor=models.ForeignKey('Professor',verbose_name='استاد مشاور',null=True,blank=True, related_name='advisor')
    examiner=models.ForeignKey('Professor',verbose_name='استاد داور',null=True, related_name='examiner')
    dean=models.ForeignKey('Professor',verbose_name='مدیر گروه',null=True, related_name='dean')
    student=models.ForeignKey('Student',verbose_name='دانشجو')
    semester=models.ForeignKey('Semester',verbose_name='نیمسال')
    approval_date=jmodels.jDateField(verbose_name='تاریخ تصویب')
    is_archived=models.BooleanField(verbose_name='بایگانی شده است؟')
    designated_defense_time=models.OneToOneField('DefenseTime', null=True,verbose_name='تاریخ و زمان اختصاص یافته برای دفاع')
    class Meta:
        verbose_name=u'جلسه دفاع مصوب شورا'
        verbose_name_plural=u'جلسات دفاع مصوب شورا' 
        ordering = ['designated_defense_time']
    def __str__(self):
        return u"{} توسط {} مصوب {}".format(self.subject,self.student,str(self.approval_date))
    @property
    def info(self):
        txt='دانشجو: {}،استاد راهنما: {}،استاد مشاور: {}،استاد داور: {}'
        advisor_name=self.advisor.name if self.advisor!=None else 'ندارد'
        processed_txt=txt.format(self.student.info_from_self,self.supervisor.name,advisor_name,self.examiner.name)
        return processed_txt
    @property
    def major(self):
        return self.student.major
    @property
    def is_scheduled(self):
        return True if not self.designated_defense_time== None else False

# Helpers and such...
def format_datetime(datetime_obj):
    return datetime_obj.strftime("%Y-%m-%d %H:%M")
def format_time(time_obj):
    return time_obj .strftime("%H:%M")
    
def jdatetime_fromgregorian(greg_datetime):
    j_date=jdatetime.date.fromgregorian(date=greg_datetime)
    jalali_datetime=jdatetime.datetime(j_date.year,j_date.month,j_date.day,greg_datetime.hour,greg_datetime.minute)
    return jalali_datetime
@property
def jalali_last_login(self):
    greg_last_login=self.last_login
    j_last_login=jdatetime_fromgregorian(greg_last_login)

    return format_datetime(j_last_login)
auth.models.User.add_to_class('jalali_last_login', jalali_last_login)