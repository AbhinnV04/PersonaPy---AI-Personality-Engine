"""
/assets/serve_asset_details.py
========================

-This module contains a function to fetch available assets from a JSON file. 
    It includes a test function to verify the functionality of the main function.

- TO RUN / TEST: "python -m assets.serve_asset_details.py"
    directly from the command line in the source directory.
    
- Decorator functions are used to mark core functions, which are the actual endpoints /
    and internal test functions, only meant for internal use.
"""

import json
import os
import sys

from utils.decorators import core_function, internal_test

@core_function
def fetch_available_assets():
    file_path = os.path.join(os.path.dirname(__file__), "available_assets.json")
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    
    except FileNotFoundError:
        print("Error: 'available_assets.json' not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from 'available_assets.json'.")
        return None

@internal_test
def test_fetch_available_assets():
    """ Test function to verify the functionality of fetch_available_assets """
    assets = fetch_available_assets()
    
    if assets:
        for id, asset in assets.items():
            print(f"asset id: {id}:  \nitems:{asset}\n")
    else:
        print("---Test failed: No assets fetched.---") 
    
    
if __name__ == "__main__":
    """ This block is for testing the function directly. And Learning purposes. """
    test_fetch_available_assets()
