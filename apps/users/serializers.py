__author__ = 'beimenchuixue'
__blog__ = 'http://www.cnblogs.com/2bjiujiu/'
__date__ = '2018/3/1 12:16'

import re
from datetime import datetime, timedelta

from rest_framework import serializers
from django.contrib.auth import get_user_model
UserProfile = get_user_model()

from ShoppingApi.settings import REGEX_MOBILE
from users.models import VerifyCode


class SmsSerializer(serializers.Serializer):
    """
    短信验证
    """
    mobile = serializers.CharField(required=True, max_length=11)

    def validate_mobile(self, mobile):
        """验证手机号码合法性"""
        # 验证 手机号码是否合法
        p = re.compile(REGEX_MOBILE)
        if not p.match(mobile):
            raise serializers.ValidationError("手机号码非法")

        # 验证发送频率
        send_ago_time = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        # 添加时间在一分钟以内
        if VerifyCode.objects.filter(add_time__gt=send_ago_time, mobile=mobile):
            raise serializers.ValidationError("距离上一次发送未超过一分钟")

        # 手机是否注册
        if UserProfile.objects.filter(mobile=mobile):
            raise serializers.ValidationError("用户已经存在")

        return mobile
