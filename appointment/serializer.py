# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from appointment.models import Appointment, AppointmentTestMapping
from lab.serializer import ClinicalTestSerializer, LabOnlySerializer
from userProfile.serializer import UserProfileWithUserSerializer
from django.contrib.auth.models import User

class AppointmentTestMappingSerializer(serializers.HyperlinkedModelSerializer):
    clinical_test_id = ClinicalTestSerializer()

    class Meta:
        model = AppointmentTestMapping
        fields = ('clinical_test_id', 'url')

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    lab = LabOnlySerializer()
    user = UserProfileWithUserSerializer()
    tests = AppointmentTestMappingSerializer(many=True)

    class Meta:
        model = Appointment
        fields = ('lab', 'location', 'time', 'url', 'user', 'lab' ,'tests')