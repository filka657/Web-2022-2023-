import json
import pprint

with open('quiz.json', 'r') as f:
    data = json.load(f)
data['quiz']['maths']['q3'] = {'question': '2 * 3 = ?', 'options': ['4', '5', '6'], 'answer': str(2 * 3)}
data_json = json.dumps(data, indent = 4)
with open('newquiz.json', 'w') as file:
    file.write(data_json)
pprint.pprint(data)
