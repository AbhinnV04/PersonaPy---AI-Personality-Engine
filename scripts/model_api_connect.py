from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

def GetResponseAPI(prompt_vars: dict[str, str]):   
    # load_dotenv()
    # HF_API_KEY = os.getenv("API_KEY")

    # MODEL = "mistralai/Mistral-7B-Instruct-v0.3"

    # client = InferenceClient(model=MODEL, token=HF_API_KEY)
    # prompt = "Say Hi"
    # response = client.text_generation(prompt, max_new_tokens=200)

    # print("Dhoni:", response)
    raise NotImplementedError


# if __name__ == "__main__":
    # pass
