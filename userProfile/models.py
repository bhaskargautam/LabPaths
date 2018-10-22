# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User

class UserProfile(TimeStampedModel):
    user = models.ForeignKey(User, related_name='profiles', on_delete=models.CASCADE)
    address = models.CharField(max_length=1000, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()