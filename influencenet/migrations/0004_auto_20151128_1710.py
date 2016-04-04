# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencenet', '0003_influencenode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influenceedge',
            name='follower',
            field=models.ForeignKey(related_name='follower', to='influencenet.InfluenceNode'),
        ),
        migrations.AlterField(
            model_name='influenceedge',
            name='influencer',
            field=models.ForeignKey(related_name='influencer', to='influencenet.InfluenceNode'),
        ),
    ]
