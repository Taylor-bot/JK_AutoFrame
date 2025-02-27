from autoDemo.common.yaml_config import GetConfig
from autoDemo.common.commom_requests import CommonRequests


def login(user):
    username, password, grantType, clientId = GetConfig().get_userinfo(user)
    header = {'Content-Type': 'application/json'}

    res = CommonRequests(headers=header).post_request_login(suffix_url='/login',
                                              json={'username': username, 'password': password,
                                                    'grantType': grantType, 'clientId': clientId}
                                              )

    return res.json()['data']['access_token']


if __name__ == '__main__':
    print(login('laoShe'))
