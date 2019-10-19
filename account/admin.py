from django.contrib import admin

from account.models import Account
from account.models import Gender
from account.models import Country, City, Province


class AccountAdmin(admin.ModelAdmin):
    fields = [
        'user_name',
        'password',
        'email',
        'phone',
        'head_image',
        'gender',
        'city',
        'province',
        'country'
    ]
    list_display = ('user_name',)


admin.site.register(Account, AccountAdmin)


class GenderAdmin(admin.ModelAdmin):
    fields = [
        'name',
    ]
    list_display = ('name',)


admin.site.register(Gender, GenderAdmin)


class CountryAdmin(admin.ModelAdmin):
    fields = [
        'name',
    ]
    list_display = ('name',)


admin.site.register(Country, CountryAdmin)


class ProvinceAdmin(admin.ModelAdmin):
    fields = [
        'name',
    ]
    list_display = ('name',)


admin.site.register(Province, ProvinceAdmin)


class CityAdmin(admin.ModelAdmin):
    fields = [
        'name',
    ]
    list_display = ('name',)


admin.site.register(City, CityAdmin)