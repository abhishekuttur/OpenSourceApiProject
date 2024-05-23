# from flask_cors import CORS
from flask import request, jsonify
import json
from pymongo import MongoClient
import json
import google.generativeai as genai
from app import create_app


# app = Flask(__name__)
app=create_app()
# CORS(app)

@app.route('/process_this_prompt', methods=['POST'])
def process_this_prompt():
    prompt=request.json.get('prompt')
    
    # genai.configure(api_key="AIzaSyAXvlaK-F0ukOyv259cFKmW-vqKUVjO1wQ")
    genai.configure(api_key="AIzaSyAlk2Th43xvHBtWG32I5f5A8iBdfaPdMYs")

    generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                        generation_config=generation_config)
    except Exception as e:
        print(f"Error creating GenerativeModel: {e}")
        exit(1)

    convo = model.start_chat(history=[])
    convo.send_message(prompt)
    data=convo.last.text
    app.logger.info("D A T A >>>>>>>>>>>{}".format(data))
    # step1_output, step2_output = data.split("```json\n")
    json_data_1,json_data_2 = data.split('"Step2":')
    json1=json_data_1.split('"Step1":')[1]  
    cleanJson1=json1.strip()[0:-1]
    
    json_data1 = json.loads(cleanJson1)
    
    cleanJson2=json_data_2.strip()[0:-5]    
    json_data2 = json.loads(cleanJson2)
    def find_sublevel_nodes(attack_id):
        sublevel_nodes = []
        for item in json_data2:
            if item['Sub_Attack_id'].startswith(attack_id + '-'):
                sublevel_nodes.append({
                    'Sub_Attack_id': item['Sub_Attack_id'],
                    'Title': item['Title'].split(':')[0]

                })
        return sublevel_nodes

    transformed_data = []

    for item in json_data1:
            main_level_node = {
                'Attack_id': item['Attack_id'],
                'Title': item['Title'].split(':')[0],
                'sublevel1': find_sublevel_nodes(item['Attack_id'])
            }
            transformed_data.append(main_level_node)
    return transformed_data 

# Mongo DB
clientMongo = MongoClient('mongodb://localhost:27017')
db = clientMongo['MY_DB']

@app.route('/add_data',methods=['POST'])
def add_data():
    data=[
        {
            'attack_id':1,
            'Title':'New Attack 1'
        },{
            'attack_id':2,
            'Title':'New Attack 2'
        },{
            'attack_id':3,
            'Title':'New Attack 3'
        },{
            'attack_id':4,
            'Title':'New Attack 4'
        }
    ]
    app.logger.info("D A T A >>>>>>>>>>>{}".format(data))
    db.my_collection.insert_many(data)  
    return 'Data inserted successfully!'

@app.route('/get_details',methods=['POST'])
def get_details():
    data = list(db.my_collection.find({}))
    app.logger.info("D A T A >>>>>>>>>>>{}".format(data))
    for item in data:
        item['_id'] = str(item['_id'])
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
