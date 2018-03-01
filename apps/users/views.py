from django.shortcuts import render

# Create your views here.

from django.db.models import Q
from django.contrib.auth.backends import ModelBackend

from django.contrib.auth import get_user_model
UserProfile = get_user_model()
# from users.models import UserProfile


class CustomBackend(ModelBackend):
    """
    自定义用户验证，用邮箱和手机号码登录
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(mobile=username))

            if user.check_password(raw_password=password):
                return user
        except Exception as e:
            print(e)
            return None
