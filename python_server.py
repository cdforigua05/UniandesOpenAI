from flask import Flask
from flask import jsonify
from flask import Flask, abort, request
from tempfile import NamedTemporaryFile
import whisper
import torch
from pathlib import Path
import os
import json 
import gpt3
import openai

# GPT-3 API Key
openai.api_key = "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"

# Check if NVIDIA GPU is available
torch.cuda.is_available()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load the Whisper model:
model = whisper.load_model("base", device=DEVICE)

app = Flask(__name__)


@app.route("/")
def hello_world():
    print("HELLOW WORLD!")
    rta = {'greeting':'Hello from Flask!'}
    return jsonify(rta)

@app.route('/processAudio',methods=['POST'])
def processAudio():
    print("Llego")
    return "<h1> Super bien </h1>"

@app.route('/whisper', methods=['POST'])
def handler():
    body = request.get_json()
    if len(body)==0:
        # If the user didn't submit any files, return a 400 (Bad Request) error.
        abort(400)
    body=json.loads(body["text"])
    transcript = body["text"]
    summary = gpt3.gpt3complete(transcript).replace("\n", "")
    # For each file, let's store the results in a list of dictionaries.
    # This will be automatically converted to JSON.
    return {'transcript': transcript, 
            "summary":summary}

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
