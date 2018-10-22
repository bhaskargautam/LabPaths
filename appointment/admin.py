# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from appointment.models import *

class AppointmentAdmin(admin.ModelAdmin):
    pass

class AppointmentTestMappingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(AppointmentTestMapping, AppointmentTestMappingAdmin)