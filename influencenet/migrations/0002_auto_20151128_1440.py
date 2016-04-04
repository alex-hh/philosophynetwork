# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencenet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='philosopher',
            name='dbpedia_link',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='philosopher',
            name='freebase_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='philosopher',
            name='date_of_birth',
            field=models.DateTimeField(null=True),
        ),
    ]
