# Generated by Django 3.2.13 on 2022-07-12 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_mensaje_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
