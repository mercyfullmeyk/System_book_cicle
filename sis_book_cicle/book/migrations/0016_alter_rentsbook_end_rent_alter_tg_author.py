# Generated by Django 5.1.1 on 2025-01-14 16:38

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_alter_rentsbook_end_rent'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentsbook',
            name='end_rent',
            field=models.DateField(default=datetime.datetime(2025, 2, 13, 16, 38, 32, 14486)),
        ),
        migrations.AlterField(
            model_name='tg',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
