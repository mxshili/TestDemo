import pytest

from libs.device import device


class TestDevice:

    name = '设备添加'

    @pytest.mark.parametrize('types,modeltypes,ruletypes,machinenumber,description',
        [('1','69','57','sldkdjf','dsasfdsf'),
         ('2','67','56','sldkdj','dsasfds'),
         ('3','68','55','sldkd','dsasfd')
    ],scope='function')

    def test_device_001_301(self,types,modeltypes,ruletypes,machinenumber,description):

        device.device.testdevice(types,modeltypes,ruletypes,machinenumber,description)