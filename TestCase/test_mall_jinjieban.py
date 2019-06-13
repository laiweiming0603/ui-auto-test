from time import sleep

import pytest

class Test_mall:
    @pytest.mark.fahuo
    def test_fahuo(self,base):
        base.driver.get("http://192.168.60.132/#/oms/order")
        #点击订单状态
        base.click('点击订单状态', '//label[contains(text(),"订单状态")]/following-sibling::div//input')
        #选择待发货
        base.click('点击待发货','//span[contains(text(),"待发货")]')
        #点击查询
        base.click('点击查询搜索','//span[contains(text(),"查询搜索")]')
        #点击第一条订单的订单发货
        base.click('点击第一条订单发货','(//span[contains(text(),"订单发货")])[1]')
        #断言
        assert '发货列表' in base.driver.page_source
        #点击物流公司
        base.click('点击物流公司','//input[@placeholder="请选择物流公司"]')
        #选择顺丰快递
        base.click('选择顺丰快递','//span[contains(text(),"顺丰")]')
        #输入物流单号
        base.send_keys('输入快递单号','(//input[@type="text"])[2]','123456')
        #点击确定
        base.click('点击确定','(//span[contains(text(),"确定")])[1]')
        #点击确定
        base.click('点击确定', '(//span[contains(text(),"确定")])[2]')
        #获取提示文本
        text = base.get_text('获取提示文本', '//div[@role="alert"]//p')
        # 断言
        assert '发货成功' in text

    @pytest.mark.tuihuo
    def test_th(self,base):
        base.driver.get("http://192.168.60.132/#/oms/returnApply")
        #点击退货申请处理
        base.click('点击退货申请处理', '(//span[contains(text(),"申请处理")])[1]')
        #点击处理状态
        base.click('点击处理状态', '//label[contains(text(),"处理状态")]//following-sibling::div//input')
        #点击待处理
        base.click('点击待处理','//span[contains(text(),"待处理")]')
        #点击查询搜索
        base.click('点击查询搜索', '//span[contains(text(),"查询搜索")]')
        #点击查看详情
        base.click('点击查看详情', '(//span[contains(text(),"查看详情")])[1]')
        #滚动到底
        base.scroll_screen('滚动到底')
        #获取订单金额
        text = base.get_text('获取订单金额', '//div[contains(text(),"订单金额")]/following-sibling::div')
        text=text[1:]
        #输入获取金额
        base.send_keys('输入退款金额','//div[contains(text(),"退款金额")]/following-sibling::div//input',str(text))
        #点击确认退货
        base.click('点击确认退货','//span[contains(text(),"确认退货")]')
        #点击确定
        base.click('点击确定','//span[contains(text(),"确定")]')
        #获取提示文本
        get_text = base.get_text('获取提示文本', '//div[@role="alert"]//p')
        print(get_text)
        #断言
        assert '操作成功'in get_text
        sleep(5)
