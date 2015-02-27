# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20150223_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('branch', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'branch',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profession', models.CharField(max_length=100)),
                ('profession_branch', models.ForeignKey(to='person.Branch')),
            ],
            options={
                'db_table': 'profession',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'region',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='person_branch',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='person_profession',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='person_position',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
