import pytest

from libs.machine import machine_update


class TestMachine:

    name = '设备型号管理'

    @pytest.mark.parametrize('model,description,types',[
        ('elife-canbinlocker-g22-10-20-40','南京e生活存储柜-10大20中40小','存储柜'),
        ('萨达范德萨分开附件砥砺奋进看见网络机房份额阿斯蒂芬较大司法局阿德杀戮空间大飞机啊塞德里克就阿斯利康大家所带来的科技收到就发了受打击了圣诞快乐士大夫胜多负少大富豪大数据开发收款单号发我额发货萨达范德萨的','南京e生活存储柜-10大20中40小','存储柜'),
        ('bokpower-charger-g22-220v450w','杭州bok 2022款450瓦 电瓶车充电站','电瓶车充电站'),
        ('njcw-carwasher-g22-2s','南京e生活2022款洗车机 2个洗车位','洗车站'),
        ('yixun-charger-g22-220v7kw','南京易迅能源2022款7千瓦汽车充电站','汽车充电站'),
    ],scope='function')

    def test_SMP_device_model_add_001_301(self,model,description,types):
        machine_update.machine.machine_add(model, description, types)


    @pytest.mark.parametrize('modeltext,description',[
        ('bokpower-charger-g22-220v440w','大连bok 2022款450瓦 电瓶车充电站')
    ],scope='function')
    def test_SMP_device_model_change_501(self,modeltext,description):
        machine_update.machine.machine_change(description)


    def test_SMP_device_model_delete_601(self):
        machine_update.machine.machine_delete()





