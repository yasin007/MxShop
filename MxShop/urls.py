# Django 项目的 URL 声明，就像你网站的“目录”

from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from users.views import SmsCodeViewset, UserViewSet
from goods.views import GoodsListViewSet, CategoryViewSet
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.documentation import include_docs_urls
import xadmin

router = DefaultRouter()

# 发送验证码
router.register(r'codes', SmsCodeViewset, base_name="codes")
# 注册
router.register(r'users', UserViewSet, base_name='users')

# 商品列表
router.register(r'goods', GoodsListViewSet, base_name='goods')

# 商品分类列表
router.register(r'categorys', CategoryViewSet, base_name='categorys')
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^xadmin/', xadmin.site.urls),
    # 文档
    url(r'docs/', include_docs_urls(title="慕学生鲜")),
    # drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt的认证接口
    url(r'^login/', obtain_jwt_token),
]
