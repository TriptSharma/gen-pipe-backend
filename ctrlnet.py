import base64
from gradio_client import Client
import sys
from rich import print

client = Client("https://a23884f5d2e9044cb9.gradio.live/")

# def __wait_for_startup__(self) -> None:
#     if not self.__process__:
#         print(
#             "[red]Error[/red]: Fooocus is not running. Can't establish a connection to the Fooocus server."
#         )
#         self.dispose()
#         sys.exit(1)

#     for line in self.fooocus_logs:
#         if "App started successful" in line:
#             print("Fooocus has started successfully!")
#             break




def generate_picture(
    prompt: str,
    resolution: tuple = (896, 1152),
    model: str = "juggernautXL_v8Rundiffusion.safetensors",
    lora_1: str | None = "sd_xl_offset_example-lora_1.0",
    lora_1_weight: int | float = 1,
    refiner: None = None,
    refiner_weight: float = 0.5,
    upscale_mode: bool = False,
    save_picture: str | None = None,
) -> bool | str:
    placeholder_img = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQImWNgYGBgAAAABQABh6FO1AAAAABJRU5ErkJggg=="
    print(f"Setting Fooocus params...")
    # client.predict(True, fn_index=53)  # Advanced: True
    client.predict(fn_index=65)  # ??? some button components called
    client.predict(True, "0", fn_index=66)  # Random: True, Seed: 0

    client.predict(
        False,  
        prompt, 
        "unrealistic, saturated, high contrast, big nose, painting, drawing, sketch, cartoon, anime, manga, render, CG, 3d, watermark, signature, label",
        ["Fooocus V2", "Fooocus Photograph", "Fooocus Negative", "Fooocus Sharp", "Fooocus Masterpiece", "Fooocus Enhance", "Fooocus Cinematic",],
        "Quality",
        f'{resolution[0]}×{resolution[1]} <span style="color: grey;"> | 1:2 </span>',
        1,
        "png",
        "0",
        False,
        6, 3, model, 
        refiner if refiner else "None", 
        refiner_weight if refiner else 0.5,
        True, lora_1 if lora_1 else "None", lora_1_weight,
        True, "None", 1,
        True, "None", 1,
        True, "None", 1,
        True, "None", 1, 
        True, "", 
        "Disabled", placeholder_img, ["Left"],
        placeholder_img,  "", 
        placeholder_img,  
        True,
        True,
        True,
        False,
        1.5,  0.8,  0.3,  
        7,
        2,
        "dpmpp_2m_sde_gpu", 
        "karras",  
        "Default (model)",
        -1, -1, -1, -1, -1, -1, 
        False, False, False, False,
        64, 128,
        "joint", 
        0.25,  
        False,
        1.01, 1.02, 0.99, 0.95, 
        False,
        False,
        "None",
        1,  
        0.618,
        False,
        False,
        0,  
        False,  
        False,  
        "fooocus",
        placeholder_img, 0.5, 0.6, "ImagePrompt",  
        placeholder_img, 0.5, 0.6, "ImagePrompt", 
        placeholder_img, 0.5, 0.6, "ImagePrompt", 
        placeholder_img, 0.5, 0.6, "ImagePrompt", 
        False, 0, 
        False, 
        None,  
        False if upscale_mode == False else True,
        "Disabled",
        "Before First Enhancement",
        "Original Prompts",  
        False, 
        "",  
        "",  
        "",  
        "sam", "full", "vit_b", 0.25, 0.3, 0, False,"v2.6", 1, 0.618, 0, False, False, "",  "",  "",  
        "sam", "full", "vit_b", 0.25, 0.3, 0, False,"v2.6", 1, 0.618, 0, False, False, "",  "",  "",  
        "sam", "full", "vit_b", 0.25, 0.3, 0, False,"v2.6", 1, 0.618, 0, False, 
        fn_index=67
    )



    # client.predict(
    #     False,  # bool gen image grid
    #     prompt,  # prompt
    #     "unrealistic, saturated, high contrast, big nose, painting, drawing, sketch, cartoon, anime, manga, render, CG, 3d, watermark, signature, label",  # negative prompt
    #     [
    #         "Fooocus V2",
    #         "Fooocus Photograph",
    #         "Fooocus Negative",
    #         "Fooocus Sharp",
    #         "Fooocus Masterpiece",
    #         "Fooocus Enhance",
    #         "Fooocus Cinematic",
    #     ],  # List[str] in 'Selected Styles' Checkboxgroup component
    #     "Quality",  # Performance radio button
    #     f'{resolution[0][0]}×{resolution[0][1]} <span style="color: grey;"> | 1:2 </span>',  # aspect ratio
    #     1,  # image number slider
    #     "png",  # output format
    #     "0",  # seed (str)
    #     False,  # read wildcards in order
    #     6,  # image sharpness
    #     3,  # guidance scale
    #     model,  # Option from: ['juggernautXL_v8Rundiffusion.safetensors'] Base Model (SDXL only)
    #     refiner if refiner else "None",  # Option from: ['None', 'juggernautXL_v8Rundiffusion.safetensors']) in 'Refiner (SDXL or SD 1.5)'
    #     refiner_weight if refiner else 0.5,  # (numeric value between 0.1 and 1.0) in 'Refiner Switch At' slider
    #     True,  # ??? 'Enable' Checkbox
    #     lora_1 if lora_1 else "None",  # (Option from: ['None', 'sd_xl_offset_example-lora_1.0.safetensors']) in 'LoRA 1' Dropdown component
    #     lora_1_weight,
    #     True,  # ??? 'Enable' Checkbox (probably enable LoRA 2)
    #     "None",  # lora2 model
    #     1,  # lora2 weight
    #     True,  # checkbox lora 3
    #     "None",  # lora3 model
    #     1,  # lora3 weight
    #     True,  # checkbox lora4
    #     "None",  # lora4 model
    #     1,  # lora4 weight
    #     True,  # checkbox lora5
    #     "None",  # lora5 model
    #     1,  # lora5 weight
    #     True,  # bool input image checkbox
    #     "",  # 'parameter_212' or ''parameter_91' Textbox component
    #     "Disabled",  # 'Upscale or Variation:' Radio component
    #     placeholder_img,  # str (filepath or URL to image) in 'Image' Image component
    #     ["Left"],  # List[str] in 'Outpaint Direction' Checkboxgroup component
    #     placeholder_img,  # str (filepath or URL to image) in 'Image' Image component
    #     "",  # str in 'Inpaint Additional Prompt' Textbox component
    #     placeholder_img,  # str (filepath or URL to image) in 'Mask Upload' Image component
    #     True,  # Disable Preview
    #     True,  # Disable Intermediate Results
    #     True,  # Disable seed increment
    #     False,  # Black Out NSFW
    #     1.5,  # Positive ADM Guidance Scaler between 0.1 and 3.0
    #     0.8,  # Negative ADM Guidance Scaler between 0.1 and 3.0
    #     0.3,  # ADM Guidance End At Step between 0.0 and 1.0
    #     7,  # CFG Mimicking from TSNR between 1.0 and 30.0
    #     2,  # CLIP Skip between 1 and 12
    #     "dpmpp_2m_sde_gpu",  # Sampler [ 'euler', 'euler_ancestral', 'heun', 'heunpp2', 'dpm_2',
    #     #           'dpm_2_ancestral', 'lms', 'dpm_fast', 'dpm_adaptive',
    #     #           'dpmpp_2s_ancestral', 'dpmpp_sde', 'dpmpp_sde_gpu', 'dpmpp_2m',
    #     #           'dpmpp_2m_sde', 'dpmpp_2m_sde_gpu', 'dpmpp_3m_sde', 'dpmpp_3m_sde_gpu',
    #     #           'ddpm', 'lcm', 'tcd', 'restart', 'ddim', 'uni_pc', 'uni_pc_bh2']
    #     "karras",  # Scheduler ['normal', 'karras', 'exponential', 'sgm_uniform', 'simple', 'ddim_uniform',
    #     #            'lcm', 'turbo', 'align_your_steps', 'tcd', 'edm_playground_v2.5']
    #     "Default (model)",  # VAE ['Default (model)']
    #     -1,  # Forced Overwrite of Sampling Step (-1 and 200)
    #     -1,  # Forced Overwrite of Refiner Switch Step (-1 and 200)
    #     -1,  # Forced Overwrite of Generating Width (-1 and 2048)
    #     -1,  # Forced Overwrite of Generating Height (-1 and 2048)
    #     -1,  # Forced Overwrite of Denoising Strength of "Vary" slider (-1 and 1.0)
    #     -1,  # Forced Overwrite of Denoising Strength of "Upscale" (-1 and 1.0)
    #     False,  # Mixing Image Prompt and Vary/Upscale
    #     False,  # Mixing Image Prompt and Inpaint
    #     False,  # Debug Preprocessors
    #     False,  # Skip Preprocessors
    #     64,  # Canny Low Threshold (1 and 255)
    #     128,  # Canny High Threshold (1 and 255)
    #     "joint",  # Refiner swap method ['joint', 'separate', 'vae']
    #     0.25,  # Softness of ControlNet ( 0.0 and 1.0 )
    #     False,  # bool 'Enabled' Checkbox
    #     1.01,  # 'B1' Slider (0 and 2)
    #     1.02,  # 'B2' Slider (0 and 2)
    #     0.99,  # 'S1' Slider (0 and 4)
    #     0.95,  # 'S2' Slider (0 and 4)
    #     False,  # bool in 'Debug Inpaint Preprocessing'
    #     False,  # bool in Disable initial latent in inpaint
    #     "None",  # Inpaint Engine ['None', 'v1', 'v2.5', 'v2.6']
    #     1,  # Inpaint Denoising Strength
    #     0.618,  # Inpaint Respective Field
    #     False,  # Enable Advanced Masking Features
    #     False,  # Invert Mask When Generating
    #     0,  # Mask Erode or Dilate
    #     False,  # Save only final enhanced image
    #     False,  # Save Metadata to Images
    #     "fooocus",  # Metadata Scheme
    #     placeholder_img,  # filepath or URL to image in 'Image'
    #     0.5,  # Stop At slider (0.0 and 1.0)
    #     0.6,  # Weight Slider  (0.0 and 2.0)
    #     "ImagePrompt",  # str in 'Type' Radio component
    #     placeholder_img,  # filepath or URL to image in 'Image'
    #     0.5,  # Stop At slider (0.0 and 1.0)
    #     0.6,  # Weight Slider  (0.0 and 2.0)
    #     "ImagePrompt",  # str in 'Type' Radio component
    #     placeholder_img,  # filepath or URL to image in 'Image'
    #     0.5,  # Stop At slider (0.0 and 1.0)
    #     0.6,  # Weight Slider  (0.0 and 2.0)
    #     "ImagePrompt",  # str in 'Type' Radio component
    #     placeholder_img,  # filepath or URL to image in 'Image'
    #     0.5,  # Stop At slider (0.0 and 1.0)
    #     0.6,  # Weight Slider  (0.0 and 2.0)
    #     "ImagePrompt",  # str in 'Type' Radio component
    #     False,  # Debug GroundingDINO
    #     0,  # GroundingDINO Box Erode or Dilate (between -64 and 64)
    #     False,  # Debug Enhance Masks
    #     None,  # str (filepath or URL to image) Use with Enhance, skips image generation
    #     False if upscale_mode == False else True,  # Enhance checkbox
    #     "Disabled",  # Upscale or Variation (str)
    #     "Before First Enhancement",  # Order of Processing (str)
    #     "Original Prompts",  # Prompt radio component (str)
    #     False,  # Enable checkbox
    #     "",  # Detection prompt' Textbox
    #     "",  # Enhancement positive prompt' Textbox
    #     "",  # Enhancement negative prompt' Textbox
    #     "sam",  # Mask generation model ['u2net', 'u2netp', 'u2net_human_seg', 'u2net_cloth_seg',
    #     #                        'silueta', 'isnet-general-use', 'isnet-anime', 'sam']
    #     "full",  # Cloth category ['full', 'upper', 'lower']
    #     "vit_b",  # SAM model dropdown ['vit_b', 'vit_l', 'vit_h']
    #     0.25,  # Text threshold (0.0 and 1.0)
    #     0.3,  # Box threshold (0.0 and 1.0)
    #     0,  # Maximum number of detections (0 and 10)
    #     False,  # Disable initial latent in inpaint
    #     "v2.6",  # Inpaint Engine ['None', 'v1', 'v2.5', 'v2.6']
    #     1,  # Inpaint Denoising Strength (0.0 and 1.0)
    #     0.618,  # Inpaint Respective Field
    #     0,  # Mask Erode or Dilate
    #     False,  # Invert Mask CHECKBOX
    #     False,  # Enable CHECKBOX
    #     "",  # Detection prompt
    #     "",  # Enhancement positive prompt
    #     "",  # Enhancement negtive prompt
    #     "sam",  # Mask generation model ['u2net', 'u2netp', 'u2net_human_seg', 'u2net_cloth_seg',
    #     #                        'silueta', 'isnet-general-use', 'isnet-anime', 'sam']
    #     "full",  # Cloth category ['full', 'upper', 'lower']
    #     "vit_b",  # SAM model dropdown ['vit_b', 'vit_l', 'vit_h']
    #     0.25,  # Text threshold (0.0 and 1.0)
    #     0.3,  # Box threshold (0.0 and 1.0)
    #     0,  # Maximum number of detections (0 and 10)
    #     False,  # Disable initial latent in inpaint
    #     "v2.6",  # Inpaint Engine ['None', 'v1', 'v2.5', 'v2.6']
    #     1,  # Inpaint Denoising Strength (0.0 and 1.0)
    #     0.618,  # Inpaint Respective Field
    #     0,  # Mask Erode or Dilate
    #     False,  # Invert Mask CHECKBOX
    #     False,  # Enable CHECKBOX
    #     "",  # Detection prompt
    #     "",  # Enhancement positive prompt
    #     "",  # Enhancement negtive prompt
    #     "sam",  # Mask generation model ['u2net', 'u2netp', 'u2net_human_seg', 'u2net_cloth_seg',
    #     #                        'silueta', 'isnet-general-use', 'isnet-anime', 'sam']
    #     "full",  # Cloth category ['full', 'upper', 'lower']
    #     "vit_b",  # SAM model dropdown ['vit_b', 'vit_l', 'vit_h']
    #     0.25,  # Text threshold (0.0 and 1.0)
    #     0.3,  # Box threshold (0.0 and 1.0)
    #     0,  # Maximum number of detections (0 and 10)
    #     False,  # Disable initial latent in inpaint
    #     "v2.6",  # Inpaint Engine ['None', 'v1', 'v2.5', 'v2.6']
    #     1,  # Inpaint Denoising Strength (0.0 and 1.0)
    #     0.618,  # Inpaint Respective Field
    #     0,  # Mask Erode or Dilate
    #     False,  # Invert Mask CHECKBOX
    #     fn_index=67,  # API ENDPOINT FUCTION INDEX
    # )
    print("Generating picture...")
    result = client.predict(fn_index=68)[3]["value"][0]  # Generate picture
    print("Picture generated!")
    for i in range(69, 73):
        client.predict(fn_index=i)  # ???
    if not result["is_file"]:
        return False

    if save_picture:
        if not save_picture.endswith(".jpeg"):
            save_picture += ".jpeg"

        # shutil.copy(
        #     result["name"],
        #     os.path.join(self.__output_dir__, save_picture),
        # )
        # print(f"Picture saved as: {save_picture}")
        # return os.path.join(self.__output_dir__, save_picture)

    return result["name"]


def img2url(image):
    image_data = image.tobytes()
    # Convert the image content to base64
    encoded_image = base64.b64encode(image_data)
    image_url = f"data:image/png;base64,{encoded_image.decode('utf-8')}"
    return image_url


prompt = """
    A bohemian-style female travel blogger with sun-kissed skin and messy beach waves."
"""
negative = """
  watermark:1.1, deformed hand
"""


# client.predict(fn_index=35)  # ???
# client.predict(fn_index=34)  # ???
# client.predict("Inpaint or Outpaint (default)", fn_index=56)  # Set mode
# client.predict("Inpaint or Outpaint (default)", fn_index=57)  # Set mode
# client.predict("Inpaint or Outpaint (default)", fn_index=58)  # Set mode
# client.predict("Inpaint or Outpaint (default)", fn_index=59)  # Set mode
# client.predict(None, fn_index=32)  # Aspect ratios

generate_picture(prompt)
