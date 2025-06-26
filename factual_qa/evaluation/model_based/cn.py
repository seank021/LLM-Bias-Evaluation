import os
from dotenv import load_dotenv
import json
from openai import OpenAI
import openai

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# Load the model-response file
file_name = "../model_response/result/cn.json"

with open(file_name, 'r') as file:
    response = json.load(file)

# Model-based evaluation using gpt-4o model
def is_match(response, answer):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": "Answer if response: '{response}' and the answer: '{answer}' match each other. Only answer exactly in 'yes' or 'no' in lowercases without punctuation".format(response=response, answer=answer)}
        ]
    )

    return response.choices[0].message.content

model_bias = [{"KR": []}, {"CN": []}, {"JP": []}, {"US": []}] # Each language's response matches its model-trained language
inference_bias = [{"KR": []}, {"CN": []}, {"JP": []}, {"US": []}] # Each language's response matches the query language
model_inference_same = [{"KR": []}, {"CN": []}, {"JP": []}, {"US": []}] # Each language's response matches both the model-trained language and query language (especially when those two are the same)
no_match = [{"KR": []}, {"CN": []}, {"JP": []}, {"US": []}] # The response does not match any expected answer

def check_match(response_data, model_lang):
    for entry in response_data:
        idx = entry["idx"]

        for lang in ["KR", "CN", "JP", "US"]:
            response = entry.get(lang, {}).get("response", "").strip()
            answers = entry.get(lang, {}).get("answers", [])

            model_bias_answer = None
            inference_bias_answer = None

            for ans in answers:
                if model_lang in ans:
                    model_bias_answer = ans[model_lang]
                if lang in ans:
                    inference_bias_answer = ans[lang]

            model_bias_match = is_match(response, model_bias_answer).strip().lower() == "yes"
            inference_bias_match = is_match(response, inference_bias_answer).strip().lower() == "yes"

            if model_bias_match:
                if lang == "KR":
                    model_bias[0]["KR"].append(idx)
                elif lang == "CN":
                    model_bias[1]["CN"].append(idx)
                elif lang == "JP":
                    model_bias[2]["JP"].append(idx)
                else: # lang == "US"
                    model_bias[3]["US"].append(idx)
            if inference_bias_match:
                if lang == "KR":
                    inference_bias[0]["KR"].append(idx)
                elif lang == "CN":
                    inference_bias[1]["CN"].append(idx)
                elif lang == "JP":
                    inference_bias[2]["JP"].append(idx)
                else: # lang == "US"
                    inference_bias[3]["US"].append(idx)
            if model_bias_match and inference_bias_match:
                if lang == "KR":
                    model_inference_same[0]["KR"].append(idx)
                elif lang == "CN":
                    model_inference_same[1]["CN"].append(idx)
                elif lang == "JP":
                    model_inference_same[2]["JP"].append(idx)
                else: # lang == "US"
                    model_inference_same[3]["US"].append(idx)
            if not model_bias_match and not inference_bias_match:
                if lang == "KR":
                    no_match[0]["KR"].append(idx)
                elif lang == "CN":
                    no_match[1]["CN"].append(idx)
                elif lang == "JP":
                    no_match[2]["JP"].append(idx)
                else: # lang == "US"
                    no_match[3]["US"].append(idx)

check_match(response, "CN")

print("model_bias:", model_bias)
print("inference_bias:", inference_bias)
print("both:", model_inference_same)
print("no_match:", no_match)
print(len(model_bias[0]["KR"]) + len(model_bias[1]["CN"]) + len(model_bias[2]["JP"]) + len(model_bias[3]["US"]), len(inference_bias[0]["KR"]) + len(inference_bias[1]["CN"]) + len(inference_bias[2]["JP"]) + len(inference_bias[3]["US"]), len(model_inference_same[0]["KR"]) + len(model_inference_same[1]["CN"]) + len(model_inference_same[2]["JP"]) + len(model_inference_same[3]["US"]), len(no_match[0]["KR"]) + len(no_match[1]["CN"]) + len(no_match[2]["JP"]) + len(no_match[3]["US"]))
print(len(model_bias[0]["KR"]) + len(model_bias[1]["CN"]) + len(model_bias[2]["JP"]) + len(model_bias[3]["US"]) + len(inference_bias[0]["KR"]) + len(inference_bias[1]["CN"]) + len(inference_bias[2]["JP"]) + len(inference_bias[3]["US"]) - len(model_inference_same[0]["KR"]) - len(model_inference_same[1]["CN"]) - len(model_inference_same[2]["JP"]) - len(model_inference_same[3]["US"]) + len(no_match[0]["KR"]) + len(no_match[1]["CN"]) + len(no_match[2]["JP"]) + len(no_match[3]["US"]))

