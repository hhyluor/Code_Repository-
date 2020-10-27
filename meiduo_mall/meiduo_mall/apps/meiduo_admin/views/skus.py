from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SKUImage, SKU
from meiduo_admin.serializers.skus import SKUImageSerializer, SKUSimpleSerializer


class SKUImageViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    queryset = SKUImage.objects.all()
    serializer_class = SKUImageSerializer

    lookup_value_regex = '\d+'

    # GET /meiduo_admin/skus/images/ -> list
    # POST /meiduo_admin/skus/images/ -> create
    # GET /meiduo_admin/skus/images/(?P<pk>\d+)/ -> retrieve
    # PUT /meiduo_admin/skus/images/(?P<pk>\d+)/ -> update
    # DELETE /meiduo_admin/skus/images/(?P<pk>\d+)/ -> destroy

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #     # 问题1：考虑 SKUImageSerializer 能不能直接用？
    #     # ① 考虑序列化器类的字段是否满足需求？② 考虑字段的read_only和write_only设置是否正确？
    #     serializer = self.get_serializer(data=request.data)
    #     # 问题2：考虑是否需要补充验证？validate_<fieldname>：validate_sku_id
    #     serializer.is_valid(raise_exception=True)
    #     # 问题3：考虑序列化器类中的create是否满足业务需要？
    #     serializer.save() # 调用序列化器类中的create
    #     return Response(serializer.data, status=201)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save() # 调用序列化器类中的update
    #     return Response(serializer.data)

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete() # 思考题：除了删除表中的数据，FDFS中对应的文件是否会被删除？？？
    #     return Response(status=204)


# GET /meiduo_admin/skus/simple/
class SKUSimpleView(ListAPIView):
    permission_classes = [IsAdminUser]

    queryset = SKU.objects.all()
    serializer_class = SKUSimpleSerializer

    # 关闭分页
    pagination_class = None
