# -*- coding:utf-8 -*-

from rest_framework import serializers


class StuffDetailSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    image = serializers.CharField()
    acquire_price = serializers.CharField()
    brand = serializers.SerializerMethodField()
    intro = serializers.CharField()
    owner_name = serializers.SerializerMethodField()
    owner_image = serializers.SerializerMethodField()

    def get_brand(self, obj):
        return obj.brand.name

    def get_owner_name(self, obj):
        return obj.owner.user_name

    def get_owner_image(self, obj):
        return obj.owner.head_image


class StuffListSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    image = serializers.CharField()
    acquire_price = serializers.CharField()
    brand = serializers.SerializerMethodField()

    def get_brand(self, obj):
        return obj.brand.name