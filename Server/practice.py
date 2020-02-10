import json

with open('./naver.json', 'r', encoding='utf-8') as f:
    temp = json.load(f)

print(temp)