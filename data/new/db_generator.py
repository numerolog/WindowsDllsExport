#!/usr/bin/env python3
import os.path
import sqlite3
import json

def parse_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>>FILE;'):
                file_name = line.split(';')[1].rstrip('<')
                data.append({'type': 'file', 'name': file_name + '.dll', 'functions': []})
            elif line.startswith('>>FUNC;'):
                func_name = line.split(';')[1].rstrip('<')
                data[-1]['functions'].append(func_name)
    return data

'''
for item in parsed_data:
    print(f"File: {item['name']}")
    print("Functions:")
    for func in item['functions']:
        print(f"- {func}")
    print()
'''

def save_sqlite(parsed_data, save_to):
    print('Creating sqlite table...')
    conn = sqlite3.connect(save_to)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exports (
            dllname text,
            exportname text
        )
    ''')

    for item in parsed_data:
        for func in item['functions']:
            cursor.execute('INSERT INTO exports (dllname, exportname) VALUES (?, ?)', (item['name'], func))

    conn.commit()
    conn.close()
    print('Done.')

def save_json(parsed_data, save_to):
    print('Creating json table...')
 
    data = []
    for item in parsed_data:
        for func in item['functions']:
            data.append({
                "dllname": item['name'],
                "exportname": func
            })

    with open(save_to, 'w') as file:
        json.dump(data, file, indent=4)
    print('Done.')


file_path = 'raw/WinXP-2600.TXT' 
file_name = os.path.basename(file_path).rsplit('.', 1)[0]
parsed_data = parse_file(file_path)
save_sqlite(parsed_data, 'converted/' + file_name + '-exports.db')
save_json(parsed_data, 'converted/' + file_name + '-exports.json')


