from django.db import models

# Create your models here.

class AccountBase(models.Model):
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Gender(AccountBase):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = "gender"


class Country(AccountBase):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = "country"


class Province(AccountBase):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = "province"


class City(AccountBase):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = "city"


class Account(AccountBase):

    id = models.IntegerField(primary_key=True, auto_created=True)
    user_name = models.CharField(max_length=256, null=True)
    password = models.CharField(max_length=256, null=False)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=128)
    head_image = models.CharField(max_length=128)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        db_table = "account"