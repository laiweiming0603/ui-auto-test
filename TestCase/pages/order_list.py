

class order_list:
    def __init__(self,base):
        self.base = base
    #订单列表超链接
    order_list_a="http://192.168.60.132/#/oms/order"
    #订单状态下拉框
    order_status_a='//label[contains(text(),"订单状态")]/following-sibling::div//input'
    #选择待发货
    to_be_deliverd='//span[contains(text(),"待发货")]'
    #查询搜索按钮
    chaxunsousuo='//span[contains(text(),"查询搜索")]'
    #订单发货
    fahuo='(//span[contains(text(),"订单发货")])[1]'
    def click_order_list_a(self):
        self.base.click('点击订单列表超链接',self.order_list_a)
    def click_order_status_a(self):
        self.base.click('点击订单状态下拉框',self.order_status_a)
    def click_to_be_deliverd(self):
        self.base.click('点击待发货',self.to_be_deliverd)
    def click_chaxunsousuo(self):
        self.base.click('点击查询搜索按钮',self.chaxunsousuo)
    def click_fahuo(self):
        self.base.click('点击订单发货',self.fahuo)