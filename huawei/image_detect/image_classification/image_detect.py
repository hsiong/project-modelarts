# coding=utf-8

import os

import requests

from config import config
from sign import sign


# 保存结果到文件
def save2file(line: str):
	file_path = 'example.txt'  # 目标文件的路径
	# 使用追加模式打开文件, 如果文件不存在，在指定路径创建一个新文件，并写入指定的文本行。
	with open(file_path, 'a', encoding='utf-8') as file:
		file.write(line + '\n')


# 调用华为云接口, 实现图像分类
def detect_file(file):
	# 将目录的路径和文件名合成一个完整的路径
	file_path = os.path.join(root, file)
	# Send request
	files = {'images': open(file_path, 'rb')}
	resp = requests.request(request.method, request.scheme + "://" + request.host + request.uri,
							headers=request.headers, files=files)
	
	# saveResult
	code = resp.status_code
	out = resp.text
	strOut = f'filePath:{file_path},code:{code},out:{out}'
	print(strOut)
	save2file(strOut)


if __name__ == '__main__':
	request = sign.sign(config.__URL)
	fileDir = '/Volumes/Game Drive/病虫害/病虫害识别数据集/病害/test'
	# os.walk生成目录树下的所有文件名
	for root, dirs, files in os.walk(fileDir):
		for file in files:
			detect_file(file)
