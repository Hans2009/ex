# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegistrationForm

# Create your views here.
def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])

            if user:
                login(request,user)
                return HttpResponse("Welcom you. You have been authenticated successfully")
            else:
                return HttpResponse("sorry, your username or password is not right")
        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request,"account/login.html", {"form":login_form})

def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponse("successfully")
        else:
            return HttpResponse("sorry, you can't register.")

    else:
        user_form = RegistrationForm()
        return render(request, "account/register.html", {"form": user_form})




def download_file(request):  
    # do something  
    the_file_name='11.png'             
    filename='media/uploads/11.png'    
    response=StreamingHttpResponse(readFile(filename))  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition']='attachment;filename="{0}"'.format(the_file_name)  
    return response  
  
def readFile(filename,chunk_size=512):  
    with open(filename,'rb') as f:  
        while True:  
            c=f.read(chunk_size)  
            if c:  
                yield c  
            else:  
                break  
