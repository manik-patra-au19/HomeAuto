from email.policy import default
from random import choice
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Device(models.Model):
    deviceID    = models.CharField(max_length=10,primary_key=True)
    devicetype  = models.CharField(max_length=20)
    lightStatus = models.ImageField(choices=((0,0),(1,1)),default=0)
    fanstatus   = models.ImageField(choices=((0,0),(1,1)),default=0)

    def __str__(self):
        return self.deviceID

class UserDevice(models.Model):
    User   = models.ForeignKey(User,on_delete=models.CASCADE)
    Device = models.ForeignKey(Device,on_delete=models.CASCADE)

    def __str__(self):
       return self.user.usename + ''+self.device.deviceId