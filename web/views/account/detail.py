# -*- coding:utf-8 -*-
from django.views import generic
from django.shortcuts import render
from account.models import Account as AccountModel
from web.serializer.account import AccountSerializer



class AccountDetailView(generic.DetailView):
    template_name = 'account/detail.html'
    model = AccountModel

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = AccountSerializer(instance=self.object).data
        context = self.get_context_data(**kwargs)
        context['account'] = data
        context['the_title'] = '旧物.'
        return render(request=request, template_name=self.template_name, context=context)