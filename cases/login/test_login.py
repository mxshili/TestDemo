from libs.login.loginin import login
import pytest


class Test_SMPlogin:

    name = '登录用例测试'

    @pytest.mark.parametrize('username,password,asserttext',[
        ('byhy','sdfsdf',None),
        (None,'sdfsdf','请输入用户名'),
        ('byhy',None,'请输入密码'),
        ('byhy','sdfsdfs','登录失败： 用户名或密码错误'),
        ('byhy','sdfsd','登录失败： 用户名或密码错误'),
        ('byy','sdfsdf','登录失败： 用户名不存在'),
        ('byhyf','sdfsdf','登录失败： 用户名不存在')
    ])
    def test_SMP_login_001_007(self,username,password,asserttext):
        outtext = login.loginin(username,password)
        if outtext is None:
            assert 1==1
        else:
            assert outtext == asserttext


