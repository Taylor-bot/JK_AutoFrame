import requests
from requests.adapters import HTTPAdapter
from autoDemo.common.yaml_config import GetConfig
from autoDemo.common.deal_with_response import deal_with_response



class CommonRequests:
    def __init__(self, headers=None, timeout=10):
        # self.config = GetConfig()
        self.sess = requests.session()
        # 在session实例上挂载adapter实例，目的就是请求异常时，自动重试
        self.sess.mount('http://', HTTPAdapter(max_retries=3))
        self.sess.mount('https://', HTTPAdapter(max_retries=3))
        #忘记把headers放进session里面了！！
        self.sess.headers = headers
        self.timeout = timeout
        #调用获取yaml中的baseurl
        self.url = GetConfig().get_base_url()
        self.login_url = GetConfig().get_login_url()

    def get_request(self, suffifx_url, params=None):
        #Get方法的封装
        res = self.sess.get(url=self.url + suffifx_url, params=params, timeout=self.timeout)
        #调用处理接口报文的方法，将接口放进测试报告
        deal_with_response(params, res)
        return res


    def post_request(self, suffix_url, data=None, json=None):
        #post的封装
        if data:
            res = self.sess.post(url=self.url + suffix_url, data=data, timeout=self.timeout)
            deal_with_response(data, res)
            return res
        if json:
            res = self.sess.post(url=self.url + suffix_url, json=json, timeout=self.timeout)
            deal_with_response(json, res)
            return res

        res = self.sess.post(url=self.url + suffix_url, timeout=self.timeout)
        deal_with_response(None, res)
        return res

    def post_request_login(self, suffix_url, data=None, json=None):
        #post的封装
        if data:
            res = self.sess.post(url=self.login_url + suffix_url, data=data, timeout=self.timeout)
            deal_with_response(data, res)
            return res
        if json:
            res = self.sess.post(url=self.login_url + suffix_url, json=json, timeout=self.timeout)
            deal_with_response(json, res)
            return res

        res = self.sess.post(url=self.login_url + suffix_url, timeout=self.timeout)
        deal_with_response(None, res)
        return res
    #魔法函数
    def __del__(self):
        self.sess.close()


if __name__ == '__main__':
    get_res = CommonRequests().get_request('/get')
    post_res = CommonRequests().post_request('/post')
    print(get_res.text, '\n', post_res.text)