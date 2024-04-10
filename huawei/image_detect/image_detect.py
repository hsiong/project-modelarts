
# coding=utf-8

import requests
import os
from sign.apig_sdk import signer
from config import config

if __name__ == '__main__':
	# Config url, ak, sk and file path.
	url = config.__URL
	# 认证用的ak和sk硬编码到代码中或者明文存储都有很大的安全风险,建议在配置文件或者环境变量中密文存放,使用时解密,确保安全;
	# 本示例以ak和sk保存在环境变量中来实现身份验证为例,运行本示例前请先在本地环境中设置环境变量HUAWEICLOUD_SDK_AK和HUAWEICLOUD_SDK_SK。
	ak = os.environ[config.__AK]
	sk = os.environ[config.__SK]
	file_path = "预测文件的本地路径"
	
	# Create request, set method, url, headers and body.
	method = 'POST'
	headers = {"x-sdk-content-sha256": "UNSIGNED-PAYLOAD"}
	request = signer.HttpRequest(method, url, headers)
	
	# Create sign, set the AK/SK to sign and authenticate the request.
	sig = signer.Signer()
	sig.Key = ak
	sig.Secret = sk
	sig.Sign(request)
	
	# Send request
	files = {'images': open(file_path, 'rb')}
	resp = requests.request(request.method, request.scheme + "://" + request.host + request.uri, headers=request.headers, files=files)
	
	# Print result
	print(resp.status_code)
	print(resp.text)


