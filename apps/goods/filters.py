__author__ = 'beimenchuixue'
__blog__ = 'http://www.cnblogs.com/2bjiujiu/'
__date__ = '2018/2/27 10:34'

import django_filters
from goods.models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    prince_min = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    prince_max = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['prince_min', 'prince_max', 'name']