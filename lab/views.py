# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from lab.models import ClinicalTest, Lab, LabSchedule
from lab.serializer import ClinicalTestSerializer, LabSerializer, LabScheduleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class LabViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing lab.
    """
    queryset = Lab.objects.all()
    serializer_class = LabSerializer
    permission_classes = [IsAuthenticated]

class LabScheduleViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing lab schedulw.
    """
    queryset = LabSchedule.objects.all()
    serializer_class = LabScheduleSerializer
    permission_classes = [IsAuthenticated]

class ClinicalTestViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing clinical tests.
    """
    queryset = ClinicalTest.objects.all()
    serializer_class = ClinicalTestSerializer
    permission_classes = [IsAuthenticated]