import os

# 数据文件夹路径
data_dir = 'origin_data'

# 类别列表
classes = ['0', '1']

# 用于存储数据的列表
data = []

# 遍历所有类别文件夹
for class_name in classes:
    class_dir = os.path.join(data_dir, class_name)

    # 遍历所有文件
    for file_name in os.listdir(class_dir):
        file_path = os.path.join(class_dir, file_name)
        print(file_name)
        # 读取文件内容
        with open(file_path, 'r') as f:
            content = f.read()
        
        # 将数据添加到列表中
        data.append((content, class_name))

# 将数据保存为CSV文件
import csv

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
