import os
import json
import pytest

from autoDemo.common.tools import sep, get_project_path
from autoDemo.common.login import login
from autoDemo.common.mysql_operate import mysql

@pytest.fixture
def token():
    def _token(user):
        token_dir = sep([get_project_path(), 'token_dir'])
        if not os.path.exists(token_dir):
            os.mkdir(token_dir)

        # 生成用户对应的token文件
        token_path = sep([token_dir, user + '_token.json'])
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
                return token['token']

    return _token


@pytest.fixture
def conn_database_fun():
    print(f'\n####init database')
    mysql.connect()

    yield mysql

    print(f'\n### close database')
    mysql.close()


# 该错误是因为在测试代码中直接调用了名为 get_token 的 fixture 函数。在 pytest 中，fixture 是通过依赖注入的方式自动提供给测试函数的参数，不应该被直接调用
# 所以这里的写法不对，不能用main函数
if __name__ == '__main__':
    print(token())
