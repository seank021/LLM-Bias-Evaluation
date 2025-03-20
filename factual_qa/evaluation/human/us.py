# no_match_us for all languages: [9, 10, 14, 35, 38, 39, 40, 41, 48, 53, 54, 55, 56, 57, 60, 66, 67]

model_bias_us = [
    {"KR": [3, 11, 16, 22, 26, 29, 30, 37, 42, 49, 50, ]},
    {"CN": [5, 16, 18, 21, 25, 26, 27, 29, 30, 45, 50, ]},
    {"JP": [3, 16, 19, 23, 25, 26, 27, 29, 34, 37, 42, 44, 50, 59, 63, ]},
    {"US": [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 28, 29, 30, 31, 32, 33, 34, 37, 43, 44, 45, 47, 49, 50, 51, 52, 61, 62, 64, 65, 68, 69, 70, ]}
]
inference_bias_us = [
    {"KR": [1, 2, 4, 6, 12, 13, 15, 16, 17, 19, 20, 21, 24, 25, 27, 29, 30, 36, 42, 43, 44, 45, 47, 49, 50, 51, 62, 68, 69, 70, ]},
    {"CN": [1, 2, 3, 4, 6, 7, 8, 11, 12, 13, 15, 16, 17, 19, 20, 22, 24, 28, 29, 30, 31, 32, 36, 37, 46, 47, 50, 51, 52, 58, 59, 61, 63, 64, 68, 69, 70, ]},
    {"JP": [1, 2, 5, 6, 7, 8, 11, 12, 13, 16, 17, 20, 21, 22, 23, 24, 25, 28, 29, 30, 31, 32, 33, 34, 42, 43, 47, 49, 50, 68, 69, 70, ]},
    {"US": [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 28, 29, 30, 31, 32, 33, 34, 37, 43, 44, 45, 47, 49, 50, 51, 52, 61, 62, 64, 65, 68, 69, 70, ]}
]
model_inference_same_us = [
    {"KR": [16, 29, 30, 42, 49, 50, ]},
    {"CN": [16, 29, 30, 50, ]},
    {"JP": [16, 23, 25, 29, 34, 42, 50, ]},
    {"US": [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 28, 29, 30, 31, 32, 33, 34, 37, 43, 44, 45, 47, 49, 50, 51, 52, 61, 62, 64, 65, 68, 69, 70, ]}
]
no_match_us = [
    {"KR": [5, 7, 8, 9, 10, 14, 18, 23, 28, 31, 32, 33, 34, 35, 38, 39, 40, 41, 46, 48, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, ]},
    {"CN": [9, 10, 14, 23, 33, 34, 35, 38, 39, 40, 41, 42, 43, 44, 48, 49, 53, 54, 55, 56, 57, 60, 62, 65, 66, 67, ]},
    {"JP": [4, 9, 10, 14, 15, 18, 35, 36, 38, 39, 40, 41, 45, 46, 48, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 64, 65, 66, 67, ]},
    {"US": [8, 9, 10, 14, 15, 24, 25, 26, 27, 35, 36, 38, 39, 40, 41, 42, 46, 48, 53, 54, 55, 56, 57, 58, 59, 60, 63, 66, 67, ]}
]

print("model_bias_us:", model_bias_us)
print("inference_bias_us:", inference_bias_us)
print("both:", model_inference_same_us)
print("no_match_us:", no_match_us)
print(len(model_bias_us[0]["KR"]) + len(model_bias_us[1]["CN"]) + len(model_bias_us[2]["JP"]) + len(model_bias_us[3]["US"]), len(inference_bias_us[0]["KR"]) + len(inference_bias_us[1]["CN"]) + len(inference_bias_us[2]["JP"]) + len(inference_bias_us[3]["US"]), len(model_inference_same_us[0]["KR"]) + len(model_inference_same_us[1]["CN"]) + len(model_inference_same_us[2]["JP"]) + len(model_inference_same_us[3]["US"]), len(no_match_us[0]["KR"]) + len(no_match_us[1]["CN"]) + len(no_match_us[2]["JP"]) + len(no_match_us[3]["US"]))
print(len(model_bias_us[0]["KR"]) + len(model_bias_us[1]["CN"]) + len(model_bias_us[2]["JP"]) + len(model_bias_us[3]["US"]) + len(inference_bias_us[0]["KR"]) + len(inference_bias_us[1]["CN"]) + len(inference_bias_us[2]["JP"]) + len(inference_bias_us[3]["US"]) - len(model_inference_same_us[0]["KR"]) - len(model_inference_same_us[1]["CN"]) - len(model_inference_same_us[2]["JP"]) - len(model_inference_same_us[3]["US"]) + len(no_match_us[0]["KR"]) + len(no_match_us[1]["CN"]) + len(no_match_us[2]["JP"]) + len(no_match_us[3]["US"]))

