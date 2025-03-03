import os.path

import allure
import pytest
import yaml

from autoDemo.common.commom_requests import CommonRequests


# 美化代码的快捷键 ctrl+alt+l

@allure.feature("采购管理-自动报货门店组")
class Test_storeGroup:
    @allure.title("查询自动报货门店组")
    @allure.description("测试查询门店组数量是否大于0")
    @pytest.mark.order(1)
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
        assert res.json()['data']['total'] > 0

    @allure.title("查询自动报货门店组")
    @allure.description("测试根据管理者查询是否成功")
    @pytest.mark.parametrize("writeTokenToYaml", [0,1], indirect=True)
    @pytest.mark.order(2)
    def test_findByStoreGroupByArgs(self, writeTokenToYaml):
        args = writeTokenToYaml
        # print(args)
        # deepseek YYDS
        res = CommonRequests(args["headers"]).post_request(args["url"], json=args["json"])
        assert res.json()['data']['total'] > 0 and res.json()['success'] is True

    # 测试用例有几个，index就是n-1！！！多了会报错
    @allure.title("新增自动报货门店组")
    @allure.description("测试新增根据区域是否成功")
    @pytest.mark.order(3)
    # @pytest.mark.skip
    @pytest.mark.parametrize("writeToken",
                             [
                                 {"filename": "addStoreGroup.yaml", "index": 0},
                                 # {"filename": "addStoreGroup.yaml", "index": 1}

                             ],
                             indirect=True)
    def test_addStoreGroup(self, writeToken):
        args = writeToken
        # print(args['json']['reportStoreGroupName'])
        res = CommonRequests(args['headers']).post_request(args['url'], json=args['json'])
        assert res.json()['success'] is True and res.json()['code'] == 200

    # 输出新增的报货门店组的id
    def findStoreGroupByName(self, token):
        absPath = os.path.dirname(__file__)
        # 写入token到findStoreGroupByName.yaml文件
        with open(os.path.join(absPath, 'findStoreGroupByName.yaml'), 'r', encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)

            data['headers']["authorization"] = 'Bearer ' + token('laoShe')
            # 读取addStoreGroup.yaml的reportStoreGroupName并写入到findStoreGroupByName.yaml文件
            with open(os.path.join(absPath, 'addStoreGroup.yaml'), 'r', encoding='utf-8') as f:
                addData = yaml.load(f, Loader=yaml.FullLoader)
                data['json']['reportStoreGroupName'] = addData[0]['json']['reportStoreGroupName']

            print(data)
            res = CommonRequests(data['headers']).post_request(data['url'], json=data['json'])
            return res.json()['data']['list'][0]['id']



    @allure.title("作废自动报货门店组")
    @allure.description("作废自动报货门店组是否成功")
    @pytest.mark.order(4)
    # @pytest.mark.skip
    def test_cancelStoreGroup(self, token):
        header = {"authorization": "Bearer " + token('laoShe'), 'client_id': 'yunchao_erp'}
        json = {
            "id": self.findStoreGroupByName(token)
        }
        res = CommonRequests(header).post_request('/supermarket-stock/api/v1/sm-erp/stock/cancellationReportStoreGroup', json=json)
        print(res.json())