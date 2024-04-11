
import os

def walk_directory(directory, parent_name=None, depth=0):
	"""批量标注。
	Args:
		directory (str): 要遍历的目录路径。
		depth (int): 当前遍历的深度，用于可视化和理解递归深度。
		parent_name: str: 父目录名称。
	"""
	# 获取当前目录下的所有子目录和文件
	with os.scandir(directory) as entries:
		for entry in entries:
			if entry.is_dir():
				if depth == 0:
					parent_name = entry.name
				# 递归调用以遍历子目录
				walk_directory(entry.path, parent_name, depth + 1)
			elif entry.is_file():
				if parent_name is None:
					# 处理隐藏文件
					continue
				file_path = entry.path  # 目标文件的路径
				file_path = file_path[0: file_path.index('.')] + '.txt'
				# 使用追加模式打开文件, 如果文件不存在，在指定路径创建一个新文件，并写入指定的文本行。
				with open(file_path, 'w', encoding='utf-8') as file:
					file.write(parent_name + '\n')


if __name__ == '__main__':
	fileDir = '/Volumes/Game Drive/病虫害/病虫害识别数据集/病害/train'
	walk_directory(fileDir)
