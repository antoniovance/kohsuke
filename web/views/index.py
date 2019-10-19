# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views import generic


class Index(generic.TemplateView):
    template_name = "index/index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['the_title'] = '我的旧物.'
        context['columns'] = range(13)
        context['columns1'] = range(14)
        return render(request, template_name=self.template_name, context=context)