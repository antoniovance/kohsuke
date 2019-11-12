# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.views import generic
from stuff.models import Stuff as StuffModel
from web.serializer import StuffDetailSerializer


class StuffMoreListView(generic.ListView):
    template_name = "stuff/more.html"
    model = StuffModel

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        data = StuffDetailSerializer(instance=self.get_queryset(), many=True).data

        context = self.get_context_data(**kwargs)
        context['stuff'] = data
        context['the_title'] = '我的旧物.'
        context['products'] = data
        return render(request=request, template_name=self.template_name, context=context)