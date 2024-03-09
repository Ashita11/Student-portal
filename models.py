from email.policy import default
from django.db import models
class user(models.Model):
    uroll = models.IntegerField(default=0)
    uname = models.CharField(max_length=100,default=0)
    uemail = models.EmailField(primary_key=True,default=0)
    upass = models.CharField(max_length=30,default=0)
    umob =models.DecimalField(default=0,decimal_places=0,max_digits=10)
    ubranch = models.CharField(max_length=30,default=0)
    um =models.IntegerField(default=0)
    uelec =models.IntegerField(default=0)
    uelex =models.IntegerField(default=0)
    uchem =models.IntegerField(default=0)
    uphy =models.IntegerField(default=0)
    um2 =models.IntegerField(default=0)
    uelec2 =models.IntegerField(default=0)
    uelex2 =models.IntegerField(default=0)
    uchem2 =models.IntegerField(default=0)
    uphy2 =models.IntegerField(default=0)
    upaid=models.IntegerField(default=0)
    ufine=models.IntegerField(default=0)
    upending=models.IntegerField(default=0)
    jm=models.JSONField(default='dict')
    jp=models.JSONField(default='dict')
    jc=models.JSONField(default='dict')
    jel=models.JSONField(default='dict')
    jex=models.JSONField(default='dict')


class teacherr(models.Model):
    temail=models.EmailField(primary_key=True,default=0)
    tpass=models.CharField(max_length=30,default=0)