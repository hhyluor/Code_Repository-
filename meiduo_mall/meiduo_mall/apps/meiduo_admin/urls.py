from django.urls import re_path
from meiduo_admin.views import users, statistical, skus, permissions

urlpatterns = [
    re_path(r'^authorizations/$', users.AdminAuthView.as_view()),
    # 数据统计
    re_path(r'^statistical/day_active/$', statistical.UserDayActiveCountView.as_view()),
    re_path(r'^statistical/day_orders/$', statistical.UserDayOrdersCountView.as_view()),
    re_path(r'^statistical/month_increment/$', statistical.UserMonthIncrementView.as_view()),
    # 普通用户管理
    re_path(r'^users/$', users.UserInfoView.as_view()),

    # 图片数据管理
    # re_path(r'^skus/images/$', skus.SKUImageViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # })),
    # re_path(r'^skus/images/(?P<pk>\d+)/$', skus.SKUImageViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),
    re_path(r'^skus/simple/$', skus.SKUSimpleView.as_view()),

    # 权限数据管理
    # re_path(r'^permission/perms/$', permissions.PermissionViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # })),
    # re_path(r'^permission/perms/(?P<pk>\d+)/$', permissions.PermissionViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),
    re_path(r'^permission/content_types/$', permissions.ContentTypeView.as_view()),

    # 用户组管理
    # re_path(r'^permission/groups/$', permissions.GroupViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # })),
    # re_path(r'^permission/groups/(?P<pk>\d+)/$', permissions.GroupViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),
    re_path(r'^permission/simple/$', permissions.GroupViewSet.as_view({
        'get': 'simple'
    })),

    # 管理员管理
    re_path(r'^permission/admins/$', permissions.AdminViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    re_path(r'^permission/admins/(?P<pk>\d+)/$', permissions.AdminViewSet.as_view({
        'get': 'retrieve',
        'put':'update',
    })),

    re_path(r'^permission/groups/simple/$', permissions.AdminViewSet.as_view({
        'get': 'simple'
    }))
]

# 路由Router: 自动生成视图集中API接口的url配置项
# 图片数据管理
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('skus/images', skus.SKUImageViewSet, basename='images')
urlpatterns += router.urls

# 权限数据管理
router = SimpleRouter()
router.register('permission/perms', permissions.PermissionViewSet, basename='perms')
urlpatterns += router.urls

# 用户组数据管理
router = SimpleRouter()
router.register('permission/groups', permissions.GroupViewSet, basename='groups')
urlpatterns += router.urls

for url in router.urls:
    print(url)
