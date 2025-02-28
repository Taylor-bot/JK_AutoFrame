import allure
import pytest

from autoDemo.common.commom_requests import CommonRequests


# 美化代码的快捷键 ctrl+alt+l

@allure.feature("采购管理-自动报货门店组")
class Test_storeGroup:

    @allure.title("查询自动报货门店组")
    @allure.description("测试查询门店组数量是否大于0")
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
        # print(res.json())
        assert res.json()['data']['total'] > 0

    @allure.title("查询自动报货门店组")
    @allure.description("测试根据管理者查询是否成功")
    @pytest.mark.parametrize("writeTokenToYaml", [0,1], indirect=True)
    def test_findByManager(self, writeTokenToYaml):
        args = writeTokenToYaml
        # print(args)
        # deepseek YYDS
        res = CommonRequests(args["headers"]).post_request(args["url"], json=args["json"])
        assert res.json()['data']['total'] > 0 and res.json()['success'] is True




