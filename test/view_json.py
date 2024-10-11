import json

with open('../data/graph.json','r',encoding='utf-8') as f:
    data = json.load(f)
cnt = 0
for item in data:
    # if item['db_id'] == 'formula_1':
    if cnt == 2 :
        print(item['graph'][0])
        # print(item['db_id'])
        # print(item['table_name'])
        # print(item['db_info'])
        # print(item['requirement'])
        break
    cnt += 1
print(cnt)