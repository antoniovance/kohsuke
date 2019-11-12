from django.shortcuts import render
from rest_framework import views
from rest_framework.response import responses

# Create your views here.


class StuffMoreApiView(views.APIView):
    def get(self, request, **kwargs):
        stuff = {}

        return responses(stuff)