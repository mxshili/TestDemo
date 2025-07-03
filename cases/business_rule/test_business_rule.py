from libs.business_rule import business_rule

import pytest



class TestBusinessRule:

    name = '业务规则'

    @pytest.mark.parametrize('ruleName,minConsume,estimateConsume,measurement,measurePrice,description,types',[
        ('全国-电瓶车充电费率1','0.1','2','千瓦时','1','','1')
    ],scope='function')

    def test_business_rule1(self,ruleName,minConsume,estimateConsume,
                            measurement,measurePrice,description,types):

        business_rule.test_service_rule_type1(
            ruleName,minConsume,estimateConsume,measurement,
            measurePrice,description,types)


    @pytest.mark.parametrize('ruleName,minConsume,estimateConsume,description,types',[
        ('南京-洗车机费率1','2','10','','2')
    ],scope='function')

    def test_business_rule2(self,ruleName,minConsume,
                            estimateConsume,description,types):

        business_rule.test_service_rule_type2(
            ruleName,minConsume,estimateConsume,description,types)


    @pytest.mark.parametrize('ruleName,businesscode,measurement,measurePrice,description,types',[
            ('南京-存储柜费率1','业务码100L','小时','2','','3')
        ],scope='function')

    def test_business_rule3(self,ruleName,businesscode,measurement,
                            measurePrice,description,types):

        business_rule.test_service_rule_type3(
            ruleName,businesscode,measurement,measurePrice,description,types)






