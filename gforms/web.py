import json

from flask import Flask, request, jsonify
from threading import Thread
# Assuming the following imports are in your environment
from gforms import prompts, ai, gsheets, gmail

app = Flask(__name__)


def background_task(data):
    try:
        print('inside background')
        prompt = prompts.get_prompt_to_get_blueprint(data)
        if prompt is not None:
            print('before blup')
            blueprint = ai.get_blueprint(prompt)
            print('after blup')
            gmail.send_email('Check out your Blueprint', blueprint, data['Email Address'])
            
            data_str = json.dumps(data)
            gsheets.insert_base_items([[data_str, blueprint, prompt]])

    except Exception as x:
        print(x)


@app.route('/handle_gforms_notifications', methods=['POST'])
def handle():
    try:
        data = request.json

        thread = Thread(target=background_task, args=[data])
        thread.start()

        return jsonify({"message": "Data received successfully"}), 200

    except Exception as x:
        print(x)
        return jsonify({"error": f"Error: {x}"}), 500


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)  # Adjust the host and port as needed
