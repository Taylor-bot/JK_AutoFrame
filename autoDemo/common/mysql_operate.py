import pymysql
from autoDemo.common.yaml_config import GetConfig


class MysqlOperate:
    def __init__(self):
        mysql_config = GetConfig().get_mysql_config()
        self.host = mysql_config['host']
        self.db = mysql_config['db']
        self.port = mysql_config['port']
        self.user = mysql_config['user']
        self.password = mysql_config['password']
        self.conn = None
        self.cursor = None

    # 建立数据库连接
    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host, db=self.db, port=self.port, user=self.user,
                                        password=self.password,
                                        charset='utf8')
        except Exception as e:
            print(e)
            return False

        self.cur = self.conn.cursor()
        return True

    # 关闭数据库
    def close(self):
        self.cur.close()
        self.conn.close()
        return True

    # 增、删、改需要commit
    def commit(self):
        self.conn.commit()
        return True

    def execute(self, sql):
        # 建立连接
        self.connect()
        self.cur.execute(sql)
        queryData = self.cur.fetchall()

        if queryData == ():
            queryData = None
            print("没有获取到任何数据")
        else:
            pass
        return queryData

    # 插入数据
    def insertData(self):
        # 暂时不写，用不到
        pass


mysql = MysqlOperate()

# 测试是否可以连通
if __name__ == '__main__':
    mysql.connect()
    # sql = "select * from `order` limit 10"
    # fetchData= mysql.execute(sql)
    # print(fetchData)
    a = [1, 2, 3]
    print(a)
