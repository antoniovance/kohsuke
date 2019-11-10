# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views import generic
from stuff.models import Stuff as StuffModel
from web.serializer import StuffDetailSerializer


class StuffDetailView(generic.DetailView):
    template_name = 'stuff/detail.html'
    model = StuffModel

    def get(self, request, *args, **kwargs):
        self.object= self.get_object()
        data = StuffDetailSerializer(instance=self.object).data
        context = self.get_context_data(**kwargs)
        context['stuff'] = data
        context['the_title'] = '我的旧物.'
        return render(request=request, template_name=self.template_name, context=context)