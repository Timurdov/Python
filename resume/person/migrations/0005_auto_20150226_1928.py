# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20150226_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='person_region',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
