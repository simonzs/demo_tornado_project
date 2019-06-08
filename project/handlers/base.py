import json
import tornado.web
from utils.session import Session

class BaseHandler(tornado.web.RequestHandler):
    """
        自定义的基类
    """
    @property
    def db(self):
        """
            作为RequestHandler对象的db属性
        """
        return self.application.db

    @property
    def redis(self):
        """
            做为RequestHandler对象的edis属性
        """    
        return self.application.redis

    def initialize(self, databse=None):
        """
            对应每个请求的处理类Handler在构造一个实例后首先执行initialize()方法,
            路由映射中的第三个字典型参数会作为该方法的命名参数传递,
            (r'/user/(.*)', ProfileHandler, dict(database=database))
        """
        print('initalize')
            
    def prepare(self):
        """
            预解析json数据
        """
        print('prepare')
        if self.request.headers.get('Content-Type', '').startswith('applicatiuons/json'):
            self.json_args = json.loads(self.request.body)  
        else:
            self.json_args = {}
    def get_current_user(self):
        """
            判断用户是否登录
        """
        self.session =Session(self)
        return self.session.data

    def set_default_headers(self):
        """
            设置请求头            
        """
        print('set_defualt_headers')
        # 设置get与post方式的默认响应格式为json
        self.set_header('Content-Type','application/json; charset=UTF-8')
        # 设置一个名为author, 值为simon的header
        self.set_header('author', 'simon')

    def finish_request(self, body):
        """
            将发送的body数据,转换成json格式
        """
        print('finish_request')
        self.write(json.dumps(body, sort_keys=True, separators=(',', ': ')))
        self.finish()

    def write_success_json(self, data=None):
        """
            信息发送成功后，添加描述信息
        """
        print('write_success_json')
        self.set_status(200)
        body = {'desc': 'success'}
        if data is not None:
            body['data'] = data
        return self.finish_request(body)

    def unauthorized(self):
        """
            用户没有登录,或者登录失败, 表示需要重新登录
        """
        print('unauthorized')
        self.send_error(status_code = 401, desc = 'user unauthorized, you need to login again')

    def access_failed(self):
        """
            已经有了用户信息， 发现该用户没有访问网页的权限
        """
        print('access_failed')
        self.send_error(403, desc = 'you do not have permission to access this page')

    def write_error(self, status_code, desc, reason=None):
        """
            在返回错误时, 也添加了错误的描述信息
        """
        print('write_error')
        if reason is None:
            self.set_status(status_code)
        else:
            self.set_status(status_code, reason=reason)
        self.finish_request({'desc': desc})

    def get(self):
        print('get')
        body = 'base get'
        self.write_success_json(body)

    def post(self):
        print('post')
        #self.redirect('/')
        self.unauthorized()

    def on_finish(self):
        print('on_finish')
