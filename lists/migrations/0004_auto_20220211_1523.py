# Generated by Django 2.2.5 on 2022-02-11 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20220211_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to=settings.AUTH_USER_MODEL),
        ),
    ]
