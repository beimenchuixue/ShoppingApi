from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfile(User):
    """
    用户信息，继承并扩展默认表
    """
    gender_choice = (
        (0, '男'),
        (1, '女')
    )
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name='用户名', help_text='用户名')
    birthday = models.DateField(null=True, blank=True, verbose_name='生日', help_text='生日')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号码', help_text='手机号码')
    gender = models.IntegerField(default=1, verbose_name='性别', help_text='性别')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    验证码
    """
    code = models.CharField(max_length=12, verbose_name='验证码', help_text='验证码')
    mobile = models.CharField(max_length=11, verbose_name='手机号码', help_text='手机号码')

    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.mobile
