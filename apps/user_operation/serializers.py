__author__ = 'beimenchuixue'
__blog__ = 'http://www.cnblogs.com/2bjiujiu/'
__date__ = '2018/3/2 14:48'


from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserFav


class UserFavSerializer(serializers.ModelSerializer):
    """
    用户收藏，只需要显示当前用户则可
    """
    user = serializers.HiddenField(
        # 获取当前用户
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav

        # 定义返回得字段信息
        fields = ('user', 'goods')

        # 作用两个字段之上，可以写在Meta之中，出错显示 non_filed_errors
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message='已收藏'
            )
        ]