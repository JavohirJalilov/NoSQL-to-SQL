import requests
from tinydb import TinyDB
db = TinyDB('data.json')

tables = list(db.tables())
table = db.table(tables[0])

data = table.all()

url = 'http://127.0.0.1:8000/api/add/'
print(data[0])
for i in data:
    data = {
        "price": i['price'],
        "memory": i['memory'],
        "ram": i['RAM'],
        "color": i['color'],
        "img_url": i['img_url'],
        "name": i['name'],
        "model": i['company'],
    }

    response = requests.post(url, json=data)
    print(response.text)
