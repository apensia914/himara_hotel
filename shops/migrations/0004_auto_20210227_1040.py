# Generated by Django 2.2.5 on 2021-02-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_auto_20210226_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopitem',
            name='item_price',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Item Price'),
        ),
    ]