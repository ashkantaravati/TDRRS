from django.db import models
#CHOICES
SEMESTER_CHOICES=[(1,u'پاییز'),(2,u'بهار'),(3,u'تابستان')]






# Create your models here.
#مکان دفاع
class DefensePlace(models.Model):
    placeName=models.CharField(max_length=50,verbose_name='نام مستعار اتاق دفاع')
    roomName=models.CharField(max_length=50,verbose_name='نام یا شماره اتاق')
    buildingName=models.CharField(max_length=50,verbose_name='نام ساختمان')
    semester=models.ForeignKey('Semester',verbose_name='نیمسال تحصیلی')
    class Meta:
        verbose_name=u'محل دفاع'
        verbose_name_plural=u'محل‌های دفاع'
    def __str__(self):
        return "{}-{}-{}".format(self.placeName,self.buildingName,self.roomName)
#نیمسال تحصیلی
class Semester(models.Model):
    beginningYear=models.IntegerField(verbose_name='سال شروع')
    endingYear=models.IntegerField(verbose_name='سال پایان')
    semesterType=models.IntegerField(choices=SEMESTER_CHOICES,verbose_name='نوع نیمسال')
    class Meta:
        verbose_name=u'نیمسال تحصیلی'
        verbose_name_plural=u'نیمسال‌های تحصیلی'        
    def __str__(self):
        return u"{} {}-{}".format(self.get_semesterType_display(),self.beginningYear,self.endingYear)
