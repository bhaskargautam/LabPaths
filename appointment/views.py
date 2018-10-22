# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from appointment.models import Appointment, AppointmentTestMapping
from appointment.serializer import AppointmentSerializer, AppointmentTestMappingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class AppointmentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing appointment.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

class AppointmentTestMappingViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing tests related to appointment.
    """
    queryset = AppointmentTestMapping.objects.all()
    serializer_class = AppointmentTestMappingSerializer
    permission_classes = [IsAuthenticated]