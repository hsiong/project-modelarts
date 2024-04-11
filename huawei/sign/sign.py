# coding=utf-8

import requests

from config import config
from sign.apig_sdk import signer

if __name__ == '__main__':
	sig = signer.Signer()
	# Set the AK/SK to sign and authenticate the request.
	# 认证用的ak和sk硬编码到代码中或者明文存储都有很大的安全风险，建议在配置文件或者环境变量中密文存放，使用时解密，确保安全；
	# 本示例以ak和sk保存在环境变量中为例，运行本示例前请先在本地环境中设置环境变量HUAWEICLOUD_SDK_AK和HUAWEICLOUD_SDK_SK。
	sig.Key = config.__SK
	sig.Secret = config.__AK
	
	# The following example shows how to set the request URL and parameters to query a VPC list.
	# Set request Endpoint.
	# Specify a request method, such as GET, PUT, POST, DELETE, HEAD, and PATCH.
	# Set request URI.
	# Set parameters for the request URL.
	r = signer.HttpRequest("GET", "https://endpoint.example.com/v1/77b6a44cba5143ab91d13ab9a8ff44fd/vpcs?limit=1")
	# Add header parameters, for example, x-domain-id for invoking a global service and x-project-id for invoking a project-level service.
	r.headers = {"content-type": "application/json"}
	# Add a body if you have specified the PUT or POST method. Special characters, such as the double quotation mark ("), contained in the body must be escaped.
	r.body = ""
	sig.Sign(r)
	print(r.headers["X-Sdk-Date"])
	print(r.headers["Authorization"])
	resp = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body)
	print(resp.status_code, resp.reason)
	print(resp.content)


# 华为云接口验签
def sign(url: str) -> signer.HttpRequest:
	# Create request, set method, url, headers and body.
	method = 'POST'
	headers = {"x-sdk-content-sha256": "UNSIGNED-PAYLOAD"}
	request = signer.HttpRequest(method, url, headers)
	
	# Create sign, set the AK/SK to sign and authenticate the request.
	sig = signer.Signer()
	sig.Key = config.__AK
	sig.Secret = config.__SK
	sig.Sign(request)
	return request
