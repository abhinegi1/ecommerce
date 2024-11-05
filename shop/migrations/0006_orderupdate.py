# Generated by Django 5.0.8 on 2024-10-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_orders_amount_remove_orders_transaction_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=25533)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]