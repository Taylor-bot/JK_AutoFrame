import allure
import requests

from autoDemo.common.commom_requests import CommonRequests


# 美化代码的快捷键 ctrl+alt+l
@allure.description("自动报货门店组查询接口")
@allure.feature("采购管理")
class Test_storeGroup:

    @allure.tag("查询")
    def test_findStoreGroup(self, token):
        header = {"authorization": "Bearer " + token('laoShe'), 'client_id': 'yunchao_erp'}
        # ：例如，\s 在正则表达式中表示空白字符，但在普通字符串中需要写成 \\s，而使用 r 前缀后可以直接写成 \s。
        # ：^ 是正则表达式的元字符，表示匹配字符串的开头位置。
        json = {
            "pageSize": 10,
            "pageNum": 1,
            "storeCodes": []
        }
        res = CommonRequests(header).post_request('/supermarket-stock/api/v1/sm-erp/stock/reportStoreGroupPageInfo',
                                                  json=json)
        print(res.json())
