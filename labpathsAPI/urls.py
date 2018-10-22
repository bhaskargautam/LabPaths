"""labpathsAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from userProfile.views import UserViewSet, UserProfileViewSet
from lab.views import ClinicalTestViewSet, LabViewSet, LabScheduleViewSet
from appointment.views import AppointmentViewSet, AppointmentTestMappingViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'user-profile', UserProfileViewSet)
router.register(r'lab', LabViewSet)
router.register(r'clinical-test', ClinicalTestViewSet)
router.register(r'lab-schedule', LabScheduleViewSet)
router.register(r'appointment', AppointmentViewSet)
router.register(r'appointment-test', AppointmentTestMappingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
]
