# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from userProfile.models import UserProfile
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('address', 'latitude', 'longitude', 'phone', 'url')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profiles = UserProfileSerializer(many=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_staff', 'url', 'profiles')

class UserOnlySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_staff', 'url')

class UserProfileWithUserSerializer(serializers.HyperlinkedModelSerializer):
    user = UserOnlySerializer()

    class Meta:
        model = UserProfile
        fields = ('user', 'address', 'latitude', 'longitude', 'phone', 'url')
