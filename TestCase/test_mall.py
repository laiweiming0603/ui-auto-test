from time import sleep

from Common.Baseui import baseUI




class Test_mall:
    def test_login(self, driver):
        #使用baseUI
        base = baseUI(driver)
        #打开登录页面
        driver.get('http://192.168.60.132/#/login')
        #输入用户名
        base.send_keys('输入用户名','//input[@name="username"]','admin')
        # 密码
        base.send_keys('输入密码','//input[@name="password"]','123456')
        # 点击登录
        base.click('点击登录','//span[contains(text(),"登录")]')
        assert '首页' in driver.page_source
        sleep(3)

    def test_fahuo(self,driver):
        #点击订单
        base = baseUI(driver)
        base.click('点击订单','(//span[contains(text(),"订单")])[1]')
        #点击订单列表
        base.click('点击订单列表','//span[contains(text(),"订单列表")]')
        #点击订单状态
        base.click('点击订单状态', '//label[contains(text(),"订单状态")]/following-sibling::div//input')
        #选择待发货
        base.click('点击待发货','//span[contains(text(),"待发货")]')
        #点击查询
        base.click('点击查询搜索','//span[contains(text(),"查询搜索")]')
        #点击第一条订单的订单发货
        base.click('点击第一条订单发货','(//span[contains(text(),"订单发货")])[1]')
        #断言
        assert '发货列表' in driver.page_source
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
        text = base.get_text('获取提示文本', '//div[@aria-label="提示"]/following-sibling::div//p')
        # 断言
        assert text in driver.page_source
        sleep(5)
    # def test_th(self,driver):
    #     # 点击订单
    #     base = baseUI(driver)
    #     base.click('点击订单', '//span[contains(text(),"订单")]')
    #     #点击退货原因设置
    #     base.click('点击退货原因设置', '//span[contains(text(),"原因设置")]')
    #     #点击删除第一条退货原因
    #
    #     #点击添加退货原因
    #     #输入原因类型
    #     #点击确定
