import yaml

common_json = {"interface": "XX接口",
               "name": "XX用例",
               "url": "/XX",
               "headers": {
                   "authorization": "{token}",
                   "client_id": "yunchao_erp"
               },
               "json":None}

# 原始的 JSON 数据
json_data = {
    "id": "null",
    "storeCirclingType": "1",
    "model": "1",
    "adminUsers": [
        {
            "adminUserId": "1784108031949144064",
            "adminUserPhone": "18275887305",
            "adminUserName": "张太娈"
        }
    ],
    "reportStoreGroupName": "测试自动化",
    "storeCodes": [
        {
            "id": "9a162ce5d1114bc4aed59da4b4d2dabc",
            "name": "石家庄",
            "pid": "95c2a9461e104581953f08738f19c0b4",
            "level": "2",
            "storeSize": None,
            "disableCheckbox": False
        },
        {
            "id": "MD853124",
            "name": "数据中心pda看板-测试门店-2号店",
            "pid": "9a162ce5d1114bc4aed59da4b4d2dabc",
            "level": "3",
            "storeSize": None,
            "disableCheckbox": False
        },
        {
            "id": "MD601025",
            "name": "多单位2",
            "pid": "9a162ce5d1114bc4aed59da4b4d2dabc",
            "level": "3",
            "storeSize": None,
            "disableCheckbox": False
        },
        {
            "id": "MD784502",
            "name": "测试4",
            "pid": "9a162ce5d1114bc4aed59da4b4d2dabc",
            "level": "3",
            "storeSize": None,
            "disableCheckbox": False
        },
        {
            "id": "MD067174",
            "name": "阿瑟大法官",
            "pid": "9a162ce5d1114bc4aed59da4b4d2dabc",
            "level": "3",
            "storeSize": None,
            "disableCheckbox": False
        },
        {
            "id": "MD650580",
            "name": "青源堂",
            "pid": "9a162ce5d1114bc4aed59da4b4d2dabc",
            "level": "3",
            "storeSize": None,
            "disableCheckbox": False
        },
        {
            "id": "95c2a9461e104581953f08738f19c0b4",
            "name": "河北省",
            "pid": "0",
            "level": "1",
            "storeSize": None,
            "disableCheckbox": False,
            "label": "河北省",
            "title": "河北省",
            "key": "95c2a9461e104581953f08738f19c0b4",
            "children": [
                {
                    "id": "9a162ce5d1114bc4aed59da4b4d2dabc",
                    "name": "石家庄",
                    "pid": "95c2a9461e104581953f08738f19c0b4",
                    "level": "2",
                    "storeSize": None,
                    "disableCheckbox": False,
                    "label": "石家庄",
                    "title": "石家庄",
                    "key": "9a162ce5d1114bc4aed59da4b4d2dabc",
                    "children": [
                        {
                            "id": "MD853124",
                            "name": "数据中心pda看板-测试门店-2号店",
                            "pid": "9a162ce5d1114bc4aed59da4b4d2dabc",
                            "level": "3",
                            "storeSize": None,
                            "disableCheckbox": False,
                            "label": "数据中心pda看板-测试门店-2号店",
                            "title": "数据中心pda看板-测试门店-2号店",
                            "key": "MD853124",
                            "children": []
                        },
                        {
                            "id": "MD601025",
                            "name": "多单位2",
                            "pid": "9a162ce5d1114bc4aed59da4b4d2dabc",
                            "level": "3",
                            "storeSize": None,
                            "disableCheckbox": False,
                            "label": "多单位2",
                            "title": "多单位2",
                            "key": "MD601025",
                            "children": []
                        },
                        {
                            "id": "MD784502",
                            "name": "测试4",
                            "pid": "9a162ce5d1114bc4aed59da4b4d2dabc",
                            "level": "3",
                            "storeSize": None,
                            "disableCheckbox": False,
                            "label": "测试4",
                            "title": "测试4",
                            "key": "MD784502",
                            "children": []
                        },
                        {
                            "id": "MD067174",
                            "name": "阿瑟大法官",
                            "pid": "9a162ce5d1114bc4aed59da4b4d2dabc",
                            "level": "3",
                            "storeSize": None,
                            "disableCheckbox": False,
                            "label": "阿瑟大法官",
                            "title": "阿瑟大法官",
                            "key": "MD067174",
                            "children": []
                        },
                        {
                            "id": "MD650580",
                            "name": "青源堂",
                            "pid": "9a162ce5d1114bc4aed59da4b4d2dabc",
                            "level": "3",
                            "storeSize": None,
                            "disableCheckbox": False,
                            "label": "青源堂",
                            "title": "青源堂",
                            "key": "MD650580",
                            "children": []
                        }
                    ]
                }
            ]
        }
    ]
}

common_json["json"] = json_data
# 将 JSON 数据转换为 YAML 格式
yaml_data = yaml.dump(common_json, allow_unicode=True, sort_keys=False)

# 打印转换后的 YAML 数据
# print(yaml_data)

# 将yaml_data写入yaml文件
with open('../testcases/storeGroup/addStoreGroup.yaml', 'w', encoding='utf-8') as file:
    file.write(yaml_data)
