import json
import os
from datetime import datetime

from flask import Flask, request, jsonify

# Assuming the following imports are in your environment
from gforms import prompts, ai, gsheets, gmail, config
from gforms.gmail import create_pdf_file

app = Flask(__name__)


def background_task(data):
    try:
        print('inside background')
        user_data = prompts.extract_user_data(data)
        if user_data is not None:
            print('before blup')
            blueprint_json = ai.generate_blueprint(user_data)
            print(f"receive AI response. Length: {len(blueprint_json)}")
            with open("blueprints/latest.json", 'w') as json_file:
                json.dump(json.loads(blueprint_json), json_file, indent=4)
            if os.path.exists("blueprints/latest.json"):
                print("json stored")

            recipient = data['Email Address']
            blueprint_filename = create_pdf_file("blueprints", "blueprint.pdf", blueprint_json, recipient)
            message = f"Please, " \
                      f"let us know if the Blueprint was useful for you. " \
                      f"Any kind of feedback is very valuable for us.\n" \
                      f"If you are not satisfied with the Blueprint, we will send you another " \
                      f"one taking your feedback into account.\nBy the way, you can maintain and " \
                      f"improve your lifestyle with the " \
                      f"Blueprint for the 2nd week by filling the feedback form\n\n" \
                      f"https://forms.gle/VQRdsc43q51VdsgW6"
            gmail.send_email('Check out your Blueprint', message, data['Email Address'], blueprint_filename)

            data_str = json.dumps(data)
            now = datetime.now()
            epoch = datetime(1899, 12, 30)
            delta = now - epoch
            current_time = delta.days + (delta.seconds / 86400)

            gsheets.insert_base_items([[data_str, blueprint_json, user_data, current_time]])

    except Exception as x:
        config.logger.exception(x)


@app.route('/handle_gforms_notifications', methods=['POST'])
def handle():
    try:
        data = request.json

        background_task(data)

        return jsonify({"message": "Data received successfully"}), 200

    except Exception as x:
        print(x)
        return jsonify({"error": f"Error: {x}"}), 500


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)  # Adjust the host and port as needed
