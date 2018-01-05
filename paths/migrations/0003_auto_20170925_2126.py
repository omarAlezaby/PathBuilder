# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paths', '0002_auto_20170925_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='depend_on',
        ),
        migrations.AddField(
            model_name='course',
            name='depend_on',
            field=models.ManyToManyField(blank=True, related_name='_course_depend_on_+', to='paths.Course'),
        ),
    ]