import unittest
import ddt
import common.commons as common
from base.configHttp import Base

r = common.Common().ReadExcelTypeDict('cezxhi .xlsx')  # 拿到具体的Excel表数据
@ddt.ddt  #导入ddt模块
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:  # setupclass类方法  全部用例开始前执行一次
        cls.logs = common.Common().get_logs() # 导入日志方法
        cls.logs.debug('开始写入接口自动化测试用例')
    @classmethod
    def tearDownClass(cls) -> None:
        cls.logs.debug('自动化接口用例结束')

    def setUp(self) -> None:
        self.logs.debug('开始本条接口用例')

    def tearDown(self) -> None:
        self.logs.debug('结束本条用例')

    @ddt.data(*r) #  引入ddt模块，读取拿到的数据
    def test_logins(self,pars):  # 用例方法名开头必须已test  pars参数为接收的表数据值
        import json  #导入json模块
        dic = json.loads(pars['body参数值'])  # 将Excel数据中的参数值转变为json格式
        url = pars['接口地址']  # 拿到请求url
        yuqi = pars['预期结果']  # 拿到预期结果
        fs = pars['请求方式'] # 拿到请求方式
        result = Base().requests_type(method = fs,url = url,data = dic)  # 填充base页的请求api
        self.assertEqual(result.text, yuqi)  # 进行断言 看用例是否通过


if __name__ == '__main__':
    load = unittest.TestLoader().loadTestsFromTestCase(TestLogin)  #使用loader加载方式 来找寻所有已test开头的用例
    suite = unittest.TestSuite([load,])

    common.Common().GetHtmlResult(suite,'登录测试用例')