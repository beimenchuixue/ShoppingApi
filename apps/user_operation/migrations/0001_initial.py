# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-24 09:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(default='', help_text='省份', max_length=100, verbose_name='省份')),
                ('city', models.CharField(default='', help_text='城市', max_length=100, verbose_name='城市')),
                ('district', models.CharField(help_text='区域', max_length=100, verbose_name='区域')),
                ('address', models.CharField(help_text='详细地址', max_length=300, verbose_name='详细地址')),
                ('singer_name', models.CharField(help_text='签收人', max_length=20, verbose_name='签收人')),
                ('singer_mobile', models.CharField(help_text='手机号码', max_length=11, verbose_name='手机号码')),
                ('add_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('user', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户地址信息',
                'verbose_name_plural': '用户地址信息',
            },
        ),
        migrations.CreateModel(
            name='UserFav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('goods', models.ForeignKey(help_text='商品', on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
                ('user', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户收藏',
                'verbose_name_plural': '用户收藏',
            },
        ),
        migrations.CreateModel(
            name='UserLeavingMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.IntegerField(default=0, help_text='留言类型', verbose_name='留言类型')),
                ('subject', models.CharField(help_text='留言主题', max_length=20, verbose_name='留言主题')),
                ('message', models.CharField(help_text='留言内容', max_length=100, verbose_name='留言内容')),
                ('file', models.FileField(help_text='上传文件', max_length=50, upload_to='message', verbose_name='上传文件')),
                ('add_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('user', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户留言',
                'verbose_name_plural': '用户留言',
            },
        ),
    ]
