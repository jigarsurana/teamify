# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('email_id', models.EmailField(max_length=80, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=15)),
                ('google_id', models.CharField(max_length=200, blank=True)),
                ('facebook_id', models.CharField(max_length=200, blank=True)),
                ('gender', models.CharField(max_length=1, blank=True)),
                ('city', models.CharField(max_length=51, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
