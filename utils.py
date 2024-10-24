import io
import re
import base64
from PIL import Image


def decode_data_uri(data_uri):
    # Regular expression to extract the Base64 part
    match = re.match(r'data:(image/\w+);base64,(.+)', data_uri)
    if not match:
        raise ValueError("Invalid Data URI format")
    
    mime_type, base64_data = match.groups()
    byte_data = base64.b64decode(base64_data)
    return byte_data


def img2url(image):
    image_data = image.tobytes()
    # Convert the image content to base64
    encoded_image = base64.b64encode(image_data)
    image_url = f"data:image/png;base64,{encoded_image.decode('utf-8')}"
    return image_url


def bytes_to_pil(image_bytes):
    try:
        image = Image.open(io.BytesIO(image_bytes))
        return image
    except Exception as e:
        print(f"Error converting bytes to image: {e}")
        return None
    
def save_sd_bytes_img(bytes_data):
    for i, image in enumerate(bytes_data["artifacts"]):
        with open(f"./out/v1_txt2img_{i}.png", "wb") as f:
            f.write(base64.b64decode(image["base64"]))
