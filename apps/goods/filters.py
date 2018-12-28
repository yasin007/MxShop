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
    top_category = django_filters.NumberFilter(method='top_category_filter')
    is_new = django_filters.Filter(field_name='is_new', help_text="是否为最新")
    is_hot = django_filters.Filter(field_name='is_hot', help_text="是否为热销")
    is_ship_free = django_filters.Filter(field_name='ship_free', help_text="是否为承担运费")

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'is_new', 'is_hot', 'is_ship_free']
