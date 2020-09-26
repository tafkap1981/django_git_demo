"""
file: views.py
date: 2020-09-26 23:11
author: Joshua Xue
desc:
"""
from django.http import HttpResponse


def index_view(request):
    return HttpResponse('Hello git!')
