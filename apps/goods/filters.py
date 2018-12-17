# -*- coding: utf-8 -*-
__author__ = 'bobby'

import django_filters
from django.db.models import Q
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    pricemin = django_filters.NumberFilter(field_name='shop_price', lookup_expr='gte', help_text="最低价格")
    pricemax = django_filters.NumberFilter(field_name='shop_price', lookup_expr='lte', help_text='最高价格')

    # 模糊匹配
    # name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', help_text='商品名字')

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax']
