from flask import Flask, request, jsonify
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import json

# Postman Url : http://127.0.0.1:5000/process_prompt

# prompt = """
# You are an automotive in-vehicle network security expert tasked with creating a list of the Top 5 Attack Vectors for CAN Bus targeting security analysts performing threat modeling for Electronic Control Units (ECUs).
# Step#1 : On each of the listed 5 attacks , extract the heading which is delimited by a colon and list down the 5 attacks.Arrange the heading from Step#1 , and create a json output with following keys:
# Attack_id, Level=1 , Title, Description ,Type of Attack Step#2 : Take the Attack list from Step#1  and create top 3 sub attacks for each of the attack. Arrange the attacks from Step#2 , and create a json output with following keys: Attack_id, Level=2 , Title, Description ,Type of Attack
# """

# APIKEY = "AKEyXzUyYGh6sNVXxL4QTM4j3BZ-oPXXzny5eTmbZ-vUsXqkCdmmR-lGASm3R5JINarzyC7m3t0"

import openai

import os

import pandas as pd

import time

APIKEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYzkyMDg2NzctNTA3NS00YzYyLWEwZDEtMjcwOGEyM2M3ZjEwIiwidHlwZSI6ImFwaV90b2tlbiJ9.APzvbMo8bOI0Q6ygfhy0soHt3tBe1-mPWyXDBMG7RV4"

import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYzkyMDg2NzctNTA3NS00YzYyLWEwZDEtMjcwOGEyM2M3ZjEwIiwidHlwZSI6ImFwaV90b2tlbiJ9.APzvbMo8bOI0Q6ygfhy0soHt3tBe1-mPWyXDBMG7RV4"}

url = "https://api.edenai.run/v2/text/generation"
# print(result)
# print(result['openai']['generated_text'])

# prompt = '\n\n\nStep#1 Output:\n[\n  {\n    "Attack_id": 1,\n    "Level": 1,\n    "Title": "Denial of Service (DoS) Attack",\n    "Description": "An attacker floods the CAN bus with a large number of messages, causing the system to crash or become unresponsive.",\n    "Type of Attack": "Physical"\n  },\n  {\n    "Attack_id": 2,\n    "Level": 1,\n    "Title": "Man-in-the-Middle (MitM) Attack",\n    "Description": "An attacker intercepts and modifies messages on the CAN bus, allowing them to inject malicious commands or alter data.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 3,\n    "Level": 1,\n    "Title": "Replay Attack",\n    "Description": "An attacker records legitimate messages on the CAN bus and replays them at a later time to gain unauthorized access or cause system malfunctions.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 4,\n    "Level": 1,\n    "Title": "Firmware/Software Attack",\n    "Description": "An attacker exploits vulnerabilities in the ECU\'s firmware or software to gain access to the CAN bus and manipulate data or commands.",\n    "Type of Attack": "Software"\n  },\n  {\n    "Attack_id": 5,\n    "Level": 1,\n    "Title": "Physical Attack",\n    "Description": "An attacker physically accesses the CAN bus or ECU to tamper with hardware components or install malicious devices.",\n    "Type of Attack": "Physical"\n  }\n]\n\nStep#2 Output:\n[\n  {\n    "Attack_id": 1,\n    "Level": 2,\n    "Title": "Flooding Attack",\n    "Description": "An attacker sends a large number of messages to the CAN bus, overwhelming the system and causing a DoS.",\n    "Type of Attack": "Physical"\n  },\n  {\n    "Attack_id": 1,\n    "Level": 2,\n    "Title": "Jamming Attack",\n    "Description": "An attacker continuously transmits noise on the CAN bus, disrupting communication and causing a DoS.",\n    "Type of Attack": "Physical"\n  },\n  {\n    "Attack_id": 1,\n    "Level": 2,\n    "Title": "Bus Off Attack",\n    "Description": "An attacker sends a series of error frames to the CAN bus, causing the system to go into a Bus Off state and become unresponsive.",\n    "Type of Attack": "Physical"\n  },\n  {\n    "Attack_id": 2,\n    "Level": 2,\n    "Title": "Message Modification",\n    "Description": "An attacker intercepts and modifies messages on the CAN bus, allowing them to inject malicious commands or alter data.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 2,\n    "Level": 2,\n    "Title": "Message Injection",\n    "Description": "An attacker injects new messages onto the CAN bus, bypassing authentication and authorization mechanisms.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 2,\n    "Level": 2,\n    "Title": "Message Replay",\n    "Description": "An attacker replays previously captured messages on the CAN bus, bypassing authentication and authorization mechanisms.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 3,\n    "Level": 2,\n    "Title": "Message Recording",\n    "Description": "An attacker records legitimate messages on the CAN bus and replays them at a later time to gain unauthorized access or cause system malfunctions.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 3,\n    "Level": 2,\n    "Title": "Message Manipulation",\n    "Description": "An attacker modifies the contents of recorded messages before replaying them, allowing them to inject malicious commands or alter data.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 3,\n    "Level": 2,\n    "Title": "Message Deletion",\n    "Description": "An attacker deletes recorded messages on the CAN bus, causing system malfunctions or disrupting communication.",\n    "Type of Attack": "Network"\n  },\n  {\n    "Attack_id": 4,\n    "Level": 2,\n    "Title": "Buffer Overflow",\n    "Description": "An attacker exploits a buffer overflow vulnerability in the ECU\'s firmware or software to gain access to the CAN bus and manipulate data or commands.",\n    "Type of Attack": "Software"\n  },\n  {\n    "Attack_id": 4,\n    "Level": 2,\n    "Title": "Code Injection",\n    "Description": "An attacker injects malicious code into the ECU\'s firmware or software, allowing them to gain access to the CAN bus and manipulate data or commands.",\n    "Type of Attack": "Software"\n  },\n  {\n    "Attack_id": 4,\n    "Level": 2,\n    "Title": "Firmware Update Attack",\n    "Description": "An attacker exploits vulnerabilities in the ECU\'s firmware update process to install malicious firmware, gaining access to the CAN bus and manipulating data or commands.",\n    "Type of Attack": "Software"\n  },\n  {\n    "Attack_id": 5,\n    "Level": 2,\n    "Title": "ECU Tampering",\n    "Description": "An attacker physically accesses the ECU and modifies hardware components, allowing them to manipulate data or commands on the CAN bus.",\n    "Type of Attack": "Physical"\n  },\n  {\n    "Attack_id": 5,\n    "Level": 2,\n    "Title": "Device Installation",\n    "Description": "An attacker installs a malicious device on the CAN bus, allowing them to intercept and modify messages or inject commands.",\n    "Type of Attack": "Physical"\n  },\n  {\n    "Attack_id": 5,\n    "Level": 2,\n    "Title": "ECU Replacement",\n    "Description": "An attacker replaces a legitimate ECU with a malicious one, gaining access to the CAN bus and manipulating data or commands.",\n    "Type of Attack": "Physical"\n  }\n]'

