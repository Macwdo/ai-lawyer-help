import json
import os

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


# from langchain.chains.summarize import load_summarize_chain
from ai.services.ai.llm import LLMService, OllamaModels
from ai.services.pdf_manager import PDFManager

pdf = PDFManager()
text = open("tmp/texts/imprensa_2_text.txt", "r").read()

llm = LLMService().get_reasoning_llm(model=OllamaModels.GEMMA3_12B)


def break_lines(text: str):
    return text.split("\n")


def match_json(response_prompt: str, original_text: str):
    """
    Try match a json in the text.
    """

    # Json dumps
    try:
        match = json.loads(response_prompt)["phrase"]
        return match

    except Exception as e:
        print("Error trying to match json.", e)

    return original_text


def fixed_line(line: str, phrase: str, foward_line: str):
    prompt = """
    You are a PDF reader. You are a phrase extracted from a PDF file.
    I will give you a phrase, preview line and foward line of a pdf.
    
    You should just fix it.
    
    Preview line: __preview_line__
    
    Phrase: __phrase__
    
    Foward line: __foward_line__
    
    Fix the phrase.
    You must not change or complete the phrase, just fix language errors.
    You must return a json with the following structure:
    
    
    json```
    { 
        "phrase": "your fixed phrase"
    }
    ```
    
    
    Do not return anything else than the fixed phrase in the json.
    Do not return any additional information.
    """

    prompt = (
        prompt.replace("__preview_line__", line)
        .replace("__phrase__", phrase)
        .replace("__foward_line__", foward_line)
    )

    res = llm.invoke(prompt)
    return res


text = break_lines(text)
text = [t for t in text if t]

fixed_text = []

for i in range(len(text)):
    prev = text[i - 1] if i > 0 else ""
    line = text[i]
    foward = text[i + 1] if i < len(text) - 1 else ""

    print("---------------------------------------------------")
    print("Preview line: ", prev)
    print("Line: ", line)
    print("Foward line: ", foward)

    res = fixed_line(prev, line, foward)
    response = match_json(res, line)
    print("---------------------------------------------------")
    print("Fixed line: ", response)

    fixed_text.append(response)

for i, line in enumerate(fixed_text):
    print("Fixed line: ", line)
