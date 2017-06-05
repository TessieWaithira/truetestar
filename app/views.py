# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Test


# Create your views here.
def create_test(request):
    tests = Test.objects.all()
    return render(request, 'create_test.html', {'tests': tests})


