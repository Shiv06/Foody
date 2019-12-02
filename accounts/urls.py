from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns=[
path('login/',views.CustomLogin.as_view(),name="login"),
path('registration/',views.Registration.as_view(),name="register"),
]
