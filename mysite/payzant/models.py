# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblAllStoresHardlines(models.Model):
    plan = models.TextField(db_column='Plan', blank=True, null=True)  # Field name made lowercase.
    store = models.TextField(db_column='Store')  # Field name made lowercase.
    item_number = models.TextField(db_column='Item_Number')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    date_added = models.DateField(db_column='Date_Added', blank=True, null=True)  # Field name made lowercase.
    rop_protect = models.TextField(db_column='ROP_Protect', blank=True, null=True)  # Field name made lowercase.
    proxy_only = models.TextField(db_column='Proxy_Only', blank=True, null=True)  # Field name made lowercase.
    popularity = models.TextField(db_column='Popularity', blank=True, null=True)  # Field name made lowercase.
    location = models.TextField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    location_2 = models.TextField(db_column='Location_2', blank=True, null=True)  # Field name made lowercase.
    location_3 = models.TextField(db_column='Location_3', blank=True, null=True)  # Field name made lowercase.
    order_point = models.FloatField(db_column='Order_Point', blank=True, null=True)  # Field name made lowercase.
    order_point_a = models.FloatField(db_column='Order_Point_A', blank=True, null=True)  # Field name made lowercase.
    order_point_b = models.FloatField(db_column='Order_Point_B', blank=True, null=True)  # Field name made lowercase.
    order_point_c = models.FloatField(db_column='Order_Point_C', blank=True, null=True)  # Field name made lowercase.
    order_point_d = models.FloatField(db_column='Order_Point_D', blank=True, null=True)  # Field name made lowercase.
    min_order_point = models.FloatField(db_column='Min_Order_Point', blank=True, null=True)  # Field name made lowercase.
    imu_safety_stock = models.FloatField(db_column='IMU_Safety_Stock', blank=True, null=True)  # Field name made lowercase.
    rule_used = models.TextField(db_column='Rule_Used', blank=True, null=True)  # Field name made lowercase.
    new_order_point = models.FloatField(db_column='New_Order_Point', blank=True, null=True)  # Field name made lowercase.
    projected_order_point = models.FloatField(db_column='Projected_Order_Point', blank=True, null=True)  # Field name made lowercase.
    qoh = models.FloatField(db_column='QOH', blank=True, null=True)  # Field name made lowercase.
    average_qoh = models.FloatField(db_column='Average_QOH', blank=True, null=True)  # Field name made lowercase.
    retail_price = models.FloatField(db_column='Retail_Price', blank=True, null=True)  # Field name made lowercase.
    average_cost = models.FloatField(db_column='Average_Cost', blank=True, null=True)  # Field name made lowercase.
    replacement_cost = models.FloatField(db_column='Replacement_Cost', blank=True, null=True)  # Field name made lowercase.
    inv_value = models.FloatField(db_column='Inv_Value', blank=True, null=True)  # Field name made lowercase.
    new_inv_value = models.FloatField(db_column='New_Inv_Value', blank=True, null=True)  # Field name made lowercase.
    value_change = models.FloatField(db_column='Value_Change', blank=True, null=True)  # Field name made lowercase.
    lead_time_count = models.FloatField(db_column='Lead_Time_Count', blank=True, null=True)  # Field name made lowercase.
    forecast_model_used = models.TextField(db_column='Forecast_Model_Used', blank=True, null=True)  # Field name made lowercase.
    forecast_demand_per_day = models.FloatField(db_column='Forecast_Demand_Per_Day', blank=True, null=True)  # Field name made lowercase.
    total_days_of_supply = models.FloatField(db_column='Total_Days_Of_Supply', blank=True, null=True)  # Field name made lowercase.
    days_of_supply_required = models.FloatField(db_column='Days_Of_Supply_Required', blank=True, null=True)  # Field name made lowercase.
    demand_adjustment_factor = models.FloatField(db_column='Demand_Adjustment_Factor', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_all_stores_hardlines'


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
