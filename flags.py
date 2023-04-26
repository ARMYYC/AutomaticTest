import json
import os

def header_json():
    data={}
    data['blocks']=[]

    data['blocks'].append({
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': 'Hi Team :wave: Test related with every functionality in the OSCWI Tool'
        }
    })
    with open('jsonFiles/main.json', 'w') as file:
        data = json.dump(data, file, indent=4)

def passed(datos):

    with open('jsonFiles/main.json') as file:
        data = json.load(file)

    data['blocks'].append({
        'type': 'section',
        'text': {
            'type': 'mrkdwn',
            'text': datos
        }
    })

    with open('jsonFiles/main.json', 'w') as file:
        data = json.dump(data, file, indent=4)

def unpassed(datos):

    with open('jsonFiles/main.json') as file:
        data = json.load(file)

    data['blocks'].append({
        'type': 'section',
        'text': {   
            'type': 'mrkdwn',
            'text': datos
        }
    })

    with open('jsonFiles/main.json', 'w') as file:
        data = json.dump(data, file, indent=4)

def delete_json_file():

    pathName = os.path.dirname(os.path.abspath(__file__))
    jsonFile = f"{pathName}/jsonFiles/main.json"
    print(jsonFile)
    os.remove(jsonFile)
