__author__ = 'beimenchuixue'
__blog__ = 'http://www.cnblogs.com/2bjiujiu/'
__date__ = '2018/2/24 17:04'

from rest_framework import serializers
from goods.models import Goods
from goods.models import GoodsCategory, GoodsImage


class GoodsImageSerializer(serializers.ModelSerializer):
    """
    商品相关的轮播图
    """
    class Meta:
        model = GoodsImage
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    image = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = '__all__'


class CategorySerializer3(serializers.ModelSerializer):
    """
    三级类
    """
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer2(serializers.ModelSerializer):
    """
    二级类
    """
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsCategorySerializer(serializers.ModelSerializer):
    """
    一级类
    """
    # 返回多条数据需要给定 many=True参数
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'