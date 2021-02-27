# Generated by Django 2.2.5 on 2021-02-25 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='breakfast',
        ),
        migrations.RemoveField(
            model_name='room',
            name='wifi',
        ),
        migrations.AddField(
            model_name='room',
            name='smoke',
            field=models.BooleanField(default=False, verbose_name='Smoking Availability'),
        ),
    ]