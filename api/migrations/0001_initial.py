# Generated by Django 3.1.5 on 2022-03-28 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('deviceID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('devicetype', models.CharField(max_length=20)),
                ('lightStatus', models.ImageField(choices=[(0, 0), (1, 1)], default=0, upload_to='')),
                ('fanstatus', models.ImageField(choices=[(0, 0), (1, 1)], default=0, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UserDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.device')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
