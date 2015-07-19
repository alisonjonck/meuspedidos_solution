# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('html', models.IntegerField(null=True, blank=True)),
                ('css', models.IntegerField(null=True, blank=True)),
                ('javascript', models.IntegerField(null=True, blank=True)),
                ('python', models.IntegerField(null=True, blank=True)),
                ('django', models.IntegerField(null=True, blank=True)),
                ('ios', models.IntegerField(null=True, blank=True)),
                ('android', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
