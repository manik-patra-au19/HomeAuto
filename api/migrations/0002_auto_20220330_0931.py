# Generated by Django 3.1.5 on 2022-03-30 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='fanstatus',
            field=models.IntegerField(choices=[(0, 0), (1, 1)], default=0),
        ),
        migrations.AlterField(
            model_name='device',
            name='lightStatus',
            field=models.IntegerField(choices=[(0, 0), (1, 1)], default=0),
        ),
    ]
