# -*- coding:utf-8 -*-

from django.views import generic
from stuff.models import Stuff as StuffModel


class StuffMoreList(generic.ListView):

    def get(self, request, *args, **kwargs):
        pass