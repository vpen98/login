from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length = 32, verbose_name = '账号',null=False,blank=False)
    password = models.CharField(max_length = 300, verbose_name = '密码',null=False,blank=False)
    register_time = models.DateTimeField(verbose_name = '注册时间')