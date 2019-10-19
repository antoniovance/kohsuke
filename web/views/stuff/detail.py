# -*- coding:utf-8 -*-
from django.shortcuts import HttpResponse
from django.views import generic


class StuffDetailPage(generic.DetailView):

    def get(self, request, *args, **kwargs):
        pass