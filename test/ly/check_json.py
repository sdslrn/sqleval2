import json


def read_and_print_graphs(json_file_path):
    try:
        # 打开并读取JSON文件
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # 遍历每个元素并输出其graph字段
        for element in data:
            graph = element.get('graph')
            if graph:
                print(f"Element ID: {element.get('id')}, Name: {element.get('name')}")
                print(json.dumps(graph, indent=4))  # 使用json.dumps来格式化输出
                print('-' * 40)  # 分隔符
            else:
                print(f"Element ID: {element.get('id')}, Name: {element.get('name')} has no graph field.")

    except FileNotFoundError:
        print(f"Error: The file {json_file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file {json_file_path} is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # 使用示例


json_file_path = 'path/to/your/jsonfile.json'  # 替换为你的JSON文件路径
read_and_print_graphs(json_file_path)