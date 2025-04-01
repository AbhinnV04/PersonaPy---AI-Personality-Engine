"""
/src/scripts/model_handler.py
============================

Handles model connection
- GetResponseAPI: Connects to the model API and retrieves a response.
- GetOllamaResponse: Connects to the Ollama model and retrieves a response.
- testAPIResponse: Tests the API response by calling GetResponseAPI and printing the output.
- testOllamaResponse: Tests the Ollama response by calling GetOllamaResponse and printing the output.
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

@core_function
def GetOllamaResponse(prompt_vars: dict[str, str] | None = None) -> dict[str]:
    """ Function to get response from local ollama model. """
    raise NotImplementedError

""" ---------------------------- """

@internal_test
def testAPIResponse():
    output = GetResponseAPI()
    if output:
        print(f"API Response: {output}")
    else:
        print("Test Failed: No output from API.")
        
@internal_test
def testOllamaResponse():
    """ GetOllamaResponse function to get the response from the Ollama model. """
    raise NotImplementedError

""" -------------------------- """

if __name__ == "__main__":
    """ This block is for testing the function directly. And Learning purposes. """
    # testAPIResponse()
    testOllamaResponse()
