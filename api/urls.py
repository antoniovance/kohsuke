# -*- coding:utf-8 -*-

from django.urls import path
from .views import StuffMoreApiView

urlpatterns = [
    path('stuff/more/<int:type>', StuffMoreApiView.as_view(), name="stuff_more")
]