# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IN_NUM', models.CharField(max_length=100)),
                ('OUT_NUM', models.CharField(max_length=100)),
            ],
        ),
    ]
