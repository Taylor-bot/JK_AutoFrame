import pytest

if __name__ == '__main__':
    pytest.main()

# pytest --collect-only：仅收集用例不执行，查看是否识别到测试项
# pytest -v：显示详细输出，观察文件加载过程

# pytest -s testcases\test_add_user.py --alluredir=report
# pytest .\test_storeGroup.py --alluredir=../../report
# --alluredir=report生成测试报告的目录

# 根据执行结果，生成测试报告，查看allure报告：
# allure generate report -o ../../report/api_report --clean
# --clean 选项表示在生成报告前先清空输出目录。

# 查看 Allure 报告
# allure open api_report

# 执行testcases里面所有的test
# pytest testcase --alluredir=allure-results
