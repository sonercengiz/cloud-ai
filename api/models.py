
from django.db import models
from django.forms import IntegerField


class Products(models.Model):
    title = models.TextField()
    price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'Products'


class Users(models.Model):
    username = models.TextField()
    password = models.TextField()

    class Meta:
        managed = True
        db_table = 'Users'


class Purchases(models.Model):
    productid = models.IntegerField()
    userid = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'Purchases'