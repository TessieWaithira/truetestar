# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Profile
from .models import Project


from django.contrib import admin

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
