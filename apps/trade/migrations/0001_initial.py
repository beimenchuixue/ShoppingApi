# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-24 09:10
from __future__ import unicode_literals

import datetime
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
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=0, help_text='商品数量', verbose_name='商品数量')),
                ('add_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('goods', models.ForeignKey(help_text='商品', on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '订单商品',
                'verbose_name_plural': '订单商品',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sn', models.CharField(help_text='订单编号', max_length=30, unique=True, verbose_name='订单编号')),
                ('trade_no', models.CharField(help_text='第三方支付编号', max_length=100, unique=True, verbose_name='第三方支付编号')),
                ('order_mount', models.FloatField(default=0, help_text='支付金额', verbose_name='支付金额')),
                ('pay_time', models.DateTimeField(default=datetime.datetime.now, help_text='支付时间', verbose_name='支付时间')),
                ('address', models.CharField(help_text='收货地址', max_length=100, verbose_name='收货地址')),
                ('pay_type', models.CharField(choices=[('alipay', '支付宝'), ('wechat', '微信')], default='alipay', help_text='支付类型', max_length=10, verbose_name='支付类型')),
                ('post_script', models.CharField(help_text='订单留言', max_length=200, verbose_name='订单留言')),
                ('singer_name', models.CharField(help_text='签收人', max_length=20, verbose_name='签收人')),
                ('singer_mobile', models.CharField(help_text='手机号码', max_length=11, verbose_name='手机号码')),
                ('add_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('user', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '订单详情',
                'verbose_name_plural': '订单详情',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nums', models.IntegerField(default=0, verbose_name='购买数量')),
                ('add_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('goods', models.ForeignKey(help_text='商品', on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
                ('user', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(help_text='订单信息', on_delete=django.db.models.deletion.CASCADE, to='trade.OrderInfo', verbose_name='订单信息'),
        ),
        migrations.AlterUniqueTogether(
            name='shoppingcart',
            unique_together=set([('user', 'goods')]),
        ),
    ]
