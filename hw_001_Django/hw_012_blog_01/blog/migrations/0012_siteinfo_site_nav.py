# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170821_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='site_nav',
            field=models.TextField(default='', verbose_name='站点导航'),
        ),
    ]
