import os
from dotenv import load_dotenv
import csv
import copy
import json
from openai import OpenAI
import openai

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

def translate_ko_to_lang(lang, text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": "Translate the following Korean text to {language}: {text}".format(language=lang, text=text)}
        ]
    )

    return response.choices[0].message.content

# Read the csv file
input_file = '/dataset/questions.csv'
data = []

with open(input_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

def fill_translations(data, langs=["CN", "JP", "US"]):
    translated_data = copy.deepcopy(data)

    for group in translated_data:
        for idx, entry in enumerate(group):
            if entry["idx"].endswith("_KR"):
                kr_questions = entry["questions"]

                for lang in langs:
                    lang_entry = {
                        "idx": entry["idx"].replace("_KR", f'_{lang}'),
                        "questions": []
                    }

                    for question in kr_questions:
                        translated_question = translate_ko_to_lang(lang, question["question"])
                        translated_answers = [translate_ko_to_lang(lang, ans) if ans != "null" else "null" for ans in question["answers"]]

                        lang_entry["questions"].append({
                            "type": question["type"],
                            "question": translated_question,
                            "answers": translated_answers,
                            "related_countries": question["related_countries"],
                            "nationalities": question["nationalities"],
                            "language": lang
                        })

                    group.append(lang_entry)
    return translated_data

filled_data = fill_translations(data)

# Save to dataset.json
output_file = "dataset.json"
with open(output_file, "w", encoding="utf-8") as jsonfile:
    json.dump(filled_data, jsonfile, ensure_ascii=False, indent=4)

print(f"Dataset saved to {output_file}")
