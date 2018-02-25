__author__ = 'beimenchuixue'
__blog__ = 'http://www.cnblogs.com/2bjiujiu/'
__date__ = '2018/2/24 15:28'

import json

from django.views.generic.base import View
# cbv 方式
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from goods.models import Goods


class GoodsListView(View):
    """
    返回商品详情页面
    """
    def get(self, request):
        goods = Goods.objects.all()[:10]
        json_data = serializers.serialize('json', goods)
        # json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)