"""
create by 维尼的小熊 on 2018/12/11

"""
__autor__ = 'yasin'

import re
from datetime import datetime
from datetime import timedelta
from rest_framework import serializers
from django.contrib.auth import get_user_model
from MxShop.settings import REGEX_MOBILE
from .models import VerifyCode
from rest_framework.validators import UniqueValidator

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    """
    发送验证码
    """
    mobile = serializers.CharField(max_length=11, help_text="手机号")

    def validate_mobile(self, mobile):
        """
        验证验证码是否发送
        :param mobile: 手机号
        :return: mobile
        """
        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile


class UserRegSerializer(serializers.ModelSerializer):
    """
    用户序列化
    """
    code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, label="验证码",
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 }, help_text="验证码")
    username = serializers.CharField(label="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")],
                                     help_text="用户名")

    password = serializers.CharField(
        style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
    )

    def validate_code(self, code):
        """
        验证验证码
        :param code:验证码
        """
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")

        if verify_records:
            # 最新的一条code
            last_record = verify_records[0]
            # 过期时间5分钟
            five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)

            # 对比时间
            if five_mintes_ago > last_record.add_time:
                raise serializers.ValidationError("验证码过期")

            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")

        else:
            raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        """
        数据之后处理
        :param attrs:所有字段
        :return:
        """
        attrs["mobile"] = attrs["username"]
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ('username', 'code', 'password')