def parse_step_output(step_output):
    step_output = step_output.strip()
    attacks_list = step_output.split("[")[1].split("]")[0]
    attacks = attacks_list.split("{")[1:]
    parsed_attacks = []
    for attack in attacks:
        attack_properties = attack.split(",\n")
        attack_info = {}
        for prop in attack_properties:
            if prop.strip() == "" or prop.strip() == ",":
                continue
            key, value = prop.strip().split(": ")
            val = value.strip('"')
            # print(key,value)
            # import pdb;pdb.set_trace()
            if key == '"Type of Attack"':
                # import pdb;pdb.set_trace()
                val = val.split('"')[0]
            attack_info[key.strip('"')] = val
        parsed_attacks.append(attack_info)

    return parsed_attacks


@app.route('/process_prompt', methods=['POST'])
def process_prompt():
    # prompt='You are an automotive in-vehicle network security expert tasked with creating a list of the Top 5 Attack Vectors for CAN Bus targeting security analysts performing threat modeling for Electronic Control Units (ECUs).Step#1 : On each of the listed 5 attacks , extract the heading which is delimited by a colon and list down the 5 attacks.Arrange the heading from Step#1 , and create a json output with following keys: Attack_id, Level=1 , Title, Description ,Type of Attack Step#2 : Take the Attack list from Step#1  and create top 3 sub attacks for each of the attack. Arrange the attacks from Step#2 , and create a json output with following keys: Attack_id, Level=2 , Title, Description ,Type of Attack'
    # print(request.args)
    # print(request.params)
    # print(request)
    # print("----------------------------------------")

    prompt=request.json.get('prompt')
    # prompt = request.args.get('prompt')

    payload = {
        "providers": "openai,cohere",
        "text": prompt,
        "temperature": 0.2,
        "max_tokens": 3000,
        "fallback_providers": ""
    }
    # print(payload)

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)

    prompt = result['openai']['generated_text']
    print(prompt)
    print("---------------------------------------------------------------------------")
    step1_output, step2_output = prompt.split("Step#2 Output:")
    print(step1_output)
    step1_json = parse_step_output(step1_output)
    step2_json = parse_step_output(step2_output)
    step2_updated = dict()
    for item in step2_json:
        if item['Attack_id'] in step2_updated:
            step2_updated[item['Attack_id']].append(item)
        else:
            step2_updated[item['Attack_id']] = [item]

    for item in step1_json: 
        attack_id = item["Attack_id"]
        if attack_id in step2_updated:
            item["sublevel1"] = step2_updated[attack_id]
    return jsonify(step1_json)
    

if __name__ == '__main__':
    app.run(debug=True)
