# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfluenceEdge',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Philosopher',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateTimeField()),
                ('influences', models.ManyToManyField(related_name='_philosopher_influences_+', to='influencenet.Philosopher')),
            ],
        ),
        migrations.AddField(
            model_name='influenceedge',
            name='follower',
            field=models.ForeignKey(related_name='follower', to='influencenet.Philosopher'),
        ),
        migrations.AddField(
            model_name='influenceedge',
            name='influencer',
            field=models.ForeignKey(related_name='influencer', to='influencenet.Philosopher'),
        ),
    ]
