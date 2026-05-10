data = {
    "id":{
        "num": "del",
        "lang": "first"
    },
    "name": "str"
}

response = data
del data['id']['lang'] #del data['id']['lang'] — удалить ключ lang из словаря

print(response)