from django.contrib import admin
from stuff.models import Stuff, Brand, Category, StuffCategoryRelationship


class StuffAdmin(admin.ModelAdmin):
    fields = [
        'type',
        'name',
        'brand',
        'owner',
        'image',
        'is_online',
        'is_delete',
        'acquire_price',
        'stock',
        'intro'
    ]
    list_display = ('id', 'name', 'type')


admin.site.register(Stuff, StuffAdmin)


class BrandAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id', 'name')


admin.site.register(Brand, BrandAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'stuffs']
    list_display = ('id', 'name')


admin.site.register(Category, CategoryAdmin)


class StuffCategoryRelationshipAdmin(admin.ModelAdmin):
    fields = []
    list_display = ('id', 'stuff', 'category')


admin.site.register(StuffCategoryRelationship, StuffCategoryRelationshipAdmin)