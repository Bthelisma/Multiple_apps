# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def register(request):
    return HttpResponse("placeholder to later display all the list of users")

def login(request):
    return HttpResponse("placeholder to display a form to create a user")

def show(request, user_id):
    return HttpResponse("placeholder to display user {}".format(user_id))

def edit(request, user_id):
    return HttpResponse("placeholder to edit user {}".format(user_id))

def delete(request, user_id):
    return redirect('/users')
