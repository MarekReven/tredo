# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tredo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.CharField(max_length=40),
        ),
    ]
