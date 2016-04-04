# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencenet', '0005_auto_20151128_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='influencenode',
            name='influenced_by',
        ),
    ]
