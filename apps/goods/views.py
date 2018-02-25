from goods.serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Goods


class GoodsListView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        # 对于列表一定要添加many=True字段，才会序列化为数组对象
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

