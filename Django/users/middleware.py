# 定义中间件
def my_middleware(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次
    print('初始化调用1')

    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用
        print('每次请求前调用1')
        response = get_response(request)
        # 此处编写的代码会在每个请求处理视图之后被调用
        print('每次请求后调用1')
        return response

    return middleware


def my_middleware2(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次
    print('初始化调用2')

    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用
        print('每次请求前调用2')
        response = get_response(request)
        # 此处编写的代码会在每个请求处理视图之后被调用
        print('每次请求后调用2')
        return response

    return middleware


def my_middleware3(get_response):
    # 此处编写的代码仅在Django第一次配置和初始化的时候执行一次
    print('初始化调用3')

    def middleware(request):
        # 此处编写的代码会在每个请求处理视图前被调用
        print('每次请求前调用3')
        response = get_response(request)
        # 此处编写的代码会在每个请求处理视图之后被调用
        print('每次请求后调用3')
        return response

    return middleware
