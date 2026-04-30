import json

json_data = """ {
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "courses": [
    "Python",
    "QA Automation",
    "API Testing"
  ],
  "addres": {
    "city": "Москва",
    "zip": "10100"

  }
}
"""

parsed_data = json.loads(json_data)

print(parsed_data['courses'])
print(parsed_data['addres']['city'])
print(parsed_data['addres']['zip'])


data = {
    'name': 'Иван',
    'age': 25,
   'is_student': True,
}
json_string = json.dumps(data, indent=4)
print(json_string)

with open('json_example.json', 'r', encoding='utf-8') as file:
    read_data = json.load(file)
    print(data)

with open('json_user.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)