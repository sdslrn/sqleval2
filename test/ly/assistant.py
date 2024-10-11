import json

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def extract_ids(data):
    ids = [item['question_id'] for item in data]
    SQLs = [item['SQL'] for item in data]
    prompts = [item['prompt'] for item in data]
    return ids, SQLs, prompts

def main(file_path):
    data = read_json_file(file_path)
    ids, SQLs, prompts = extract_ids(data)
    cnt = 0
    total = 16
    for cnt in range(len(data)):
        if cnt == total :
            print(ids[cnt])
            print(SQLs[cnt])
            print(prompts[cnt])
            break
        else :
            cnt += 1

if __name__ == "__main__":
    # 你可以在这里硬编码文件路径，或者通过命令行参数传递
    file_path = '../../data/updated_dev_tied_append.json'  # 示例路径，可以修改为你的JSON文件路径
    main(file_path)