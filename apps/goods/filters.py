__author__ = 'beimenchuixue'
__blog__ = 'http://www.cnblogs.com/2bjiujiu/'
__date__ = '2018/2/27 10:34'

import django_filters
from django.db.models import Q
from goods.models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """商品过滤信息"""
    # 最大价格
    princemin = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    # 最小价格
    princemax = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    # 上一级目录信息, method指明一个查询方法，自定义查询方法
    top_category = django_filters.NumberFilter(method='top_queryset_filter')

    def top_queryset_filter(self, queryset, name, value):
        # 先判断是否是三级目录，不是再往上找一级，不是再往上找一级
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['princemin', 'princemax', 'top_category', 'is_hot']