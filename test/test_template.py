import json
# import argparse

# args_parser = argparse.ArgumentParser()
# args_parser.add_argument('--data_path', type=str, default="../data/requirement-check.json")
# args_parser.add_argument("--idx", type=int, default=0)
# args = args_parser.parse_args()

data_path = "../data/requirement-check.json"

with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

idx = 37
print("idx:", idx)

# 循环遍历json文件
for k, item in enumerate(data):
    db_info = item['db_info']
    requirement = item['requirement']
    template = (f"## <db_info>\n{db_info} \n<db_info>## \n\n"
                f"以上是一个数据库的具体信息（db_info），你需要帮我分析其需求分析（requirement）是否合理，请用中文回答。需求分析如下：\n\n"
                f"## <requirement>\n{requirement} \n<requirement>##")
    if k == idx:
        print(template)
        break

# california_schools: 0 1 2
# card_games: 3 4 5 6 7 8 9

