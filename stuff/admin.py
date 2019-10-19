from django.contrib import admin
from stuff.models import Stuff, Brand


class StuffAdmin(admin.ModelAdmin):
    fields = [
        'type',
        'name',
        'brand',
        'owner',
        'is_online',
        'is_delete',
        'acquire_price',
        'stock',
        'intro'
    ]
    list_display = ('name', 'type')


admin.site.register(Stuff, StuffAdmin)


class BrandAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name',)


admin.site.register(Brand, BrandAdmin)
