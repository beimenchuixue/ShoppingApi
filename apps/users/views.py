from random import sample

from django.db.models import Q
from django.contrib.auth.backends import ModelBackend
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler

from django.contrib.auth import get_user_model
UserProfile = get_user_model()
from users.models import VerifyCode
from users.serializers import SmsSerializer, UserRegisterSerializer

from utils.yunpian import YunPian


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


class SmsCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    发送短信验证码
    """
    serializer_class = SmsSerializer

    def __get_random_code(self, code_len=6):
        code_str = '0123456789'
        return ''.join(sample(code_str, code_len))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 发送验证码
        code = self.__get_random_code()
        mobile = serializer.validated_data['mobile']
        yun_pian = YunPian('b1d45af7f60a69881ec49ac396b93a7d')
        response = yun_pian.send_sms(code=code, mobile=mobile)

        if response.get('code', 'fail') == 0:
            # 发送成功
            # 保存到数据库
            verify_code = VerifyCode(code=code, mobile=mobile)
            verify_code.save()

            # api规范返回状态码
            return Response({
                'mobile': mobile,
                'msg': response.get('msg', '发送成功')
            }, status.HTTP_201_CREATED)

        else:
            # 发送失败, 返回错误信息
            return Response({
                'mobile': mobile,
                'msg': response.get('msg', '发送出错')
            }, status.HTTP_400_BAD_REQUEST)


class UserRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    创建用户
    """
    serializer_class = UserRegisterSerializer
    queryset = UserProfile.objects.all()

    def create(self, request, *args, **kwargs):
        """
        自定义返回前端数据，前端需要 token 和 name信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict['token'] = jwt_encode_handler(payload)
        re_dict['name'] = user.name if user.name else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()