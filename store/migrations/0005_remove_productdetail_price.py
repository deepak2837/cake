# Generated by Django 3.0.3 on 2020-05-15 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_productdetail_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetail',
            name='price',
        ),
    ]