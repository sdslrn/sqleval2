import csv
import json

# def csv_to_json(csv_file_path, json_file_path):
#     # 打开CSV文件进行读取
#     with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         header = next(csv_reader)  # 跳过标题行
#         # 创建空的列表用于存储提取的内容
#         data = []
#         # 逐行读取CSV文件的前两列
#         for row in csv_reader:
#             if len(row) >= 2:
#                 data.append({header[0]: row[0], header[1]: row[1]})
#
#     # 将提取的数据写入JSON文件
#     with open(json_file_path, mode='w', encoding='gbk') as json_file:
#         json.dump(data, json_file, ensure_ascii=False, indent=4)

import csv
import json

# 定义CSV文件名和JSON文件名
csv_file_path = '../../data/sqlite_ly.csv'  # 输入CSV文件路径
json_file_path = '../../data/output_sql_ly.json'  # 输出JSON文件路径

# 初始化一个空列表，用于存储CSV文件中的每一行数据
data = []

# 使用with语句打开CSV文件，确保文件会被正确关闭
with open(csv_file_path, mode='r', newline='', encoding='gbk') as csv_file:
    # 创建一个csv.DictReader对象，它会读取CSV文件的每一行并将其转换为字典
    csv_reader = csv.DictReader(csv_file)

    # 遍历CSV文件中的每一行
    for row in csv_reader:
        # 将每行数据（字典）添加到列表中
        data.append(row)

# 使用with语句打开JSON文件，确保文件会被正确关闭
with open(json_file_path, mode='w', newline='', encoding='utf-8') as json_file:
    # 将列表转换为JSON格式并写入文件
    # 使用indent参数来美化输出，使其更易于阅读
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print(f'CSV文件已成功转换为JSON格式，并保存为{json_file_path}')

# 示例使用
# csv_file_path = '../../data/sqlite_ly.csv'  # 输入CSV文件路径
# json_file_path = '../../data/output_sql_ly.json'  # 输出JSON文件路径
# csv_to_json(csv_file_path, json_file_path)
