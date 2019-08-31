# Generated by Django 2.2.3 on 2019-08-29 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payzant', '0003_tblallstoreshardlines'),
    ]

    operations = [
        migrations.CreateModel(
            name='DbItemByStore',
            fields=[
                ('store', models.TextField(db_column='Store')),
                ('item_number', models.TextField(db_column='Item_Number')),
                ('new_order_point', models.IntegerField(blank=True, db_column='New_Order_Point', null=True)),
                ('qoh', models.IntegerField(blank=True, db_column='QOH', null=True)),
                ('retail_price', models.FloatField(blank=True, db_column='Retail_Price', null=True)),
                ('average_cost', models.FloatField(blank=True, db_column='Average_Cost', null=True)),
                ('replacement_cost', models.FloatField(blank=True, db_column='Replacement_Cost', null=True)),
                ('inv_value', models.FloatField(blank=True, db_column='Inv_Value', null=True)),
                ('new_inv_value', models.FloatField(blank=True, db_column='New_Inv_Value', null=True)),
                ('forecast_demand_per_day', models.FloatField(blank=True, db_column='Forecast_Demand_Per_Day', null=True)),
                ('storenumber', models.TextField(db_column='StoreNumber')),
                ('storeshortname', models.TextField(blank=True, db_column='StoreShortName', null=True)),
                ('classcode', models.TextField(blank=True, db_column='ClassCode', null=True)),
                ('classname', models.TextField(blank=True, db_column='ClassName', null=True)),
                ('finelinecode', models.TextField(blank=True, db_column='FinelineCode', null=True)),
                ('finelinename', models.TextField(blank=True, db_column='FinelineName', null=True)),
                ('itemdescription', models.TextField(db_column='ItemDescription')),
                ('netsales2014', models.FloatField(blank=True, db_column='NetSales2014', null=True)),
                ('netsales2015', models.FloatField(blank=True, db_column='NetSales2015', null=True)),
                ('netsales2016', models.FloatField(blank=True, db_column='NetSales2016', null=True)),
                ('netsales2017', models.FloatField(blank=True, db_column='NetSales2017', null=True)),
                ('netsales2018', models.FloatField(blank=True, db_column='NetSales2018', null=True)),
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'db_item_by_store',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='TblAllStoresHardlines',
        ),
    ]