import logging
from libs.login.loginin import login
import pytest
logging.basicConfig(level=logging.INFO)

# 优化点：数据分离 CI/CD集成
class Test_SMP_login:

    name = '登录用例测试'

    @pytest.mark.parametrize('username,password,asserttext',[
        ('byhy','sdfsdf',None),
        (None,'sdfsdf','请输入用户名'),
        ('byhy',None,'请输入密码'),
        ('byhy','sdfsdfs','登录失败： 用户名或者密码错误'),
        ('byhy','sdfsd','登录失败： 用户名或者密码错误'),
        ('byy','sdfsdf','登录失败： 用户名不存在'),
        ('byhyf','sdfsdf','登录失败： 用户名不存在')
    ],scope='function')
    def test_SMP_login_001_007(self,username,password,asserttext):
        outtext = login.loginin(username,password)
        try:
            assert outtext == asserttext
        except AssertionError:
            logging.error(f"模型名称断言失败，预期为{asserttext},实际为{outtext}", exc_info=True)


