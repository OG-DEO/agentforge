import json


def extract_json(text):
    text = text.strip()

    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("No JSON object found.")

    candidate = text[start:end + 1]

    return json.loads(candidate)
