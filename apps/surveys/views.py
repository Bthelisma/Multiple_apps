# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse("placeholder to later display all the list of surveys")

def new(request):
    return HttpResponse("placeholder to display a form to create a new survey")
