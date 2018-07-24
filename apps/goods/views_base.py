"""
create by 维尼的小熊 on 2018/7/24

"""
__autor__ = 'yasin'

from django.views.generic.base import View
from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()[:10]

        from django.core import serializers
        import json

        json_data = serializers.serialize("json", goods)
        json_data = json.loads(json_data)

        from django.http import JsonResponse
        return JsonResponse(json_data, safe=False)
