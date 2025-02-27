import yaml
from autoDemo.common.tools import get_project_path, sep


class GetConfig:

    # 使用构造函数，初始化yaml文件，把yaml读取出来
    def __init__(self):
        project_path = get_project_path()
        with open(project_path + sep(['config', 'environment.yaml'], add_sep_before=True), 'r',
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)

    def get_userinfo(self, username):
        return self.env['user'][username]['username'], self.env['user'][username]['password'], self.env['user'][username]['grantType'], self.env['user'][username]['clientId']

    def get_base_url(self):
        return self.env['base_url']

    def get_login_url(self):
        return self.env['login_url']

    def get_mysql_config(self):
        return self.env['mysql']


if __name__ == '__main__':
    myConfig = GetConfig()
    print(myConfig.get_userinfo('laoShe'))
