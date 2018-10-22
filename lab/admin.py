# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from lab.models import *

class LabAdmin(admin.ModelAdmin):
    pass

class ClinicalTestAdmin(admin.ModelAdmin):
    pass

class LabScheduleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Lab, LabAdmin)
admin.site.register(ClinicalTest, ClinicalTestAdmin)
admin.site.register(LabSchedule, LabScheduleAdmin)