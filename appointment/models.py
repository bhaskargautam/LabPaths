# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel
from model_utils import Choices
from lab.models import Lab, ClinicalTest
from userProfile.models import UserProfile

class Appointment(TimeStampedModel):
    lab = models.ForeignKey(Lab, related_name='appointments', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, related_name='appointments', on_delete=models.CASCADE)
    time = models.DateTimeField()
    LOCATION = Choices('Lab', 'Home')
    location = models.CharField(choices=LOCATION, max_length=10, null=True, blank=True)

    def __str__(self):
        return self.user.user.get_full_name() +  " : " + str(self.time)


class AppointmentTestMapping(TimeStampedModel):
    appointment_id = models.ForeignKey(Appointment, related_name='tests', on_delete=models.CASCADE)
    clinical_test_id = models.ForeignKey(ClinicalTest, related_name='appointments', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.appointment_id) + " : " + str(self.clinical_test_id)