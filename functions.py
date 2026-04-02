import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent
json_path = BASE_DIR / Path('finances.json')


def show_relatory():
    print(read_json())
    
def add_launch(name, value, type,category, date):
    data = read_json()

    new_item = {
        "id" : len(data)+1,
        "type": type,
        "category": category,
        "name": name,
        "value": value,
        "date": date
    }

    data.append(new_item)

    with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            print("Added")

def remove_launch(id):
    data = read_json()
    initial_lenght = len(data)
    data = [d for d in data if d["id"] != id]

    if len(data) < initial_lenght:

        data = reorder_data_index(data)
        with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    else:
         print("num tem")        

def edit_launch(id,name, type, value, category, date):
    
    data = read_json()
    data_len = len(data)
    index = None

    for i in range(data_len):
         if(data[i]["id"] == id):
              index = i

    if index != None:
        data[index] = {
            "id" : id,
            "type": type,
            "category": category,
            "name": name,
            "value": value,
            "date": date
        }

        data = reorder_data_index(data)

        with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    else:
         print("num tem")


def read_json():
    if(json_path.exists()):
        with open(json_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    return(data)


def reorder_data_index(data):
    new_data = []

    for i in range(len(data)):
            ordened_data = {
                "id" : i+1,
                "type": data[i]["type"],
                "category": data[i]["category"],
                "name": data[i]["name"],
                "value": data[i]["value"],
                "date": data[i]["date"]
            }

            new_data.append(ordened_data)
    
    return new_data

def reorder_by_date():
    data = read_json()
    data.sort(key=lambda x: datetime.strptime(x['date'], '%m-%d-%Y'))
    data = reorder_data_index(data)
    with open(json_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def reorder_by_category():
    data = read_json()
    data.sort(key=lambda x: x['category'].lower())
    data = reorder_data_index(data)
    with open(json_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
