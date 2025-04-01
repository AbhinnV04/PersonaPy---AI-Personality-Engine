"""
src/assets/character_handler.py
============================

"""

from utils.decorators import internal_test, core_function

@core_function
def ParseTextDialogues(file=None) -> list[str]:
    """ Function to read from <dialogue file>.txt file and parse the text. """
    raise NotImplementedError

@core_function
def ParseJSONDialogues(file=None) -> list[str]:
    raise NotImplementedError

@core_function
def ParseJSONPersonality(file=None) -> dict[str, str]:
    raise NotImplementedError

""" --------------------- """

@internal_test
def testParseTextDialogues():
    """ Tests Dialogue test parsing """
    try:
        file = r"assets\Angie\angie_dialogue.txt"
        res = ParseTextDialogues(file)
        
        txt = []
        with open(file, "r") as f:
            for line in f:
                txt.append(line)
    except Exception as e:
        res = None
        txt = None

    if res and txt:
        print(res, txt)
    else:
        print("Test Failed")

@internal_test
def testParseJSONDialogues(file=None) -> list[str]:
    raise NotImplementedError

@internal_test
def testParseJSONPersonality(file=None) -> dict[str, str]:
    raise NotImplementedError

""" --------------------- """

if __name__ == "__main__":
    try:
        testParseTextDialogues()
    except NotImplementedError:
        print(f"Text Dialogue parser not implemented")
    except Exception as e:
        print(f"Error in Text Dialogue Parser {e}")

    try:
        testParseJSONDialogues()
    except NotImplementedError:
        print(f"JSON Dialogue parser not implemented")
    except Exception as e:
        print(f"Error in Text Dialogue Parser {e}")
        
    try:
        testParseJSONPersonality()
    except NotImplementedError:
        print(f"JSON Personality parser not implemented")
    except Exception as e:
        print(f"Error in Text Dialogue Parser {e}")
        