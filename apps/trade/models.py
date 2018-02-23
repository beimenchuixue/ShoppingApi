from datetime import  datetime

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

from goods.models import Goods


class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品', help_text='商品')
    goods_num = models.IntegerField(default=0, verbose_name='购买数量')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name


class OrderInfo(models.Model):
    """
    订单详情
    """
    status_choice = (
        ('success', '成功'),
        ('cancel', '取消'),
        ('wait', '待支付')
    )
    pay_style = (
        ('alipay', '支付宝'),
        ('wechat', '微信')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    order_sn = models.CharField(max_length=30, unique=True, verbose_name='订单编号', help_text='订单编号')
    trade_no = models.CharField(max_length=100, unique=True, verbose_name='第三方支付编号', help_text='第三方支付编号')
    order_mount = models.FloatField(default=0, verbose_name='支付金额', help_text='支付金额')
    pay_time = models.DateTimeField(default=datetime.now, verbose_name='支付时间', help_text='支付时间')
    address = models.CharField(max_length=100, verbose_name='收货地址', help_text='收货地址')
    pay_type = models.CharField(max_length=10, default='alipay', choices=pay_style, verbose_name='支付类型', help_text='支付类型')
    post_script = models.CharField(max_length=200, verbose_name='订单留言', help_text='订单留言')
    singer_name = models.CharField(max_length=20, verbose_name='签收人', help_text='签收人')
    singer_mobile = models.CharField(max_length=11, verbose_name='手机号码', help_text='手机号码')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_sn


class OrderGoods(models.Model):
    """
    订单商品
    """
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name='订单信息', help_text='订单信息')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品', help_text='商品')
    goods_num = models.IntegerField(default=0, verbose_name='商品数量', help_text='商品数量')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
