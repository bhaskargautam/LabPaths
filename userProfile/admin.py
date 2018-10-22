# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from userProfile.models import *

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)