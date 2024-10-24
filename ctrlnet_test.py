# buffer = io.BytesIO()
# image.save(buffer, format='JPEG')
# image_bytes = buffer.getvalue()

# Encode the image bytes as a base64 string
image_base64 = base64.b64encode(incept_image_bytes).decode("utf-8")
empty_image_base64 = base64.b64encode(b"0").decode("utf-8")


prompt = (
    "A bohemian-style female travel blogger with sun-kissed skin and messy beach waves."
)
control_image_depth_url = "https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro/resolve/main/assets/depth.jpg"
control_image_canny_url = "https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro/resolve/main/assets/canny.jpg"
control_mode_depth = 2
control_mode_canny = 0

width, height = incept_image.size


def fetch_img_from_url(image_url):
    response = requests.get(image_url)
    # Convert the image content to base64
    image_base64 = base64.b64encode(response.content).decode("utf-8")
    return image_base64


control_image_depth = fetch_img_from_url(control_image_depth_url)
control_image_canny = fetch_img_from_url(control_image_canny_url)


## API headers
headers = {"Authorization": f"Bearer {HUGGINGFACE_API}"}
controlnet_headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API}",
    # "Content-Type": "application/json",
}

flux_controlnet_payload = {
    # "inputs": model.generate_content(
    #     get_enhance_prompt("create a side pose of the man in the picture"),
    # ),
    "inputs": prompt,
    "control_images": [control_image_depth, control_image_canny],
    "control_modes": [control_mode_depth, control_mode_canny],
    "width": width,
    "height": height,
    "controlnet_conditioning_scale": [0.2, 0.4],
    "num_inference_steps": 24,
    "guidance_scale": 3.5,
    "generator_seed": 42,
}

# height, width, _  = controlnet_img.shape
ratio = np.sqrt(1024.0 * 1024.0 / (width * height))
new_width, new_height = int(width * ratio), int(height * ratio)
controlnet_img = incept_image.resize((new_width, new_height))


negative_prompt = ""
seed = random.randint(0, 2147483647)

generator = torch.Generator("cuda").manual_seed(seed)

# 0 -- openpose
# 1 -- depth
# 2 -- hed/pidi/scribble/ted
# 3 -- canny/lineart/anime_lineart/mlsd
# 4 -- normal
# 5 -- segment
sdxl_controlnet_payload = {
    "prompt": [prompt] * 1,
    "image_list": [
        empty_image_base64,
        empty_image_base64,
        empty_image_base64,
        image_base64,
        empty_image_base64,
    ],
    "negative_prompt": [negative_prompt] * 1,
    # "generator": generator,
    "generator_seed": seed,
    "width": new_width,
    "height": new_height,
    "num_inference_steps": 30,
    "union_control": True,
    "union_control_type": [0, 0, 0, 1, 0, 0],
}


def controlnet_query(model_payload):
    response = requests.post(
        FLUX_CONTROLNET_API_URL, headers=controlnet_headers, json=model_payload
    )
    # response = requests.post(
    #     SDXL_CONTROLNET_API_URL, headers=controlnet_headers, json=payload
    # )
    return response.content


catalogue_image = bytes_to_image(controlnet_query(flux_controlnet_payload))

print(catalogue_image)
