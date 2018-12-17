"""
create by 维尼的小熊 on 2018/12/14

"""
__autor__ = 'yasin'
from rest_framework import serializers
from goods.models import Goods, GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    商品分类序列化
    """
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    """
    商品序列化
    """
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = "__all__"
