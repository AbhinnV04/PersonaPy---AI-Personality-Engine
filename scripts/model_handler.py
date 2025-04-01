"""
/src/scripts/model_handler.py
"""
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

from utils.decorators import internal_test, core_function

@core_function
def GetResponseAPI(prompt_vars: dict[str, str] | None = None) -> dict[str]:
    """ GetResponseAPI function to get the response from the model API. """
    load_dotenv()
    HF_API_KEY = os.getenv("API_KEY")
    MODEL = "mistralai/Mistral-7B-Instruct-v0.3"
    
    client = InferenceClient(model=MODEL, token=HF_API_KEY)
    
    prompt = "Say Hi"
    response = client.text_generation(prompt, max_new_tokens=200)
    return response

@internal_test
def testAPIResponse():
    output = GetResponseAPI()
    if output:
        print(f"API Response: {output}")
    else:
        print("Test Failed: No output from API.")

if __name__ == "__main__":
    """ This block is for testing the function directly. And Learning purposes. """
    testAPIResponse()
    