from TestCase.pages.tuihuo_list import tuihuo_order_list


class Test_tuihuo:
    def test_tuihuo(self,base):
        base.driver.get("http://192.168.60.132/#/oms/returnApply")
        # 初始化退货列表页面
        tuihuo=tuihuo_order_list(base)
        # 点击退货申请处理
        tuihuo.click_shenqingchuli()
        #点击处理状态
        tuihuo.click_chulizhuangtai()
        # 点击待处理
        tuihuo.click_daichuli()
        # 点击查询搜索
        tuihuo.click_chaxunsousuo()




