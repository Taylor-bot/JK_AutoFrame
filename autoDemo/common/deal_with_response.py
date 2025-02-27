import allure

def deal_with_response(data, res):

    request_url = str(res.request.url)
    allure.attach(name='请求地址', body=request_url)

    request_method= str(res.request.method)
    allure.attach(name='请求方法', body=request_method)

    request_headers = str(res.request.headers)
    allure.attach(name='请求头', body=request_headers)

    request_data = str(data)
    allure.attach(name='请求参数', body=request_data)

    response_time = str(res.elapsed.total_seconds()*1000)
    allure.attach(name='响应时间', body=response_time)

    status_code = str(res.status_code)
    allure.attach(name='状态码', body=status_code)

    response_text = str(res.text)
    allure.attach(name='响应结果', body=response_text)
