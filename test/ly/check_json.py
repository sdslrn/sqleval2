import json

json_file_path = '../../data/zsf/graph_tied_append.json'

with open(json_file_path, 'r', encoding='utf-8') as file:
    datas = json.load(file)
    print(len(datas))

    # 遍历每个元素并输出其graph字段
for element in datas:
    print(element['graph']['nodes'])
