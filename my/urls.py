from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('getfeedback/', getfeedback, name='getfeedback'),
    path('feedbackloginfunction/', feedbackloginfunction, name='feedbackloginfunction'),

    ]