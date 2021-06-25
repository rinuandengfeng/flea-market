class Scope:
    allow_api = ()     # 允许访问的视图函数
    allow_module = ()  # 允许访问的模块名
    forbidden = ()     # 禁止访问的视图函数

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_module = self.allow_module + other.allow_module
        self.forbidden = self.forbidden + other.forbidden
        # self.forbidden = self.forbidden + other.forbidden
        # self.allow_api = list(set(self.allow_api))  # 去重 allow_api再相加的时候会有重复，debug可以看到
        return self


class UserScope(Scope):
    allow_api = ('test_db.test',)
    allow_module = ('admin', 'data')
    forbidden = ()


class AdminScope(Scope):
    allow_api = ()
    allow_module = ('admin', 'data')

    def __init__(self):
        self + UserScope()


class SuperAdminScope(Scope):
    allow_api = ()
    allow_module = ('admin', 'data')

    def __init__(self):
         self + UserScope() + AdminScope()


def is_in_scope(scope, endpoint, module_name):
    scope = globals()[scope]()
    # if endpoint in scope.forbidden:
    #     return False
    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if module_name in scope.allow_module:
        return True
    else:
        return False
