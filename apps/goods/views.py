from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer
from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination


class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页,分页，过滤，搜索，排序
    """

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # 分页
    pagination_class = GoodsPagination
    # 过滤DjangoFilterBackend
    # 搜索SearchFilter 可对对应字段加入正则表达式
    # 排序OrderingFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'add_time')


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type='1')
    serializer_class = CategorySerializer
