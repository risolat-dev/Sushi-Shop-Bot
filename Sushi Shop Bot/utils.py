import json

with open("translations.json", "r", encoding="utf-8") as f:
    TRANSLATIONS = json.load(f)

def translate(lang, key, **kwargs):
    text = TRANSLATIONS.get(lang, TRANSLATIONS["uz"]).get(key, "")
    return text.format(**kwargs)

def load_menu():
    with open("menu.json", "r", encoding="utf-8") as f:
        return json.load(f)

def calculate_total(items):
    return sum(item['price'] for item in items)
