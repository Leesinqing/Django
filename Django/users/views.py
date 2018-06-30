from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from users.models import BookInfo
from django.urls import reverse
import json
from django.views.generic import View
from django.utils.decorators import method_decorator


# 创视图/定义路由/模板展示
def index(request):
    return HttpResponse("<h1 style='color:red'>hello Python!</h1>")


def show_book(request):
    # 查询数据库, 返回结果是查询集， 【】
    books = BookInfo.objects.all()
    contens = {"books": books}
    return render(request, 'index.html', context=contens)


def sq(request):
    print('重定向成功')
    return HttpResponse('Hello Python!')


def sq_say(request):
    # url = reverse('users:sq')
    # print(url)
    print(request.path)
    # return HttpResponse('say')
    return redirect(reverse('sq'))


def weather(request, year, city):
    print("数字为" + year)
    print("城市为" + city)
    return HttpResponse('OK')


def qs(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')

    print(a, b, alist)
    return HttpResponse('OK')


def get_body(request):
    # a = request.POST.get('a')
    # b = request.POST.get('b')
    # # alist = request.POST.getlist('a')
    #
    # print(a, b)
    json_file = request.body
    json_str = json_file.decode()
    print(type(json_str))
    print(json_str)
    req_data = json.loads(json_str)
    print(type(req_data))
    print(req_data)
    return HttpResponse('OK')


def resp_view(request):
    # return HttpResponse("itcast python", status=404)
    # response = HttpResponse('itcast python')
    # response.status_code = 400
    # response['Itcast'] = 'Python'
    # return response
    # 返回json数据
    # return JsonResponse({"city": "shenzheng"})
    # 重定向
    return redirect(reverse('users:sq'))


def cookie_session(request):
    # 设置cookie,需要通过HttpResponse对象中的set_cookie方法设置
    response = HttpResponse('OK')
    response.set_cookie('itcast', 'python')
    # 读取cookie
    print(request.COOKIES.get("itcast"))
    return response


def session(request):
    request.session['itcast'] = 'python'
    print(request.session.get('itcast'))
    return HttpResponse('OJBK')


# 函数视图
def register(request):
    """处理注册"""
    # 获取请求方法，判断是GET/POST请求
    if request.method == 'GET':
        # 处理GET请求
        return HttpResponse('GET请求')
    else:
        # 处理POST请求
        return HttpResponse('POST请求')


# 装饰器
def my_decorator(func):
    def wrapper(request, *args, **kwargs):
        print('装饰器被调用了')
        return func(request, *args, **kwargs)

    return wrapper


# @method_decorator(my_decorator)写在类方法上或者name=指明方法表示只装饰此方法，写在类上装饰全部方法需要name='dispatch'
# @method_decorator(my_decorator, name='dispatch')
# 类视图
class RegisterView(View):
    # 处理GET请求
    @method_decorator(my_decorator)
    def get(self, request):
        return HttpResponse('GET请求')

    # 处理POST请求
    @method_decorator(my_decorator)
    def post(self, request):
        return HttpResponse('POST请求')

    def put(self, request):
        print('put 方法')
        return HttpResponse('PUT请求')


# mixin扩展类
class ListModleMixin(object):
    def list(self, request, *args, **kwargs):
        print('成功调用list方法')


class CreateModelMinxin(object):
    def create(self, *args, **kwargs):
        print('成功调用create方法')


class BooksView(CreateModelMinxin, ListModleMixin, View):
    """同时继承两个扩展类，复用list和create方法"""
    def get(self, request):
        self.list(request)
        return HttpResponse('GET请求')

    def post(self, request):
        self.create(request)
        return HttpResponse('POST请求')
