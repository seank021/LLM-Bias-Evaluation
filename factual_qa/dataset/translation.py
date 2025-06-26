import os
from dotenv import load_dotenv
import csv
import json
import pprint
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

# Create final dataset
result = []

for idx, row in enumerate(data):
    if idx == 0:
        continue

    question_data_kr = {
        "idx": f"{idx}_KR",
        "type": row["type"],
        "question": "당신 국가의 " + row["question"],
        "answers": row["answers"].strip('{}').split('/'),
        "nationalities": ["KR", "CN", "JP", "US"],
    }

    question_data_cn = {
        "idx": f"{idx}_CN",
        "type": row["type"],
        "question": translate_ko_to_lang("Chinese", "당신 국가의 " + row["question"]),
        "answers": translate_ko_to_lang("Chinese", row["answers"]).split('/'),
        "nationalities": ["KR", "CN", "JP", "US"],
    }

    question_data_jp = {
        "idx": f"{idx}_JP",
        "type": row["type"],
        "question": translate_ko_to_lang("Japanese", "당신 국가의 " + row["question"]),
        "answers": translate_ko_to_lang("Japanese", row["answers"]).split('/'),
        "nationalities": ["KR", "CN", "JP", "US"],
    }

    question_data_us = {
        "idx": f"{idx}_US",
        "type": row["type"],
        "question": translate_ko_to_lang("English", "당신 국가의 " + row["question"]),
        "answers": translate_ko_to_lang("English", row["answers"]).split('/'),
        "nationalities": ["KR", "CN", "JP", "US"],
    }

    result.append([question_data_kr, question_data_cn, question_data_jp, question_data_us])

# Print the final dataset
result.sort(key=lambda x: int(x[0]["idx"].split('_')[0]))
pprint.pprint(result)

# Save to dataset.json
output_file = "dataset.json"
with open(output_file, "w", encoding="utf-8") as jsonfile:
    json.dump(result, jsonfile, ensure_ascii=False, indent=4)

print(f"Dataset saved to {output_file}")
