from tokenization.sent_tokenizer import sent_tokenizer
import json

with open('/home/nbviet/Desktop/1.json') as f:
    data = json.load(f)
new_data = []
for d in data:
    d['title'] = sent_tokenizer(d['title'])
    d['description'] = sent_tokenizer(d['description'])
    d['content'] = sent_tokenizer(d['content'])
    new_data.append(d)
with open('final.json', 'w') as f:
    json.dump(new_data, f)
