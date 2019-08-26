# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DbItemByStore(models.Model):
    store = models.TextField(db_column='Store')  # Field name made lowercase.
    item_number = models.TextField(db_column='Item_Number')  # Field name made lowercase.
    new_order_point = models.FloatField(db_column='New_Order_Point', blank=True, null=True)  # Field name made lowercase.
    qoh = models.FloatField(db_column='QOH', blank=True, null=True)  # Field name made lowercase.
    retail_price = models.FloatField(db_column='Retail_Price', blank=True, null=True)  # Field name made lowercase.
    average_cost = models.FloatField(db_column='Average_Cost', blank=True, null=True)  # Field name made lowercase.
    replacement_cost = models.FloatField(db_column='Replacement_Cost', blank=True, null=True)  # Field name made lowercase.
    inv_value = models.FloatField(db_column='Inv_Value', blank=True, null=True)  # Field name made lowercase.
    new_inv_value = models.FloatField(db_column='New_Inv_Value', blank=True, null=True)  # Field name made lowercase.
    forecast_demand_per_day = models.FloatField(db_column='Forecast_Demand_Per_Day', blank=True, null=True)  # Field name made lowercase.
    storenumber = models.TextField(db_column='StoreNumber')  # Field name made lowercase.
    storeshortname = models.TextField(db_column='StoreShortName', blank=True, null=True)  # Field name made lowercase.
    classcode = models.TextField(db_column='ClassCode', blank=True, null=True)  # Field name made lowercase.
    classname = models.TextField(db_column='ClassName', blank=True, null=True)  # Field name made lowercase.
    finelinecode = models.TextField(db_column='FinelineCode', blank=True, null=True)  # Field name made lowercase.
    finelinename = models.TextField(db_column='FinelineName', blank=True, null=True)  # Field name made lowercase.
    itemdescription = models.TextField(db_column='ItemDescription')  # Field name made lowercase.
    netsales2014 = models.FloatField(db_column='NetSales2014', blank=True, null=True)  # Field name made lowercase.
    netsales2015 = models.FloatField(db_column='NetSales2015', blank=True, null=True)  # Field name made lowercase.
    netsales2016 = models.FloatField(db_column='NetSales2016', blank=True, null=True)  # Field name made lowercase.
    netsales2017 = models.FloatField(db_column='NetSales2017', blank=True, null=True)  # Field name made lowercase.
    netsales2018 = models.FloatField(db_column='NetSales2018', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'db_item_by_store'


class DbSalesDetailCustomerType(models.Model):
    storenumber = models.CharField(db_column='StoreNumber', max_length=8)  # Field name made lowercase.
    storeshortname = models.TextField(db_column='StoreShortName', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', blank=True, null=True, max_length=16)  # Field name made lowercase.
    sales = models.FloatField(db_column='Sales', blank=True, null=True)  # Field name made lowercase.
    salesdetail = models.FloatField(db_column='SalesDetail', blank=True, null=True)  # Field name made lowercase.
    accountcode = models.FloatField(db_column='AccountCode', blank=True, null=True)  # Field name made lowercase.
    itemnumber = models.CharField(db_column='ItemNumber', blank=True, null=True, max_length=32)  # Field name made lowercase.
    itemdescription = models.TextField(db_column='ItemDescription', blank=True, null=True)  # Field name made lowercase.
    measure = models.TextField(db_column='Measure', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'db_SALES_DETAIL_CUSTOMER_TYPE'
