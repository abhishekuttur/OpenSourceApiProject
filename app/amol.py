from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/process_prompt', methods=['POST'])
def process_prompt():
    try:
        data=request.json
        print(data)
        # prompt = request.args.get('prompt')
        # Assuming your prompt processing logic here
        # For simplicity, I'll just echo back the received prompt
        return jsonify({"prompt": data.get('prompt')})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# if __name__ == '_main_':
app.run(debug=True, host='127.0.0.1', port=5000)