from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

from goods.models import Goods


class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name='用户', help_text='用户')
    goods = models.ForeignKey(Goods, verbose_name='商品', help_text='商品')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        # 联合唯一
        unique_together = ('user', 'goods')

    def __str__(self):
        return self.goods.name


class UserLeavingMessage(models.Model):
    """
    用户留言信息
    """
    message_type_choice = (
        (1, "留言"),
        (2, "投诉"),
        (3, "询问"),
        (4, "售后"),
        (5, "求购")
    )
    user = models.ForeignKey(User, verbose_name='用户', help_text='用户')
    message_type = models.IntegerField(default=0, verbose_name='留言类型', help_text='留言类型')
    subject = models.CharField(max_length=20, verbose_name='留言主题', help_text='留言主题')
    message = models.CharField(max_length=100, verbose_name='留言内容', help_text='留言内容')
    file = models.FileField(max_length=50, upload_to='message', verbose_name='上传文件', help_text='上传文件')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '用户留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):
    """
    用户地址信息
    """
    user = models.ForeignKey(User, verbose_name='用户', help_text='用户')
    province = models.CharField(max_length=100, default="", verbose_name="省份", help_text='省份')
    city = models.CharField(max_length=100, default="", verbose_name="城市", help_text='城市')
    district = models.CharField(max_length=100, verbose_name='区域', help_text='区域')
    address = models.CharField(max_length=300, verbose_name='详细地址', help_text='详细地址')
    signer_name = models.CharField(max_length=20, verbose_name='签收人', help_text='签收人')
    signer_mobile = models.CharField(max_length=11, verbose_name='手机号码', help_text='手机号码')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '用户地址信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.signer_name