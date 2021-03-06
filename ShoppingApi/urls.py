"""ShoppingApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
from ShoppingApi.settings import MEDIA_ROOT
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
import xadmin

from goods.views import GoodsViewSet, CategoryViewSet
from users.views import SmsCodeViewSet, UserRegisterViewSet
from user_operation.views import UserFavViewSet

router = DefaultRouter()
# 获取商品列表信息
router.register(r'goods', GoodsViewSet, base_name='goods')
# 获取类别信息
router.register(r'categorys', CategoryViewSet, base_name='categorys')
# 注册发送短信验证码接口
router.register(r'codes', SmsCodeViewSet, base_name='codes')
# 用户注册接口
router.register(r'register', UserRegisterViewSet, base_name='register')
# 收藏
router.register(r'userfav', UserFavViewSet, base_name='userfav')

urlpatterns = [
    # xadmin 后台
    url(r'^xadmin/', xadmin.site.urls),
    # 上传文件地址
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # 文档， title 指定文档后台的总标题
    url(r'^docs/', include_docs_urls(title='生鲜商城')),
    # 用户登录接口
    url(r'^api-auth/', include('rest_framework.urls')),
    # 通过 router来管理url接口
    url(r'', include(router.urls)),
    # # 用户 token验证接口, 用户提交用户名或密码验证获取token接口
    # url(r'^api-token-auth/', views.obtain_auth_token),
    # JWT 验证接口
    url(r'^login/', obtain_jwt_token)
]
