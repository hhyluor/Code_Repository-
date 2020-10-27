from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.permissions import PermissionSerializer, ContentTypeSerializer, GroupSerializer, \
    PermSimpleSerializer, AdminSerializer, GroupSimpleSerializer
from users.models import User


class PermissionViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    lookup_value_regex = '\d+'

    # GET /meiduo_admin/permission/perms/ -> list
    # POST /meiduo_admin/permission/perms/ -> create
    # GET /meiduo_admin/permission/perms/(?P<pk>\d+)/ -> retrieve
    # PUT /meiduo_admin/permission/perms/(?P<pk>\d+)/ -> update
    # DELETE /meiduo_admin/permission/perms/(?P<pk>\d+)/ -> destroy

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     # 问题1：考虑 PermissionSerializer 能不能直接用？
    #     # ① 考虑序列化器类的字段是否满足需求？② 考虑字段的read_only和write_only设置是否正确？
    #     serializer = self.get_serializer(data=request.data)
    #     # 问题2：考虑是否需要补充验证？
    #     serializer.is_valid(raise_exception=True)
    #     # 问题3：考虑序列化器类中的create是否满足业务需要？
    #     serializer.save() # 调用序列化器类中的create
    #     return Response(serializer.data, status=201)


# GET /meiduo_admin/permission/content_types/
class ContentTypeView(ListAPIView):
    permission_classes = [IsAdminUser]

    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer

    # 关闭分页
    pagination_class = None


class GroupViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    lookup_value_regex = '\d+'

    # GET /meiduo_admin/permission/groups/ -> list
    # POST /meiduo_admin/permission/groups/ -> create
    # GET /meiduo_admin/permission/simple/ -> simple
    # GET /meiduo_admin/permission/groups/(?P<pk>\d+)/ -> retrieve
    # PUT /meiduo_admin/permission/groups/(?P<pk>\d+)/ -> update
    # DELETE /meiduo_admin/permission/groups/(?P<pk>\d+)/ -> destroy

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     # 问题1：考虑 GroupSerializer 能不能直接用？
    #     # ① 考虑序列化器类的字段是否满足需求？② 考虑字段的read_only和write_only设置是否正确？
    #     serializer = self.get_serializer(data=request.data)
    #     # 问题2：考虑是否需要补充验证？
    #     serializer.is_valid(raise_exception=True)
    #     # 问题3：考虑序列化器类中的create是否满足业务需要？
    #     serializer.save() # 调用序列化器类中的create
    #     return Response(serializer.data, status=201)

    def simple(self, request):
        """
        获取权限的简单数据：
        ① 查询所有权限的数据
        ② 将权限的数据序列化并返回
        """
        # ① 查询所有权限的数据
        perms = Permission.objects.all()

        # ② 将权限的数据序列化并返回
        serializer = PermSimpleSerializer(perms, many=True)
        return Response(serializer.data)


class AdminViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    queryset = User.objects.filter(is_staff=True)
    serializer_class = AdminSerializer

    # GET /meiduo_admin/permission/admins/ -> list
    # POST /meiduo_admin/permission/admins/ -> create
    # GET /meiduo_admin/permission/groups/simple/ -> simple

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     # 问题1：考虑 AdminSerializer 能不能直接用？
    #     # ① 考虑序列化器类的字段是否满足需求？② 考虑字段的read_only和write_only设置是否正确？
    #     serializer = self.get_serializer(data=request.data)
    #     # 问题2：考虑是否需要补充验证？
    #     serializer.is_valid(raise_exception=True)
    #     # 问题3：考虑序列化器类中的create是否满足业务需要？
    #     serializer.save() # 调用序列化器类中的create
    #     return Response(serializer.data, status=201)

    def simple(self, request):
        """
        获取用户组的简单数据：
        ① 查询数据库获取所有的用户组数据
        ② 将用户组数据序列化并返回
        """
        # ① 查询数据库获取所有的用户组数据
        groups = Group.objects.all()

        # ② 将用户组数据序列化并返回
        serializer = GroupSimpleSerializer(groups, many=True)
        return Response(serializer.data)


