from enum import Enum


class HfInferenceAPI(Enum):
    FLUX_DEV = 'https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev'
    OPENFLUX_V1 = 'https://api-inference.huggingface.co/models/ostris/OpenFLUX.1'
    FLUX_CONTROLNET_API_URL = "https://api-inference.huggingface.co/models/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro"
    SDXL_CONTROLNET_API_URL = "https://api-inference.huggingface.co/models/xinsir/controlnet-union-sdxl-1.0"
    JUGXL_CONTROLNET_API_URL = "https://api-inference.huggingface.co/models/TheMistoAI/MistoLine"

class HfSpacesAPI(Enum):
    SHAKKER_FLUX1_DEV_DARK_FANTASY = ("Fili2a2/FLUX.1-dev-LoRA-Dark-Fantasy", "/predict")

