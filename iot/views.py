# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login

from django.views.generic import View

from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.http import HttpResponse

from .forms import UserForm
# Create your views here.
def index(request):
     return HttpResponse("Hello. It is a test")
     
class UserFormView(View):
    form_class = UserForm
    template_name = 'signup.html'

    def get(self,request):
        form = self.form_class(None)
        return render (request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        
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
                    return redirect('index')

        
        return render (request,self.template_name,{'form':form})
