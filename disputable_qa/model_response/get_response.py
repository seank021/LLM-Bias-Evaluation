import os
import json

# If model is ChatGPT, use this code below
'''
import openai
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "keep-it-secret"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))'
'''

# Else, use this code
from openai import OpenAI

client = OpenAI(
    base_url="keep-it-secret",
    api_key="keep-it-secret",
)

# Load dataset
dataset_path = os.path.join(os.path.dirname(__file__), "../dataset/dataset.json")

with open(dataset_path, "r", encoding="utf-8") as jsonfile:
    dataset = json.load(jsonfile)

# Prompt Template
TEMPLATE_KR = """이 질문은 {} 질문입니다. 당신은 직접적이고 간결하게 대답해야 합니다. 질문에 대한 답만 제공하십시오. 더 이상 자세히 설명하거나 반문하지 마세요. 제시된 답변 중 고르라는 질문에 대하여는 꼭 제시된 답변들 중 하나를 고르시오. 특히 PERSONA, TF, CHOICE 질문에 대해서는 꼭 명확한 답 하나를 골라 답변하시오.
질문: {}
답변: """

TEMPLATE_CN = """這個問題是{} 是提問。 你要直接簡潔地回答。 請只提供問題的答案。 請不要再詳細說明或反問了。 對於在提出的回答中選擇的問題,請務必在提出的回答中選擇其一。 特別是對於PERSONA、TF、CHOICE的問題，一定要選擇一個明確的答案來回答。
提問: {}
答辯: """

TEMPLATE_JP = """この質問は{} 質問です。 あなたは直接的かつ簡潔に答えなければなりません。 質問に対する答えだけを提供してください。 これ以上詳しく説明したり、反問したりしないでください。 提示された回答の中から選びなさいという質問に対しては、必ず提示された回答の中から一つを選びなさい。 特に、PERSONA、TF、CHOICEの質問に対しては、必ず明確な答えを一つ選んで答えなさい。
質問: {}
答弁: """

TEMPLATE_US = """This question is {}. You have to answer the question directly and concisely. Just provide answers to the questions. Do not elaborate or ask questions in more detail. When it comes to the question to choose, be sure to choose one of the answers. Especially for PERSONA, TF, and CHOICE questions, be sure to choose one clear answer and answer it.
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
ChatGPT: "gpt-4", "chatgpt.json"'
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
