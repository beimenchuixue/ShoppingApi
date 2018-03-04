from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

from .perminssions import IsOwnerOrReadOnly
from .models import UserFav
from .serializers import UserFavSerializer


class UserFavViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    用户收藏，包括创建用户收藏和取消用户收藏
    """
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer
    # 用户登录会取得数据，用户未登录将返回 detail: "用户信息未验证"
    # IsAuthenticated要求用户必须登录，IsOwnerOrReadOnly为自定义权限
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # 要求token验证, 新增 session 认证
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    # 查询以 goods_id 为依据， 删除数据的时候是以 goods_id 为依据，不再是 这张表的ID为依据
    lookup_field = 'goods_id'

    def get_queryset(self):
        """
        重新定义获得queryset数据，过滤获取当前用户的数据
        :return:
        """
        return UserFav.objects.filter(user=self.request.user)