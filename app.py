# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image, ImageDraw, ImageFont
import io
import base64

from main import generate_image_from_inference, generate_prompt, HfInferenceAPI

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://gen-pipe-frontend.vercel.app/"}})

@app.route('/api/generate-image', methods=['OPTIONS', 'POST'])
def generate_image():
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'CORS preflight successful'})
        response.headers.add('Access-Control-Allow-Origin', 'https://gen-pipe-frontend.vercel.app/')
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
        response.headers.add('Access-Control-Allow-Origin', 'https://gen-pipe-frontend.vercel.app/')
        return response, 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"success": True, "message": "Test route working"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
