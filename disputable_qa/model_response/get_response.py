import os
from dotenv import load_dotenv
import json

load_dotenv()

# If model is gpt4, use this code below
'''
import openai
from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)
'''

# Else, use this code - using lab server
from openai import OpenAI

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY"),
)

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

# Extract responses from the model
def get_response(model_name, question_type, question_text, lang):
    if lang == "KR":
        TEMPLATE = TEMPLATE_KR
    elif lang == "CN":
        TEMPLATE = TEMPLATE_CN
    elif lang == "JP":
        TEMPLATE = TEMPLATE_JP
    else:
        TEMPLATE = TEMPLATE_US

    response = client.chat.completions.create(
        model=model_name,
        n=1,
        temperature=0.1,
        max_tokens=1500,
        stop=["\n"],
        messages=[{"role": "user", "content": TEMPLATE.format(question_type, question_text)}]
    )

    return response.choices[0].message.content.strip()

'''
model_name, output_file
KR: "MLP-KTLim/llama-3-Korean-Bllossom-8B", "kr.json"
CN: "Qwen/Qwen1.5-7B", "cn.json"
JP: "Rakuten/RakutenAI-7B", "jp.json"
US: "meta-llama/Meta-Llama-3-8B", "us.json"
gpt4: "gpt-4", "gpt4.json"'
'''
model_name = "choose-from-above"
result_dir = "result"
os.makedirs(result_dir, exist_ok=True)
output_file = os.path.join(result_dir, "choose-from-above")

results = []

for entry_set in dataset:
    for entry in entry_set:
        idx = entry["idx"]
        questions = entry["questions"]

        result_entry = {
            "idx": idx,
            "answers": []
        }

        for question_data in questions:
            model_name = model_name
            response = get_response(model_name, question_data["type"], question_data["question"], question_data["language"])

            each_entry = {
                "question": question_data["question"],
                "type": question_data["type"],
                "response": response,
                "related_countries": question_data["related_countries"],
                "answers": question_data["answers"],
                "nationalities": question_data["nationalities"]
            }
            result_entry["answers"].append(each_entry)

        results.append(result_entry)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print(f"Results saved to {output_file}")
