import re

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from users.models import User


class PermissionSerializer(serializers.ModelSerializer):
    """权限序列化器类"""
    class Meta:
        model = Permission
        fields = '__all__'


class ContentTypeSerializer(serializers.ModelSerializer):
    """权限类型序列化器类"""
    class Meta:
        model = ContentType
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    """用户组序列化器类"""
    class Meta:
        model = Group
        fields = '__all__'


class PermSimpleSerializer(serializers.ModelSerializer):
    """权限简单序列化器类"""
    class Meta:
        model = Permission
        fields = ('id', 'name')


class AdminSerializer(serializers.ModelSerializer):
    """管理员用户序列化器类"""
    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'email',
                  'groups', 'user_permissions', 'password')

        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': False,
                'allow_blank': True # 是否允许传空字符串：""
            }
        }

    def validate_mobile(self, value):
        # 是否符合手机号格式
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('手机号格式错误')

        return value

    # ModelSerializer是否需要重写 create？需要重写
    # ① 密码需要加密保存
    # ② 如果密码没传或传递是""，需要设置默认密码

    def create(self, validated_data):
        # 添加管理员的标记
        validated_data['is_staff'] = True
        # ① 先把管理员用户的其他数据保存起来
        user = super().create(validated_data)

        # ② 在进行密码设置(是否需要设置默认密码、密码加密)
        password = validated_data.get('password')

        if not password:
            # password为None或""，设置默认密码
            password = '123456abc'

        # 密码加密保存
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        """修改管理员用户"""
        # 从`validated_data`中去除密码`password`
        password = validated_data.pop('password', None)

        # 修改管理员账户信息
        super().update(instance, validated_data)

        # 修改密码
        if password:
            instance.set_password(password)
            instance.save()

        return instance

class GroupSimpleSerializer(serializers.ModelSerializer):
    """用户组序列化器类"""
    class Meta:
        model = Group
        fields = ('id', 'name')
