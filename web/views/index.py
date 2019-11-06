# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views import generic
from web.serializer import StuffListSerializer
from stuff.models import Stuff as StuffModel


class Index(generic.TemplateView):
    template_name = "index/index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['the_title'] = '我的旧物.'

        storage_query = StuffModel.objects.filter(type=1)
        datas = StuffListSerializer(instance=storage_query, many=True).data
        context['storages'] = datas

        exhibit_query = StuffModel.objects.filter(type=2)
        datas = StuffListSerializer(instance=exhibit_query, many=True).data
        context['exhibits'] = datas

        product_query = StuffModel.objects.filter(type=3)
        datas = StuffListSerializer(instance=product_query, many=True).data
        context['products'] = datas

        return render(request, template_name=self.template_name, context=context)