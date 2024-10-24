import requests
import google.generativeai as genai
# from diffusers import DiffusionPipeline


from gradio_client import Client
from models.model_list import HfInferenceAPI, HfSpacesAPI

from utils import *

##### Update WARNINGS in Environment
import os
# Increase the evaluation timeout to 10 seconds
os.environ['PYDEVD_WARN_EVALUATION_TIMEOUT'] = '130'
# Set the unblock threads timeout to 5 seconds
os.environ['PYDEVD_UNBLOCK_THREADS_TIMEOUT'] = '10'


# Configure the logging
import logging 
logging.basicConfig(level=logging.DEBUG)


from dotenv import load_dotenv
load_dotenv()

HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API')
GEMINI_API_KEY = os.getenv('GEMINI_API')
STABILITY_API_KEY = os.getenv('STABILITY_API')

if not HUGGINGFACE_API_KEY:
    raise ValueError("No HUGGINGFACE_API_KEY found in environment variables.")
if not GEMINI_API_KEY:
    raise ValueError("No GEMINI_API_KEY found in environment variables.")
if not STABILITY_API_KEY:
    raise ValueError("No STABILITY_API_KEY found in environment variables.")


class GeminiWrapper():
    def __init__(self, api_key:str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def get_enhance_prompt(self, prompt: str):
        return f"Improve the following prompt by adding appropriate \
                high resolution and more details to the scene \
                with well contrained camera quality like focal length, \
                iso etc: \n {prompt}"

    def predict(self, prompt: str):
        response = self.model.generate_content(
                        self.get_enhance_prompt(prompt)
                    ).text
        return response
        

gemini = GeminiWrapper(api_key=GEMINI_API_KEY)

def generate_prompt(prompt:str) -> str:
    enhanced_prompt = gemini.predict(prompt)
    return enhanced_prompt




class HfInferenceWrapper():
    _headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    
    def query_hf_inference(inference_engine: HfInferenceAPI, payload:dict):
        response = requests.post(inference_engine.value, headers=HfInferenceWrapper._headers, json=payload)
        return response.content


def generate_image_from_inference(inference_engine: HfInferenceAPI, prompt: str):
    incept_image_bytes = HfInferenceWrapper.query_hf_inference(
        inference_engine=inference_engine,
        payload={
            "inputs": prompt,
        }
    )
    # incept_image = bytes_to_pil(incept_image_bytes)
    # logging.debug(incept_image)

    return incept_image_bytes




class HfSpacesWrapper():
    def predict(space_api:HfSpacesAPI, prompt:str):
        client = Client(space_api.value[0])
        result = client.predict(
                param_0=prompt,
                api_name=space_api.value[1]
        )
        return result
    
def generate_image_from_spaces(client:HfSpacesAPI, prompt:str):
    result = HfSpacesWrapper.predict(client, prompt)
    logging.debug(result)
    return result



if __name__=='__main__':
    prompt = "create a wrapper for a chocolate for a birthday girl with her picture on it. And add a tag 'still doing tricks at 56'"
    enhanced_prompt = generate_prompt(prompt)

    # oflux = generate_image(HfInferenceAPI.OPENFLUX_V1, enhanced_prompt)
    flux_dev = generate_image_from_inference(HfInferenceAPI.FLUX_DEV, enhanced_prompt)
    incept_image = bytes_to_pil(flux_dev)
    logging.debug(incept_image)


    flux_dark = generate_image_from_spaces(HfSpacesAPI.SHAKKER_FLUX1_DEV_DARK_FANTASY, enhanced_prompt)


