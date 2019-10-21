# -*- coding:utf-8 -*-
from rest_framework import serializers


class AccountSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    head_image = serializers.CharField()
    email = serializers.CharField()
    phone = serializers.CharField()