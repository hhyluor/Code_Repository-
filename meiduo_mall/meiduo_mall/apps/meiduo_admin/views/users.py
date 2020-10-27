from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import mixins

from meiduo_admin.serializers.users import AdminAuthSerializer

from users.models import User
from meiduo_admin.serializers.users import UserInfoSerializer

# 思考：AdminAuthView视图代码能不能去做简化？GenericAPIView -> Mixin -> 子类视图


# POST /meiduo_admin/authorizations/
class AdminAuthView(APIView):
    def post(self, request):
        """
        管理员登录:
        ① 获取参数并进行校验(参数完整性、用户名和密码是否正确)
        ② 服务器生成jwt token
        ③ 返回响应数据，携带jwt token
        """
        # ① 获取参数并进行校验(参数完整性、用户名和密码是否正确)
        serializer = AdminAuthSerializer(data=request.data)
        # 默认校验：参数完整性、数据类型、选项参数的限制
        serializer.is_valid(raise_exception=True)

        # ② 服务器生成jwt token
        serializer.save() # 调用序列化器类中的create

        # ③ 返回响应数据，携带jwt token
        return Response(serializer.data, status=201)


# GET /meiduo_admin/users/?keyword=<关键字>
class UserInfoView(ListAPIView):
    permission_classes = [IsAdminUser]

    serializer_class = UserInfoSerializer
    # queryset = "查询集"

    def get_queryset(self):
        """重写父类的 get_queryset 方法"""
        keyword = self.request.query_params.get('keyword')
        #不同的情况，对应不同的查询集
        if not keyword:
            # 1.1 如果keyword未传递，查询所有的普通用户数据，进行返回
            users = User.objects.filter(is_staff=False)
        else:
            # 1.2 如果keyword传递了，查询用户名中含有keyword的普通用户的数据，进行返回
            users = User.objects.filter(is_staff=False, username__contains=keyword)

        return users

    # def get(self, request):
    #     """
    #     self.request：就是请求对象
    #     获取普通用户的数据：
    #     ① 查询数据库获取普通用户的数据
    #     1.1 如果keyword未传递，查询所有的普通用户数据，进行返回
    #     1.2 如果keyword传递了，查询用户名中含有keyword的普通用户的数据，进行返回
    #     ② 将查询到普通用户的数据序列化返回
    #     """
    #     return self.list(request)

    # @permission_required('users.view_user_api',raise_exception=True)
    @method_decorator(permission_required('users.view_user_api',raise_exception=True))
    def get(self, request):
        return super().get(request)