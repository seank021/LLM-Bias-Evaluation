# no_match_gpt4 for all languages: [9, 20, 28, 38, 39, 40, 42, 45, 46, 54, 55, 56, 57, 58, 59, 64]
# Main reason for no_match in gpt4: The AI claims it cannot provide an answer because it does not belong to a specific country.
# If the AI states that it cannot answer due to not having a specific country but uses the US as an example, it is categorized as a US response.

model_bias_gpt4 = [
    { "KR": [5, 16, 17, 18, 23, 29, 30, 31, 32, 33, 34, 49, 52, 53, 62, 63, 67, ]},
    { "CN": [12, 16, 17, 23, 26, 29, 30, 31, 32, 33, 49, 50, 62, ]},
    { "JP": [3, 16, 17, 18, 23, 25, 27, 29, 30, 31, 32, 33, 34, 49, 50, ]},
    { "US": [1, 2, 4, 6, 7, 12, 13, 14, 15, 16, 17, 21, 22, 23, 25, 26, 27, 29, 30, 31, 32, 35, 43, 44, 48, 49, 51, 60, 61, 62, 65, 66, 67, 68, 69, 70, ]}
]

inference_bias_gpt4 = [
    { "KR": [1, 2, 4, 6, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 34, 35, 37, 41, 43, 44, 47, 48, 49, 52, 69, 70, ]},
    { "CN": [1, 2, 16, 25, 29, 30, 31, 32, 34, 44, 47, 49, 50, 69, ]},
    { "JP": [1, 2, 4, 5, 6, 8, 10, 11, 12, 13, 14, 15, 16, 18, 21, 23, 24, 25, 26, 29, 30, 31, 32, 33, 34, 36, 37, 43, 44, 47, 48, 49, 50, 51, 53, 60, 62, 63, 69, 70, ]},
    { "US": [1, 2, 4, 6, 7, 12, 13, 14, 15, 16, 17, 21, 22, 23, 25, 26, 27, 29, 30, 31, 32, 35, 43, 44, 48, 49, 51, 60, 61, 62, 65, 66, 67, 68, 69, 70, ]}
]

model_inference_same_gpt4 = [
    { "KR": [16, 17, 18, 23, 29, 30, 31, 32, 33, 34, 49, 52, ]},
    { "CN": [16, 29, 30, 31, 32, 49, 50, ]},
    { "JP": [16, 18, 23, 25, 29, 30, 31, 32, 33, 34, 49, 50, ]},
    { "US": [1, 2, 4, 6, 7, 12, 13, 14, 15, 16, 17, 21, 22, 23, 25, 26, 27, 29, 30, 31, 32, 35, 43, 44, 48, 49, 51, 60, 61, 62, 65, 66, 67, 68, 69, 70, ]}
]

no_match_gpt4 = [
    { "KR": [3, 7, 9, 14, 20, 27, 28, 36, 38, 39, 40, 42, 45, 46, 50, 51, 54, 55, 56, 57, 58, 59, 60, 61, 64, 65, 66, 68, ]},
    { "CN": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 18, 19, 20, 21, 22, 24, 27, 28, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 48, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 70, ]},
    { "JP": [7, 9, 19, 20, 22, 28, 35, 38, 39, 40, 41, 42, 45, 46, 52, 54, 55, 56, 57, 58, 59, 61, 64, 65, 66, 67, 68, ]},
    { "US": [3, 5, 8, 9, 10, 11, 18, 19, 20, 24, 28, 33, 34, 36, 37, 38, 39, 40, 41, 42, 45, 46, 47, 50, 52, 53, 54, 55, 56, 57, 58, 59, 63, 64, ]}
]

print("model_bias_gpt4:", model_bias_gpt4)
print("inference_bias_gpt4:", inference_bias_gpt4)
print("both:", model_inference_same_gpt4)
print("no_match_gpt4:", no_match_gpt4)
print(len(model_bias_gpt4[0]["KR"]) + len(model_bias_gpt4[1]["CN"]) + len(model_bias_gpt4[2]["JP"]) + len(model_bias_gpt4[3]["US"]), len(inference_bias_gpt4[0]["KR"]) + len(inference_bias_gpt4[1]["CN"]) + len(inference_bias_gpt4[2]["JP"]) + len(inference_bias_gpt4[3]["US"]), len(model_inference_same_gpt4[0]["KR"]) + len(model_inference_same_gpt4[1]["CN"]) + len(model_inference_same_gpt4[2]["JP"]) + len(model_inference_same_gpt4[3]["US"]), len(no_match_gpt4[0]["KR"]) + len(no_match_gpt4[1]["CN"]) + len(no_match_gpt4[2]["JP"]) + len(no_match_gpt4[3]["US"]))
print(len(model_bias_gpt4[0]["KR"]) + len(model_bias_gpt4[1]["CN"]) + len(model_bias_gpt4[2]["JP"]) + len(model_bias_gpt4[3]["US"]) + len(inference_bias_gpt4[0]["KR"]) + len(inference_bias_gpt4[1]["CN"]) + len(inference_bias_gpt4[2]["JP"]) + len(inference_bias_gpt4[3]["US"]) - len(model_inference_same_gpt4[0]["KR"]) - len(model_inference_same_gpt4[1]["CN"]) - len(model_inference_same_gpt4[2]["JP"]) - len(model_inference_same_gpt4[3]["US"]) + len(no_match_gpt4[0]["KR"]) + len(no_match_gpt4[1]["CN"]) + len(no_match_gpt4[2]["JP"]) + len(no_match_gpt4[3]["US"]))

