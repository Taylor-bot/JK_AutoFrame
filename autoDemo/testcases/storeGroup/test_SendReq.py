import requests


class Test_send_request:
    session = requests.session()
    def test_start(self):
        url = 'http://47.107.116.139/phpwind/'

        # resp = Test_send_request.session.request('get', url)
        resp = self.session.get(url)

        print(resp.text)

    def test_connectMysql(self, conn_database_fun):
        mysql = conn_database_fun
        record = mysql.execute('select * from `order`limit 10')
        print(record)
