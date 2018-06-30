from django.conf.urls import url
from . import views
from users.views import my_decorator


# 定义路由
urlpatterns = [
    url(r'index/$', views.index),
    url(r'books/$', views.show_book),
    url(r'^sq/$', views.sq, name='sq'),
    url(r'^sq_say/$', views.sq_say, name='sq_say'),
    url(r'^weather/(?P<yaer>[a-z]+)/(?P<city>\d+)/$', views.weather),
    url(r'^qs/$', views.qs),
    url(r'^get_body/$', views.get_body),
    url(r'^resp/$', views.resp_view),
    url(r'^cs/$', views.cookie_session),
    url(r'^se/$', views.session),
    url(r'^register/$', views.register),
    # 耦合度太低,一个功能的实现没有在一个.py文件里,只看views不知道使用了装饰器
    # 在视图入口，分发请求之前添加装饰器，实现为类视图的所有请求方法加上装饰器，但不能实现只对特定方法添加
    # url(r'reg/$', my_decorator(views.RegisterView.as_view())),
    url(r'reg/$', views.RegisterView.as_view()),
    url(r'bookview/$', views.BooksView.as_view()),
]
