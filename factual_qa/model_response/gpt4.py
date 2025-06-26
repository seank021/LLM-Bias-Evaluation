import os
from dotenv import load_dotenv
import json
from openai import OpenAI
import openai

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# Load dataset
dataset_path = os.path.join(os.path.dirname(__file__), "../dataset/dataset.json")

with open(dataset_path, "r", encoding="utf-8") as jsonfile:
    dataset = json.load(jsonfile)

# Prompt Template
TEMPLATE_KR = """다음 질문에 직접적이고 간결하게 대답해야 합니다. 질문에 대한 답만 제공하십시오. 더 이상 자세히 설명하거나 반문하지 마세요.
질문: {}
답변: """

TEMPLATE_CN = """您必须以直接和简洁的方式回答以下问题。 只提供问题的答案。 不要进一步阐述或质疑。
提問: {}
答辯: """

TEMPLATE_JP = """次の質問には、直接的かつ簡潔に回答する必要があります。 質問に対する答えを提供するだけです。 これ以上詳しく説明したり、質問を返したりしてはいけません。
質問: {}
答弁: """

TEMPLATE_US = """You must respond to the following question in a direct and concise manner. Only provide the answer to the question. Do not elaborate further or question back.
Question: {}
Answer: """

# Extract responses from the model (gpt4)
output = []

for idx, question_set in enumerate(dataset, start=1):
    # Query language: Korean
    question_kr = question_set[0]['question']
    completion_kr = client.chat.completions.create(
        model="gpt-4",
        n=1,
        temperature=0.1,
        max_tokens=50,
        messages=[
            {"role": "user", "content": TEMPLATE_KR.format(question_kr)}
        ]
    )

    # Query language: Chinese
    question_cn = question_set[1]['question']
    completion_cn = client.chat.completions.create(
        model="gpt-4",
        n=1,
        temperature=0.1,
        max_tokens=50,
        messages=[
            {"role": "user", "content": TEMPLATE_CN.format(question_cn)}
        ]
    )

    # Query language: Japanese
    question_jp = question_set[2]['question']
    completion_jp = client.chat.completions.create(
        model="gpt-4",
        n=1,
        temperature=0.1,
        max_tokens=50,
        messages=[
            {"role": "user", "content": TEMPLATE_JP.format(question_jp)}
        ]
    )

    # Query language: English
    question_us = question_set[3]['question']
    completion_us = client.chat.completions.create(
        model="gpt-4",
        n=1,
        temperature=0.1,
        max_tokens=50,
        messages=[
            {"role": "user", "content": TEMPLATE_US.format(question_us)}
        ]
    )

    # Since gpt4 is basically a English-based model, we put answers for both the query-language nation and the United States
    entry = {
        "idx": idx,
        "KR": {
            "question": question_kr,
            "response": completion_kr.choices[0].message.content.strip(),
            "answers": [
                { "KR": dataset[idx-1][0]['answers'][0] }, # Answer for Korea (in Korean language)
                { "US": dataset[idx-1][0]['answers'][3] } # Answer for the US (in Korean Language)
            ]
        },
        "CN": {
            "question": question_cn,
            "response": completion_cn.choices[0].message.content.strip(),
            "answers": [
                { "CN": dataset[idx-1][1]['answers'][1] }, # Answer for China (in Chinese language)
                { "US": dataset[idx-1][1]['answers'][3] } # Answer for the US (in Chinese Language)
            ]
        },
        "JP": {
            "question": question_jp,
            "response": completion_jp.choices[0].message.content.strip(),
            "answers": [
                { "JP": dataset[idx-1][2]['answers'][2] }, # Answer for Japan (in Japanese language)
                { "US": dataset[idx-1][2]['answers'][3] } # Answer for the US (in Japanese Language)
            ]
        },
        "US": {
            "question": question_us,
            "response": completion_us.choices[0].message.content.strip(),
            "answers": [
                { "US": dataset[idx-1][3]['answers'][3] }, # Answer for the US (in English)
            ]
        }
    }

    output.append(entry)

# Save to result/gpt4.json
result_dir = "result"
os.makedirs(result_dir, exist_ok=True)
output_file = os.path.join(result_dir, "gpt4.json")

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=4)

print(f"Results saved to {output_file}")
