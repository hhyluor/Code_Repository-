from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser

from django.utils import timezone

from users.models import User


# GET /meiduo_admin/statistical/day_active/
class UserDayActiveCountView(APIView):
    # 仅管理员才能访问此接口
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        统计当日的获取用户数量：
        ① 查询数据库统计当日的活跃用户数量
        ② 返回响应数据
        """
        # ① 查询数据库统计当日的活跃用户数量
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        count = User.objects.filter(last_login__gte=now_date).count()

        # ② 返回响应数据
        response_data = {
            'count': count,
            'date': now_date.date() # date只取年-月-日
        }
        return Response(response_data)


# GET /meiduo_admin/statistical/day_orders/
class UserDayOrdersCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        统计当天的下单用户数量：
        ① 查询数据库统计当天的下单用户数量
        ② 返回响应的数据
        """
        # ① 查询数据库统计当天的下单用户数量
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        # 关联查询
        count = User.objects.filter(orders__create_time__gte=now_date).distinct().count()

        # ② 返回响应的数据
        response_data = {
            'count': count,
            'date': now_date.date() # date只取年-月-日
        }
        return Response(response_data)


# GET /meiduo_admin/statistical/month_increment/
class UserMonthIncrementView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        统计最近30天每天新增用户的数量：
        ① 查询数据库统计最近30天每天新增用户的数量
        ② 返回响应数据
        """
        # ① 查询数据库统计最近30天每天新增用户的数量
        # 结束时间
        end_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        # 起始时间：end_date - 29天
        begin_date = end_date - timezone.timedelta(days=29)

        cur_date = begin_date

        month_li = []

        while cur_date <= end_date:
            # cur_date 下一天的时间
            next_date = cur_date + timezone.timedelta(days=1)

            # 统计 cur_date 这一天新增用户数量
            count = User.objects.filter(date_joined__gte=cur_date,
                                        date_joined__lt=next_date).count()

            # 保存数据
            month_li.append({
                'count': count,
                'date': cur_date.date()
            })

            # cur_date 向后加 1 天
            cur_date = next_date

        # ② 返回响应数据
        return Response(month_li)