'''
model_bias_gpt4: [{'KR': [5, 16, 17, 18, 23, 29, 30, 31, 32, 33, 34, 49, 52, 53, 62, 63, 67]}, {'CN': [12, 16, 17, 23, 26, 29, 30, 31, 32, 33, 49, 50, 62]}, {'JP': [3, 16, 17, 18, 23, 25, 27, 29, 30, 31, 32, 33, 34, 49, 50]}, {'US': [1, 2, 4, 6, 7, 12, 13, 14, 15, 16, 17, 21, 22, 23, 25, 26, 27, 29, 30, 31, 32, 35, 43, 44, 48, 49, 51, 60, 61, 62, 65, 66, 67, 68, 69, 70]}]
inference_bias_gpt4: [{'KR': [1, 2, 4, 6, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 34, 35, 37, 41, 43, 44, 47, 48, 49, 52, 69, 70]}, {'CN': [1, 2, 16, 25, 29, 30, 31, 32, 34, 44, 47, 49, 50, 69]}, {'JP': [1, 2, 4, 5, 6, 8, 10, 11, 12, 13, 14, 15, 16, 18, 21, 23, 24, 25, 26, 29, 30, 31, 32, 33, 34, 36, 37, 43, 44, 47, 48, 49, 50, 51, 53, 60, 62, 63, 69, 70]}, {'US': [1, 2, 4, 6, 7, 12, 13, 14, 15, 16, 17, 21, 22, 23, 25, 26, 27, 29, 30, 31, 32, 35, 43, 44, 48, 49, 51, 60, 61, 62, 65, 66, 67, 68, 69, 70]}]
both: [{'KR': [16, 17, 18, 23, 29, 30, 31, 32, 33, 34, 49, 52]}, {'CN': [16, 29, 30, 31, 32, 49, 50]}, {'JP': [16, 18, 23, 25, 29, 30, 31, 32, 33, 34, 49, 50]}, {'US': [1, 2, 4, 6, 7, 12, 13, 14, 15, 16, 17, 21, 22, 23, 25, 26, 27, 29, 30, 31, 32, 35, 43, 44, 48, 49, 51, 60, 61, 62, 65, 66, 67, 68, 69, 70]}]
no_match_gpt4: [{'KR': [3, 7, 9, 14, 20, 27, 28, 36, 38, 39, 40, 42, 45, 46, 50, 51, 54, 55, 56, 57, 58, 59, 60, 61, 64, 65, 66, 68]}, {'CN': [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 18, 19, 20, 21, 22, 24, 27, 28, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 48, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 70]}, {'JP': [7, 9, 19, 20, 22, 28, 35, 38, 39, 40, 41, 42, 45, 46, 52, 54, 55, 56, 57, 58, 59, 61, 64, 65, 66, 67, 68]}, {'US': [3, 5, 8, 9, 10, 11, 18, 19, 20, 24, 28, 33, 34, 36, 37, 38, 39, 40, 41, 42, 45, 46, 47, 50, 52, 53, 54, 55, 56, 57, 58, 59, 63, 64]}]
81 127 67 139
280
'''

print("model_bias_gpt4")
print("KR:", round(len(model_bias_gpt4[0]["KR"]) / 70 * 100), "%")
print("CN:", round(len(model_bias_gpt4[1]["CN"]) / 70 * 100), "%")
print("JP:", round(len(model_bias_gpt4[2]["JP"]) / 70 * 100), "%")
print("US:", round(len(model_bias_gpt4[3]["US"]) / 70 * 100), "%")
print("-----------------------------")

print("inference_bias_gpt4")
print("KR:", round(len(inference_bias_gpt4[0]["KR"]) / 70 * 100), "%")
print("CN:", round(len(inference_bias_gpt4[1]["CN"]) / 70 * 100), "%")
print("JP:", round(len(inference_bias_gpt4[2]["JP"]) / 70 * 100), "%")
print("US:", round(len(inference_bias_gpt4[3]["US"]) / 70 * 100), "%")
print("-----------------------------")

print("model_inference_same_gpt4")
print("KR:", round(len(model_inference_same_gpt4[0]["KR"]) / 70 * 100), "%")
print("CN:", round(len(model_inference_same_gpt4[1]["CN"]) / 70 * 100), "%")
print("JP:", round(len(model_inference_same_gpt4[2]["JP"]) / 70 * 100), "%")
print("US:", round(len(model_inference_same_gpt4[3]["US"]) / 70 * 100), "%")
print("-----------------------------")

print("no_match_gpt4")
print("KR:", round(len(no_match_gpt4[0]["KR"]) / 70 * 100), "%")
print("CN:", round(len(no_match_gpt4[1]["CN"]) / 70 * 100), "%")
print("JP:", round(len(no_match_gpt4[2]["JP"]) / 70 * 100), "%")
print("US:", round(len(no_match_gpt4[3]["US"]) / 70 * 100), "%")

'''
model_bias_gpt4
KR: 24 %
CN: 19 %
JP: 21 %
US: 51 %
-----------------------------
inference_bias_gpt4
KR: 53 %
CN: 20 %
JP: 57 %
US: 51 %
-----------------------------
model_inference_same_gpt4
KR: 17 %
CN: 10 %
JP: 17 %
US: 51 %
-----------------------------
no_match_gpt4
KR: 40 %
CN: 71 %
JP: 39 %
US: 49 %
'''
