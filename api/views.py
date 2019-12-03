# -*- coding:utf-8 -*-
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from stuff.models import Stuff
from .serializer import StuffMoreApiSerializer

# Create your views here.


class StuffMoreApiView(RetrieveAPIView):
    queryset = Stuff.objects.all()

    def get(self, request, *args, **kwargs):
        stuff_type = kwargs.get('type')
        limit = kwargs.get('limit', 10)
        pageNo = kwargs.get('pageNo', 1)
        stuff_objs = self.queryset.filter(type=stuff_type)[(pageNo-1)*limit: pageNo*limit]
        data = StuffMoreApiSerializer(instance=stuff_objs, many=True).data
        return Response({'data': data})