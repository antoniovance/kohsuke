# -*- coding:utf-8 -*-
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from stuff.models import Stuff

# Create your views here.


class StuffMoreApiView(RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        stuff_type = kwargs.get('type')
        return Response({})