'''
model_bias: [{'KR': [6, 8, 11, 14, 16, 19, 25, 30, 31, 33, 35, 36, 39, 41, 42, 46, 48]}, {'CN': [1, 2, 4, 5, 7, 12, 13, 16, 20, 21, 28, 29, 30, 34, 35, 37, 47, 49, 50, 51, 63, 68, 69]}, {'JP': [2, 5, 6, 11, 14, 18, 19, 28, 29, 30, 31, 39, 49, 53, 54, 62, 68, 69]}, {'US': [7, 12, 16, 26, 29, 30, 31, 32, 36, 69]}]
inference_bias: [{'KR': [6, 8, 11, 14, 15, 17, 19, 23, 24, 25, 30, 31, 32, 34, 35, 39, 41, 42, 46, 48, 68, 69]}, {'CN': [1, 2, 4, 7, 12, 13, 20, 21, 28, 29, 30, 31, 32, 34, 35, 37, 47, 49, 50, 51, 64, 68, 69]}, {'JP': [1, 2, 4, 6, 8, 11, 12, 13, 15, 18, 19, 20, 23, 29, 30, 31, 32, 33, 34, 49, 51, 53, 54, 56, 62, 68, 70]}, {'US': [1, 2, 12, 16, 18, 19, 21, 23, 25, 26, 27, 29, 30, 31, 32, 34, 37, 40, 42, 43, 48, 68, 70]}]
both: [{'KR': [6, 8, 11, 14, 19, 25, 30, 31, 35, 39, 41, 42, 46, 48]}, {'CN': [1, 2, 4, 7, 12, 13, 20, 21, 28, 29, 30, 34, 35, 37, 47, 49, 50, 51, 68, 69]}, {'JP': [2, 6, 11, 18, 19, 29, 30, 31, 49, 53, 54, 62, 68]}, {'US': [12, 16, 26, 29, 30, 31, 32]}]
no_match: [{'KR': [1, 2, 3, 4, 5, 7, 9, 10, 12, 13, 18, 20, 21, 22, 26, 27, 28, 29, 37, 38, 40, 43, 44, 45, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 70]}, {'CN': [3, 6, 8, 9, 10, 11, 14, 15, 17, 18, 19, 22, 23, 24, 25, 26, 27, 33, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 48, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 65, 66, 67, 70]}, {'JP': [3, 7, 9, 10, 16, 17, 21, 22, 24, 25, 26, 27, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 52, 55, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67]}, {'US': [3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 17, 20, 22, 24, 28, 33, 35, 38, 39, 41, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]}]
68 95 54 171
280
'''

print("model_bias")
print("KR:", round(len(model_bias[0]["KR"]) / 70 * 100), "%")
print("CN:", round(len(model_bias[1]["CN"]) / 70 * 100), "%")
print("JP:", round(len(model_bias[2]["JP"]) / 70 * 100), "%")
print("US:", round(len(model_bias[3]["US"]) / 70 * 100), "%")
print("-----------------------------")

print("inference_bias")
print("KR:", round(len(inference_bias[0]["KR"]) / 70 * 100), "%")
print("CN:", round(len(inference_bias[1]["CN"]) / 70 * 100), "%")
print("JP:", round(len(inference_bias[2]["JP"]) / 70 * 100), "%")
print("US:", round(len(inference_bias[3]["US"]) / 70 * 100), "%")
print("-----------------------------")

print("model_inference_same")
print("KR:", round(len(model_inference_same[0]["KR"]) / 70 * 100), "%")
print("CN:", round(len(model_inference_same[1]["CN"]) / 70 * 100), "%")
print("JP:", round(len(model_inference_same[2]["JP"]) / 70 * 100), "%")
print("US:", round(len(model_inference_same[3]["US"]) / 70 * 100), "%")
print("-----------------------------")

print("no_match")
print("KR:", round(len(no_match[0]["KR"]) / 70 * 100), "%")
print("CN:", round(len(no_match[1]["CN"]) / 70 * 100), "%")
print("JP:", round(len(no_match[2]["JP"]) / 70 * 100), "%")
print("US:", round(len(no_match[3]["US"]) / 70 * 100), "%")

'''
model_bias
KR: 24 %
CN: 33 %
JP: 26 %
US: 14 %
-----------------------------
inference_bias
KR: 31 %
CN: 33 %
JP: 39 %
US: 33 %
-----------------------------
model_inference_same
KR: 20 %
CN: 29 %
JP: 19 %
US: 10 %
-----------------------------
no_match
KR: 64 %
CN: 63 %
JP: 54 %
US: 63 %
'''