from goods.serializers import GoodsSerializer
from rest_framework import mixins, viewsets
from rest_framework import filters

from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Goods
from goods.filters import GoodsFilter


class GoodsPagination(PageNumberPagination):
    # 一页显示数据多少
    page_size = 10
    # 通过page_size请求定义一页显示多少数据
    page_size_query_param = 'page_size'
    # 通过p来表示获得多少页的数据
    page_query_param = 'page'
    # 定义最大一页获得多少数据
    max_page_size = 10


class GoodsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表, 分页， 搜索， 过滤， 排序
    """
    queryset = Goods.objects.all()
    # 指定显示字段
    serializer_class = GoodsSerializer
    # 指定分页
    pagination_class = GoodsPagination
    # 指定过滤相关类
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 指定精确过滤字段
    # 指定过滤类
    filter_class = GoodsFilter
    # 指定在哪些内容里搜索
    search_fields = ('name', 'goods_brief', 'goods_desc')
    # 排序过滤
    ordering_fields = ('goods_num', 'shop_price')



