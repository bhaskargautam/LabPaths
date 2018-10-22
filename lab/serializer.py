# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from lab.models import ClinicalTest, Lab, LabSchedule
from django.contrib.auth.models import User


class ClinicalTestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClinicalTest
        fields = ('name', 'description', 'method', 'price', 'prerequisite', 'estimate_hours', 'url')

class LabScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LabSchedule
        fields = ('opening_time', 'break_start', 'break_end', 'closing_time', 'url')

class LabSerializer(serializers.HyperlinkedModelSerializer):
    tests = ClinicalTestSerializer(many=True)
    schedules = LabScheduleSerializer(many=True)

    class Meta:
        model = Lab
        fields = ('full_name', 'address', 'latitude', 'longitude', 'phone', 'email', 'tests', 'schedules', 'url')

class LabOnlySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Lab
        fields = ('full_name', 'address', 'latitude', 'longitude', 'phone', 'email', 'url')