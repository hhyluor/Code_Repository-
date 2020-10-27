from rest_framework import serializers
from goods.models import SKUImage, SKU


class SKUImageSerializer(serializers.ModelSerializer):
    """图片序列化器类"""
    sku_id = serializers.IntegerField(label='商品ID')

    # sku是一个关联对象，默认生成字段时使用的PrimaryKeyRelatedField
    # 此处不是要拿sku主键，希望拿到sku模型类的__str__方法的返回值
    # StringRelatedField：默认就是read_only=True
    sku = serializers.StringRelatedField(label='商品')

    class Meta:
        model = SKUImage
        fields = ('id', 'sku', 'sku_id', 'image')

    def validate_sku_id(self, value):
        """校验SKU商品是否存在"""
        try:
            sku = SKU.objects.get(id=value)
        except SKU.DoesNotExist:
            # 不存在
            raise serializers.ValidationError('SKU商品不存在')

        return value

    # 保存上传图片数据：
    # ModelSerializer create关键代码：SKUImage.objects.create(...)
    # SKU图片是有默认图片的，默认图片什么时候设置？就是在上传图片的时候设置
    # 因为ModelSerializer create没有默认图片设置的判断，所以此处需要重写create
    def create(self, validated_data):
        # ① 保存上传图片的数据：上传文件到FDFS和表的上传记录保存
        # 调用父类 ModelSerializer 中的create
        sku_image = super().create(validated_data)

        # ② 判断是否需要设置默认图片
        sku = sku_image.sku
        if not sku.default_image:
            # 设置默认图片
            sku.default_image = sku_image.image
            sku.save()

        return sku_image


class SKUSimpleSerializer(serializers.ModelSerializer):
    """SKU简单序列化器类"""
    class Meta:
        model = SKU
        fields = ('id', 'name')
