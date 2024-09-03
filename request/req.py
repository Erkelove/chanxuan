import json
import requests
from common import readdata, getPath
from common import logger

log = logger.logger

def send_request_from_yaml(filename, auth):
    """
    从YAML文件中读取测试用例并发送接口请求
    :param file_path: YAML文件路径
    """
    file_path = getPath.get_yaml_path(filename)
    test_cases = readdata.readYaml(file_path)
    for test_case in test_cases:
        test_case['request']['headers']['X-Authorization-Cx'] = f"{auth}"
        url = test_case['request']['url']
        log.info(url)
        method = test_case['request'].get('method', 'GET')
        log.info(method)
        params = test_case['request'].get('params', None)
        log.info(params)
        data = test_case['request'].get('data', None)
        data = json.dumps(data)
        log.info(data)
        headers = test_case['request'].get('headers', None)
        log.info(headers)
        response = send_request(url, method, params, data, headers)
        response = response.json()
        log.info(response)

def send_request(url, method='GET', params=None, data=None, headers=None):
    """
    发送接口请求的函数
    :param url: 请求的URL
    :param method: 请求方法，默认为GET
    :param params: URL参数
    :param data: 请求体数据
    :param headers: 请求头
    :return: 响应对象
    """
    method = method.upper()

    if method == 'GET':
        response = requests.get(url, params=params, headers=headers)
    elif method == 'POST':
        response = requests.post(url, data=data, headers=headers)
    elif method == 'PUT':
        response = requests.put(url, data=data, headers=headers)
    elif method == 'DELETE':
        response = requests.delete(url, params=params, headers=headers)
    else:
        raise ValueError("Unsupported HTTP method")

    return response

# 示例调用
# base_path = os.path.dirname(__file__)
# file_path = os.path.join(base_path, '../data/data.yaml')
# send_request_from_yaml(file_path)
# url = "https://cmm-cas-test.cds8.cn/v2/cas/authorize"
# data = {'device': 'PC', 'appId': 10007, 'grant_type': 'code', 'mobile': '18759738338', 'code': '888888'}
# data = json.dumps(data)
# response = requests.post(url, data=data)
# print(response.json())
