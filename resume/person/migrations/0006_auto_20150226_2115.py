# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_auto_20150226_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='person_branch',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
