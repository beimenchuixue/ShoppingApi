__author__ = 'beimenchuixue'
__blog__ = 'http://www.cnblogs.com/2bjiujiu/'
__date__ = '2018/3/2 18:42'

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    让用户只能操作自己相关的数据
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
