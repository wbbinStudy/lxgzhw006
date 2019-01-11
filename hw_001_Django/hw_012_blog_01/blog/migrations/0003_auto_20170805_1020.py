# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170802_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_type',
            field=models.CharField(choices=[('0', '草稿'), ('1', '软删除'), ('2', '正常')], default='0', max_length=10, verbose_name='文章类别'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_mobile',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='电话号码'),
        ),
    ]
