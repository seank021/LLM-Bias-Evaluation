import os
from dotenv import load_dotenv
import json
from openai import OpenAI
import openai

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# Load the model-response file
file_name = "../model_response/result/us.json"

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

check_match(response, "US")

print("model_bias:", model_bias)
print("inference_bias:", inference_bias)
print("both:", model_inference_same)
print("no_match:", no_match)
print(len(model_bias[0]["KR"]) + len(model_bias[1]["CN"]) + len(model_bias[2]["JP"]) + len(model_bias[3]["US"]), len(inference_bias[0]["KR"]) + len(inference_bias[1]["CN"]) + len(inference_bias[2]["JP"]) + len(inference_bias[3]["US"]), len(model_inference_same[0]["KR"]) + len(model_inference_same[1]["CN"]) + len(model_inference_same[2]["JP"]) + len(model_inference_same[3]["US"]), len(no_match[0]["KR"]) + len(no_match[1]["CN"]) + len(no_match[2]["JP"]) + len(no_match[3]["US"]))
print(len(model_bias[0]["KR"]) + len(model_bias[1]["CN"]) + len(model_bias[2]["JP"]) + len(model_bias[3]["US"]) + len(inference_bias[0]["KR"]) + len(inference_bias[1]["CN"]) + len(inference_bias[2]["JP"]) + len(inference_bias[3]["US"]) - len(model_inference_same[0]["KR"]) - len(model_inference_same[1]["CN"]) - len(model_inference_same[2]["JP"]) - len(model_inference_same[3]["US"]) + len(no_match[0]["KR"]) + len(no_match[1]["CN"]) + len(no_match[2]["JP"]) + len(no_match[3]["US"]))

'''
model_bias: [{'KR': [3, 7, 11, 16, 17, 20, 26, 29, 30, 37, 40, 47, 49, 50, 59, 61]}, {'CN': [21, 23, 25, 26, 27, 29, 30, 35, 42, 44, 50, 62, 63]}, {'JP': [12, 16, 25, 26, 27, 30, 31, 32, 33, 49, 50, 59, 61, 62]}, {'US': [1, 2, 4, 11, 12, 13, 16, 18, 19, 20, 28, 30, 31, 32, 33, 34, 37, 43, 48, 49, 51, 60, 62, 63]}]
inference_bias: [{'KR': [1, 2, 4, 5, 6, 7, 12, 15, 16, 17, 21, 23, 24, 25, 27, 30, 31, 36, 44, 46, 49, 50, 58, 61, 62, 68, 69, 70]}, {'CN': [1, 2, 4, 6, 7, 8, 12, 15, 19, 20, 22, 23, 30, 31, 33, 35, 37, 42, 44, 46, 49, 51, 56, 61, 62, 63, 69]}, {'JP': [1, 2, 6, 8, 12, 13, 16, 17, 20, 21, 24, 29, 30, 31, 32, 33, 42, 61, 69]}, {'US': [2, 4, 12, 13, 16, 19, 20, 23, 28, 30, 31, 32, 33, 34, 37, 48, 49, 51, 62, 63]}]
both: [{'KR': [7, 16, 17, 30, 49, 50, 61]}, {'CN': [23, 30, 35, 42, 44, 62, 63]}, {'JP': [12, 16, 30, 31, 32, 33, 61]}, {'US': [2, 4, 12, 13, 16, 19, 20, 28, 30, 31, 32, 33, 34, 37, 48, 49, 51, 62, 63]}]
no_match: [{'KR': [8, 9, 10, 13, 14, 18, 19, 22, 28, 32, 33, 34, 35, 38, 39, 41, 42, 43, 45, 48, 51, 52, 53, 54, 55, 56, 57, 60, 63, 64, 65, 66, 67]}, {'CN': [3, 5, 9, 10, 11, 13, 14, 16, 17, 18, 24, 28, 32, 34, 36, 38, 39, 40, 41, 43, 45, 47, 48, 52, 53, 54, 55, 57, 58, 59, 60, 64, 65, 66, 67, 68, 70]}, {'JP': [3, 4, 5, 7, 9, 10, 11, 14, 15, 18, 19, 22, 23, 28, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 51, 52, 53, 54, 55, 56, 57, 58, 60, 63, 64, 65, 66, 67, 68, 70]}, {'US': [3, 5, 6, 7, 8, 9, 10, 14, 15, 17, 21, 22, 24, 25, 26, 27, 29, 35, 36, 38, 39, 40, 41, 42, 44, 45, 46, 47, 50, 52, 53, 54, 55, 56, 57, 58, 59, 61, 64, 65, 66, 67, 68, 69, 70]}]
67 94 40 159
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
KR: 23 %
CN: 19 %
JP: 20 %
US: 34 %
-----------------------------
inference_bias
KR: 40 %
CN: 39 %
JP: 27 %
US: 29 %
-----------------------------
model_inference_same
KR: 10 %
CN: 10 %
JP: 10 %
US: 27 %
-----------------------------
no_match
KR: 47 %
CN: 53 %
JP: 63 %
US: 64 %
'''