import json
from util.prompt_text2graph import get_prompt

input_path = '../../data/dev_tied_append.json'
output_path = '../../data/updated_dev_tied_append.json'

with open(input_path,'r',encoding='utf-8') as f:
    data = json.load(f)

update_data = []

for item in data:
    sql = item['SQL']
    requirement = item['question'] + item['evidence']

    prompt_result = get_prompt(sql,requirement)

    update_item = item.copy()
    update_item['prompt'] = prompt_result

    update_data.append(update_item)

with open(output_path,'w',encoding='utf-8') as f:
    json.dump(update_data,f,indent = 4)
    # f.write('\n')

