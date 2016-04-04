# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencenet', '0004_auto_20151128_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='influencenode',
            name='influences',
        ),
        migrations.AddField(
            model_name='influencenode',
            name='influenced_by',
            field=models.ForeignKey(to='influencenet.InfluenceNode', null=True, related_name='influenced'),
        ),
    ]
