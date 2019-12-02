from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from . import forms
from django.urls import reverse_lazy

# Create your views here.

class CustomLogin(LoginView):
    template_name="accounts/login.html"
    def post(self, request, *args, **kwargs):
        form_class=self.get_form_class()
        form=self.get_form(form_class)
        data=dict()
        if form.is_valid():
            data['form_flag']=True
        else:
            data['form_flag']=False

        context={'form':form}
        data['html_form']=render_to_string(template_name=self.template_name,context=context,request=request)

        return JsonResponse(data)


class Registration(CreateView):
    form_class=forms.Registration
    template_name='accounts/register.html'
    success_url=reverse_lazy('thankyou')

    def post(self, request, *args, **skwargs):
        form=self.get_form(self.form_class)
        data=dict()

        if form.is_valid():
            form.save()
            data['form_flag']=True

        else:
            data['form_flag']=False
        context={'form':form}
        data['html_form']=render_to_string(template_name=self.template_name,context=context,request=request)

        return JsonResponse(data)
