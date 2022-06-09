# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Products(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=2)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Products'


class Purchases(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Purchases'


class Users(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    username = models.TextField(db_column='Username', blank=True, null=True)  # Field name made lowercase.
    password = models.DecimalField(db_column='Password', max_digits=18, decimal_places=2)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    createdtime = models.DateTimeField(db_column='CreatedTime')  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class Efmigrationshistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__EFMigrationsHistory'
