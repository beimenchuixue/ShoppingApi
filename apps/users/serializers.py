__author__ = 'beimenchuixue'
__blog__ = 'http://www.cnblogs.com/2bjiujiu/'
__date__ = '2018/3/1 12:16'

import re
from datetime import datetime, timedelta

from rest_framework import serializers
# 唯一数据验证
from rest_framework.validators import UniqueValidator
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


class UserRegisterSerializer(serializers.ModelSerializer):
    # 验证验证码输入并提示信息
    code = serializers.CharField(max_length=6, min_length=6, write_only=True, required=True, help_text='验证码', label='验证码', error_messages={
        'blank': "验证码不能为空",
        'required': '请输入验证码',
        'min_length': '验证码格式错误',
        'max_length': "验证码格式错误"
    })

    username = serializers.CharField(required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=UserProfile.objects.all())],
                                     label='用户名', error_messages={
            'blank': '用户名不能为空',
            'required': '请输入用户名',
            'validators': '用户已经注册'
        })
    password = serializers.CharField(style={
        'input_type': 'password'
    }, label='密码', write_only=True)

    # def create(self, validated_data):
    #     """
    #     进行明文密码进行加密
    #     :param validated_data:
    #     :return:
    #     """
    #     # 重写但是又继承父类的方法
    #     user = super(UserRegisterSerializer, self).create(validated_data=validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

    def validate_code(self, code):
        """
        code验证, 作用单个字段验证
        :param code:
        :return:
        """
        code_youxiao_time = 10
        print(code)
        last_verify_code = VerifyCode.objects.filter(mobile=self.initial_data['username']).order_by('-add_time')
        if last_verify_code:
            last_verify_code = last_verify_code[0]
            # 验证验证码是否正确
            if last_verify_code.code != code:
                raise serializers.ValidationError('验证码出错')
            # 当最新时间加上过期时间大于验证码提交的时候时间，认为验证码过期
            if last_verify_code.add_time + timedelta(hours=0, minutes=code_youxiao_time, seconds=0) < datetime.now():
                raise serializers.ValidationError('验证码过期')
            return code
        else:
            raise serializers.ValidationError('验证码出错')

    def validate(self, attrs):
        """作用于这个serializers全局字段, 对全局数据进行处理"""
        # 新增 mobile字段为 username
        attrs['mobile'] = attrs['username']
        # 删除 数据中的 code信息
        del attrs['code']
        return attrs

    class Meta:
        model = UserProfile
        fields = ('username', 'code', 'mobile', 'password')