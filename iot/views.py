# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login

from django.views.generic import View

from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.http import HttpResponse

from .forms import UserForm

from django.contrib.auth import logout

from .models import comment
# Create your views here.

def logout_view(request):
    logout(request)
    return redirect('/')

def index(request):
    return HttpResponse("Hello. It is a test")
     
class UserFormView(View):
    form_class = UserForm
    template_name = 'signup.html'

    def get(self,request):
        form = self.form_class(None)
        return render (request,self.template_name,{'form':form})

    def post(self,request):

        #login part
        if request.POST.get("username1"):
            username =  request.POST.get("username1")
            password =  request.POST.get("password1")
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/')
        
        #signup part

        form = self.form_class(request.POST)

        if request.POST.get("username"):
            if form.is_valid():
                user = form.save(commit=False)
                username =  form.cleaned_data['username']
                password =  form.cleaned_data['password']
                user.set_password(password)
                user.save()


                user = authenticate(username=username,password=password)

                if user is not None:
                    if user.is_active:
                        login(request,user)
                        return redirect('/')

        return render (request,self.template_name,{'form':form})


class about(View):
    template_name = 'about.html'

    def get(self,request):
        return render (request,self.template_name)

    def post(self,request):
        text =  request.POST.get("comments")
        name =  request.POST.get("name")
        email = request.POST.get("email")
        newComment = comment(text=text,name=name,email=email)
        newComment.save()
        return redirect('/')
