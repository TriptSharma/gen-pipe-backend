# app.py

import os
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS

from main import generate_image_from_inference, generate_prompt, HfInferenceAPI

app = Flask(__name__)
allowed_origins = ["http://localhost:3000/", "https://gen-pipe-frontend.vercel.app/"]

CORS(app, resources={r"/api/*": {"origins": allowed_origins}})

@app.route('/api/generate-image', methods=['OPTIONS', 'POST'])
def generate_image():
    origin = request.headers.get('Origin')
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'CORS preflight successful'})
        if origin in allowed_origins:
            response.headers.add('Access-Control-Allow-Origin', origin)
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response, 200

    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({'error': 'No prompt provided.'}), 400

    prompt = data['prompt']
    print(prompt)
    try:
        enhanced_prompt = generate_prompt(prompt)
        img_bytes = generate_image_from_inference(HfInferenceAPI.FLUX_DEV, enhanced_prompt)

        # Save image to a bytes buffer
        # buffered = io.BytesIO()
        # image.save(buffered, format="PNG")
        # img_bytes = buffered.getvalue()

        # # Encode image to base64
        img_base64 = base64.b64encode(img_bytes).decode('utf-8')
        response = jsonify({'image': img_base64})
        if origin in allowed_origins:
            response.headers.add('Access-Control-Allow-Origin', origin)
        return response, 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"success": True, "message": "Test route working"})

@app.route('/')
def landing_page():
    return 'Spawned in Arena'

if __name__ == '__main__':
    app.run()
