# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from userProfile.models import UserProfile
from django.contrib.auth.models import User
from userProfile.serializer import UserProfileSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing users.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]