# -*- coding:utf-8 -*-
from rest_framework import serializers


class StuffMoreApiSerialiser(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    image = serializers.CharField()
    acquire_price = serializers.CharField()
    brand = serializers.SerializerMethodField()

    def get_brand(self, obj):
        return obj.brand.name