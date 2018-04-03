from django.db import models

# Create your models here.
class DefensePlace(models.Model):
   PlaceName=models.CharField(max_length=50)
   RoomName=models.CharField(max_length=50)
   BuildingName=models.CharField(max_length=50)

   def __unicode__(self):
       return "{}-{}-{}".format(self.PlaceName,self.BuildingName,self.RoomName)
