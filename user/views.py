from django.shortcuts import render
from django.template.loader import get_template
import hashlib #导入哈希库
from user.models import Register
from django.template import RequestContext
from django.http import HttpResponse
from datetime import datetime


# Create your views here.

# 加密
def take_md5(content):
    hash = hashlib.md5() #创建hash加密实例
    hash.update(content.encode("utf-8"))  #hash加密
    result = hash.hexdigest() #获取加密结果
    return result
#注册
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        #判断输入是否为空
        if username and password1 and password2:
            usernamefilter = Register.objects.filter(username=username)
            #判断账号是否存在
            if len(usernamefilter) > 0:
                return render(request,'register.html',{'massage':"账号已存在！"})
            else:
                #判断输入的密码是否相等
                if password1 != password2:
                    return render(request,'register.html',{'massage':"马马虎虎！密码不一样！"})
                else:
                    #加密
                    password = take_md5(password1)
                    time = datetime.now()
                    #写入数据表
                    Register.objects.create(username = username,password = password,register_time = time)
                    return render(request,'success.html',{'massage':"注册成功"})
        else:
            return render(request,'register.html',{'massage':'你是坏人！丢三落四！填完！'})
    return render(request,'register.html')

#登录
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password = take_md5(password)
        namefilter = Register.objects.filter(username = username, password = password)
        if len(namefilter) > 0:
            return render(request,'success.html',{'massage':"登录成功"})
        else:
            return render(request,'success.html',{'massage':"账号或密码错误"})  
    return render(request,'login.html')
