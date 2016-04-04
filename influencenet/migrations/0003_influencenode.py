# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencenet', '0002_auto_20151128_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfluenceNode',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateTimeField(null=True)),
                ('freebase_id', models.CharField(max_length=50, null=True)),
                ('dbpedia_link', models.CharField(max_length=200, null=True)),
                ('is_philosopher', models.BooleanField(default=False)),
                ('is_writer', models.BooleanField(default=False)),
                ('influences', models.ManyToManyField(to='influencenet.InfluenceNode', related_name='_influencenode_influences_+')),
            ],
        ),
    ]
