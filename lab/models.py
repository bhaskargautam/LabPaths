# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel
from model_utils import Choices

class Lab(TimeStampedModel):
    full_name = models.CharField(max_length=70)
    address = models.CharField(max_length=1000, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return self.full_name


class ClinicalTest(TimeStampedModel):
    lab = models.ForeignKey(Lab, related_name='tests', on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=350, null=True, blank=True)
    METHOD = Choices('blood', 'urine', 'stool', 'sputum', 'physical')
    method = models.CharField(choices=METHOD, null=True, blank=True, max_length=10)
    price = models.FloatField(null=True, blank=True)
    prerequisite = models.CharField(max_length=350, null=True, blank=True)
    estimate_hours = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class LabSchedule(TimeStampedModel):
    lab = models.ForeignKey(Lab, related_name='schedules', on_delete=models.CASCADE)
    opening_time = models.DateTimeField()
    break_start = models.DateTimeField()
    break_end = models.DateTimeField()
    closing_time = models.DateTimeField()

    def __str__(self):
        return str(self.lab) + " : " + str(self.opening_time)