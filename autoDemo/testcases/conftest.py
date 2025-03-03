import os
import json
import pytest
import yaml

from autoDemo.common.tools import sep, get_project_path
from autoDemo.common.login import login
from autoDemo.common.mysql_operate import mysql

currentPath = sep([get_project_path(),'testcases', 'storeGroup'])


@pytest.fixture(scope='session')
def token():
    global_token_path = None

    def _token(user):
        nonlocal global_token_path
        token_dir = sep([get_project_path(), 'token_dir'])
        if not os.path.exists(token_dir):
            os.mkdir(token_dir)

        # 生成用户对应的token文件
        token_path = sep([token_dir, user + '_token.json'])
        global_token_path = token_path
        if not os.path.exists(token_path):
            # token文件不存在的时候，需要去调用login登录
            token = login(user)
            # 写入token文件
            with open(token_path, 'w') as f:
                json.dump({'token': token}, f)
            return token
        else:
            with open(token_path, 'r') as f:
                token = json.load(f)
                # 如果token不为空的时候，返回token
                if token['token']:
                    return token['token']
                else:
                    token = login(user)
                    return token

    yield _token
    # 后置处理函数，保证每次请求后，删除token文件，但是可以不删除，yield后面的脚本可以注销
    # if os.path.exists(global_token_path):
    #     os.remove(global_token_path)


@pytest.fixture
def conn_database_fun():
    print(f'\n####init database')
    mysql.connect()

    yield mysql

    print(f'\n### close database')
    mysql.close()


@pytest.fixture(scope='function')
def writeTokenToYaml(request, token):
    # 使用request.param接收参数化传递的用例索引
    case_index = request.param
    with open(os.path.join(currentPath, 'findStoreGroup.yaml'), 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    # 替换authorization中的token
    token = token('laoShe')
    cases = data[case_index]
    cases['headers']["authorization"] = 'Bearer ' + token
    yield cases
    # 将替换后的数据写入yaml文件
    with open(os.path.join(currentPath, 'findStoreGroup.yaml'), 'w', encoding='utf-8') as f:
        # allow_unicode=True 参数的作用是让 yaml 库在写入文件时，以 Unicode 编码来处理字符串，这样中文字符就不会被转成 Unicode 转义序列。
        # sort_keys=False 参数是为了保持字典的键值对顺序和原始数据一致，如果不设置这个参数 默认情况下 yaml.dump() 会对字典的键进行排序。
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)


@pytest.fixture(scope='function')
def writeToken(request, token):
    filename = request.param["filename"]  # 动态获取文件名
    # 使用request.param接收参数化传递的用例索引
    case_index = request.param["index"]
    with open(os.path.join(currentPath, filename), 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    # 替换authorization中的token
    token = token('laoShe')
    cases = data[case_index]
    cases['headers']["authorization"] = 'Bearer ' + token
    yield cases

# 该错误是因为在测试代码中直接调用了名为 get_token 的 fixture 函数。在 pytest 中，fixture 是通过依赖注入的方式自动提供给测试函数的参数，不应该被直接调用
# 所以这里的写法不对，不能用main函数
