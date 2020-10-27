from django.core.files.storage import Storage, FileSystemStorage
# 先导入我们安装的 fdfs_client.client 客户端
from fdfs_client.client import Fdfs_client
# 导入 settings 文件
from django.conf import settings
from rest_framework.exceptions import APIException


class FastDFSStorage(Storage):
    """自定义的文件存储类"""

    # 我们再添加一个新的方法
    # 该方法会在我们上传之前,判断文件名称是否冲突
    def exists(self, name):
        # 根据上面的图片我们可知,
        # fdfs 中的文件名是由 fdfs 生成的, 所以不可能冲突
        # 我们返回 False: 永不冲突
        return False

    def _save(self, name, content):
        """
        name：上传文件的名称
        content：文件对象，可以 `文件对象.read()` 获取上传文件的内容
        """
        client = Fdfs_client(settings.FDFS_CLIENT_CONF)

        # 上传文件
        res = client.upload_by_buffer(content.read())

        # 判断上传是否成功
        if res.get('Status') != 'Upload successed.':
            raise APIException('上传文件到FDFS失败')

        # 返回文件id
        file_id = res.get('Remote file_id')
        return file_id

    # 返回可访问到文件的完整的url地址
    # 我们知道, 保存成功后, 返回的图片是不完整的, 所以在这里拼接完整.
    def url(self, name):
        return settings.FDFS_URL + name
