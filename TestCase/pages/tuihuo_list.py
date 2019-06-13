class tuihuo_order_list:
    def __init__(self,base):
        self.base = base

    # 退货列表超链接
    tuihuo_a="http://192.168.60.132/#/oms/returnApply"
    # 点击申请处理
    shenqingchuli='(//span[contains(text(),"申请处理")])[1]'
    # 点击处理状态
    chulizhuangtai='//label[contains(text(),"处理状态")]//following-sibling::div//input'
    # 点击待处理
    daichuli='//span[contains(text(),"待处理")]'
    # 点击查询搜索
    chaxunsousuo='//span[contains(text(),"查询搜索")]'
    # 点击查看详情
    chakanxiangqing='(//span[contains(text(),"查看详情")])[1]'
    # 滚动到底


    def click_tuihuo_a(self):
        self.base.click('退货列表超链接',self.tuihuo_a)
    def click_shenqingchuli(self):
        self.base.click('点击退货点击申请处理',self.shenqingchuli)
    def click_chulizhuangtai(self):
        self.base.click('点击处理状态',self.chulizhuangtai)
    def click_daichuli(self):
        self.base.click('点击待处理',self.daichuli)
    def click_chaxunsousuo(self):
        self.base.click('点击查询搜索',self.chaxunsousuo)
