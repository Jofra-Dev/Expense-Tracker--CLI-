import json
from pathlib import Path
from datetime import datetime
import os
import requests
from dotenv import load_dotenv 

BASE_DIR = Path(__file__).parent
json_path = BASE_DIR / Path('finances.json')

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def show_relatory():
    clear()
    data = read_json()

    if not data:
        print("\n--- No records found. ---")
        return

    # Formatted table header with specific column widths
    header = f"{'ID':<4} | {'NAME':<20} | {'CATEGORY':<15} | {'TYPE':<10} | {'VALUE':<10} | {'DATE':<12}"
        
    print("\n" + "=" * len(header))
    print(header)
    print("-" * len(header))
        
    for d in data:
        print(f"{d['id']:<4} | {d['name']:<20} | {d['category']:<15} | {d['type']:<10} | ${d['value']:>8.2f} | {d['date']:<12}")
        
    print("=" * len(header) + "\n")

def add_launch(name, value, type, category, date):
    data = read_json()

    new_item = {
        "id" : len(data) + 1,
        "type": type,
        "category": category,
        "name": name,
        "value": value,
        "date": date
    }

    data.append(new_item)

    # Persists updated data list to JSON file
    with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

def remove_launch(id):
    data = read_json()
    initial_lenght = len(data)
    # Filters out the target ID to create a new list
    data = [d for d in data if d["id"] != id]

    if len(data) < initial_lenght:
        data = reorder_data_index(data)
        with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    else:
         print("ID not found.")

def edit_launch(id, name, type, value, category, date):
    data = read_json()
    data_len = len(data)
    index = None

    # Locates the index of the specific record by ID
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
         print("ID not found.")

def read_json():
    # Ensures the file exists and handles empty/corrupted JSON scenarios
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
    # Fixes ID continuity after deletions or sorting
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
    # Converts string dates to datetime objects for accurate chronological sorting
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

def clear():
    # Detects OS to run the appropriate terminal clear command
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def agent_ia():
    clear()
    data = read_json()

    prompt = (
    "You are a CLI Financial Expert System. " +
    "Analyze this JSON data: " + json.dumps(data) + " " +
    "\n\nSTRICT RULES FOR YOUR RESPONSE:" +
    "\n1. Use only plain text and standard ASCII/Unicode characters." +
    "\n2. Use a 'CLI look': create boxes using characters like │, ┌, ┐, └, ┘, ─." +
    "\n3. Be concise. No long introductions or 'As an AI...'." +
    "\n4. Section 1: 📊 QUICK DASHBOARD (Total Gain vs Total Expense)." +
    "\n5. Section 2: ⚠️ CRITICAL ALERTS (Unnecessary spending or weird data)." +
    "\n6. Section 3: 💡 3 ACTIONABLE STEPS (Specific to the numbers provided)." +
    "\n7. Use a width of max 100 characters for the boxes."
    )

    print("\n" + "─"*50)
    print("  🤖 AGENT AI IS THINKING... PLEASE WAIT")
    print("─"*50 + "\n")

    # API Request to OpenRouter - ensure key privacy in production
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "qwen/qwen3.6-plus:free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "reasoning": {"enabled": True}
        })
    )

    response_data = response.json()
    # Extracts the generated text from the API response object
    ai_response = response_data['choices'][0]['message']['content']

    clear()
    print("\n" + "═"*60)
    print("             🌟 AI FINANCIAL ADVISOR REPORT 🌟")
    print("═"*60 + "\n")
    
    print(ai_response)

    print("\n" + "═"*60)
    input("  ➤ Press ENTER to return to the menu...")