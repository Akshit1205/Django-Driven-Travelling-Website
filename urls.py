# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:21:34 2020

@author: Akshit Kumar
"""
from django.urls import path
from . import views

urlpatterns=[
    path('' , views.index , name='index'),
   ]
