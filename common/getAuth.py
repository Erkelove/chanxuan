from request import req
from common import readdata, getPath
from jsonpath_ng import parse
import json

file_path = getPath.get_yaml_path('token.yaml')
token_data = readdata.readYaml(file_path)

def extract_value(response_body, jsonpath_expr):
    matches = [match.value for match in jsonpath_expr.find(response_body)]
    if matches:
        return matches[0]
    return None
def getToken():
    url = token_data[0]['request']['url']
    method = token_data[0]['request']['method']
    data = token_data[0]['request']['data']
    data =json.dumps(data)
    res_data = req.send_request(url, method=method, data=data)
    res_data = res_data.json()
    jsonpath_expr = parse(token_data[0]['extract']['token'])
    token = extract_value(res_data, jsonpath_expr)
    assert token is not None, "Token extraction failed"
    print(f"Extracted token: {token}")
    return token

def createAuth():
    token = getToken()
    token_data[1]['request']['data']['token'] = f"{token}"
    url = token_data[1]['request']['url']
    method = token_data[1]['request']['method']
    data = token_data[1]['request']['data']
    print(data)
    data = json.dumps(data)
    res_data = req.send_request(url, method=method, data=data)
    res_data = res_data.json()
    print(res_data)
    jsonpath_expr = parse(token_data[1]['extract']['auth'])
    auth = extract_value(res_data, jsonpath_expr)
    assert auth is not None, "auth extraction failed"
    print(f"Extracted auth: {auth}")
    return auth


#createAuth()
