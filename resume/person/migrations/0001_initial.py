# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('education_name', models.CharField(max_length=200, null=True, blank=True)),
                ('education_speciality', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'education',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_last_name', models.CharField(max_length=50)),
                ('person_name', models.CharField(max_length=50)),
                ('person_father_name', models.CharField(max_length=50)),
                ('person_birthday', models.DateField(null=True, blank=True)),
                ('person_region', models.CharField(max_length=100)),
                ('person_city', models.CharField(max_length=100)),
                ('person_phone_number', models.IntegerField()),
                ('person_email', models.EmailField(max_length=75)),
                ('person_position', models.CharField(max_length=200)),
                ('person_skills', models.TextField()),
                ('person_views', models.IntegerField(default=0)),
                ('person_timestamp', models.DateTimeField(auto_now_add=True)),
                ('person_updated', models.DateTimeField(auto_now=True)),
                ('person_username', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'db_table': 'resume',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Previous',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('previous_place', models.CharField(max_length=200, null=True, blank=True)),
                ('previous_position', models.CharField(max_length=200, null=True, blank=True)),
                ('previous_person', models.ForeignKey(to='person.Person')),
            ],
            options={
                'db_table': 'previous_job',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='education',
            name='education_person',
            field=models.ForeignKey(to='person.Person'),
            preserve_default=True,
        ),
    ]