'''
model_bias_us: [{'KR': [3, 11, 16, 22, 26, 29, 30, 37, 42, 49, 50]}, {'CN': [5, 16, 18, 21, 25, 26, 27, 29, 30, 45, 50]}, {'JP': [3, 16, 19, 23, 25, 26, 27, 29, 34, 37, 42, 44, 50, 59, 63]}, {'US': [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 28, 29, 30, 31, 32, 33, 34, 37, 43, 44, 45, 47, 49, 50, 51, 52, 61, 62, 64, 65, 68, 69, 70]}]
inference_bias_us: [{'KR': [1, 2, 4, 6, 12, 13, 15, 16, 17, 19, 20, 21, 24, 25, 27, 29, 30, 36, 42, 43, 44, 45, 47, 49, 50, 51, 62, 68, 69, 70]}, {'CN': [1, 2, 3, 4, 6, 7, 8, 11, 12, 13, 15, 16, 17, 19, 20, 22, 24, 28, 29, 30, 31, 32, 36, 37, 46, 47, 50, 51, 52, 58, 59, 61, 63, 64, 68, 69, 70]}, {'JP': [1, 2, 5, 6, 7, 8, 11, 12, 13, 16, 17, 20, 21, 22, 23, 24, 25, 28, 29, 30, 31, 32, 33, 34, 42, 43, 47, 49, 50, 68, 69, 70]}, {'US': [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 28, 29, 30, 31, 32, 33, 34, 37, 43, 44, 45, 47, 49, 50, 51, 52, 61, 62, 64, 65, 68, 69, 70]}]
both: [{'KR': [16, 29, 30, 42, 49, 50]}, {'CN': [16, 29, 30, 50]}, {'JP': [16, 23, 25, 29, 34, 42, 50]}, {'US': [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 28, 29, 30, 31, 32, 33, 34, 37, 43, 44, 45, 47, 49, 50, 51, 52, 61, 62, 64, 65, 68, 69, 70]}]
no_match_us: [{'KR': [5, 7, 8, 9, 10, 14, 18, 23, 28, 31, 32, 33, 34, 35, 38, 39, 40, 41, 46, 48, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67]}, {'CN': [9, 10, 14, 23, 33, 34, 35, 38, 39, 40, 41, 42, 43, 44, 48, 49, 53, 54, 55, 56, 57, 60, 62, 65, 66, 67]}, {'JP': [4, 9, 10, 14, 15, 18, 35, 36, 38, 39, 40, 41, 45, 46, 48, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 64, 65, 66, 67]}, {'US': [8, 9, 10, 14, 15, 24, 25, 26, 27, 35, 36, 38, 39, 40, 41, 42, 46, 48, 53, 54, 55, 56, 57, 58, 59, 60, 63, 66, 67]}]
78 140 58 120
280
'''

print("model_bias_us")
print("KR:", round(len(model_bias_us[0]["KR"]) / 70 * 100), "%")
print("CN:", round(len(model_bias_us[1]["CN"]) / 70 * 100), "%")
print("JP:", round(len(model_bias_us[2]["JP"]) / 70 * 100), "%")
print("US:", round(len(model_bias_us[3]["US"]) / 70 * 100), "%")
print("-----------------------------")

print("inference_bias_us")
print("KR:", round(len(inference_bias_us[0]["KR"]) / 70 * 100), "%")
print("CN:", round(len(inference_bias_us[1]["CN"]) / 70 * 100), "%")
print("JP:", round(len(inference_bias_us[2]["JP"]) / 70 * 100), "%")
print("US:", round(len(inference_bias_us[3]["US"]) / 70 * 100), "%")
print("-----------------------------")

print("model_inference_same_us")
print("KR:", round(len(model_inference_same_us[0]["KR"]) / 70 * 100), "%")
print("CN:", round(len(model_inference_same_us[1]["CN"]) / 70 * 100), "%")
print("JP:", round(len(model_inference_same_us[2]["JP"]) / 70 * 100), "%")
print("US:", round(len(model_inference_same_us[3]["US"]) / 70 * 100), "%")
print("-----------------------------")

print("no_match_us")
print("KR:", round(len(no_match_us[0]["KR"]) / 70 * 100), "%")
print("CN:", round(len(no_match_us[1]["CN"]) / 70 * 100), "%")
print("JP:", round(len(no_match_us[2]["JP"]) / 70 * 100), "%")
print("US:", round(len(no_match_us[3]["US"]) / 70 * 100), "%")

'''
model_bias_us
KR: 16 %
CN: 16 %
JP: 21 %
US: 59 %
-----------------------------
inference_bias_us
KR: 43 %
CN: 53 %
JP: 46 %
US: 59 %
-----------------------------
model_inference_same_us
KR: 9 %
CN: 6 %
JP: 10 %
US: 59 %
-----------------------------
no_match_us
KR: 50 %
CN: 37 %
JP: 43 %
US: 41 %
'''