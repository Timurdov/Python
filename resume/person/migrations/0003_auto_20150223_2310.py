# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20150223_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='person_username',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
