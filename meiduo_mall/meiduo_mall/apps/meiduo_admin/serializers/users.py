from rest_framework import serializers

from users.models import User


class AdminAuthSerializer(serializers.ModelSerializer):
    """管理员登录序列化器类"""
    # 不能自动生成的字段，可以自己添加
    token = serializers.CharField(label='JWT Token', read_only=True)

    # 能自动生成，但是要覆盖，也可以自己添加
    username = serializers.CharField(label='用户名')

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'token')

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate(self, attrs):
        """用户名和密码是否正确"""
        # 获取 username 和 password
        username = attrs.get('username')
        password = attrs.get('password')

        # 查询管理员用户是否存在
        try:
            user = User.objects.get(username=username, is_staff=True)
        except User.DoesNotExist:
            # 用户不存在
            raise serializers.ValidationError('用户名或密码错误')
        else:
            # 校验密码是否正确
            if not user.check_password(password):
                raise serializers.ValidationError('用户名或密码错误')

            # 将 user 对象添加到 attrs 中
            attrs['user'] = user

        # 参数是必须返回的！！！
        # attrs中有什么，validated_data中就有什么
        return attrs

    def create(self, validated_data):
        # 获取 user 对象
        user = validated_data.get('user')

        # 生成jwt token
        from rest_framework_jwt.settings import api_settings

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        # 返回user对象之前，临时给user对象增加一个token属性
        user.token = token

        return user


class UserInfoSerializer(serializers.ModelSerializer):
    """普通用户的序列化器类"""
    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'email')
