from django.db import models
from account.models import Account

# Create your models here.


class Brand(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=256)
    image = models.CharField(max_length=512, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "brand"


class Stuff(models.Model):

    type_storage = 1
    type_exhibit = 2
    type_product = 3

    STUFF_TYPE = (
        (type_storage, "我的存货"),
        (type_exhibit, "我的展品"),
        (type_product, "我的货品")
    )

    id = models.IntegerField(primary_key=True, auto_created=True)
    type = models.IntegerField(choices=STUFF_TYPE, default=0)
    name = models.CharField(max_length=512, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=True, help_text="物品是否上线")
    is_delete = models.BooleanField(default=False, help_text="物品是否删除")
    acquire_price = models.IntegerField(default=0, help_text="获得的价格")
    acquire_time = models.DateTimeField(default='1900-01-01 00:00:00', help_text="物品获得时间")
    stock = models.IntegerField(default=0)
    image = models.CharField(max_length=512)  # 图片可以衍生为照片栏
    intro = models.TextField(default='', help_text='更多介绍')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "stuff"


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=512)
    Stuffs = models.ManyToManyField(
        Stuff,
        through="StuffCategoryRelationship"
    )
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "category"


class StuffCategoryRelationship(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "stuff_category_relationship"

