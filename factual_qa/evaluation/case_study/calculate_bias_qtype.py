from collections import defaultdict

# ========== Index grouped by bias types per each national model ==========
# KR - Responses of KR model
model_bias_kr = [ # questions that showed model-bias, with each query language as key
    { "KR": [1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70]},
    { "CN": [11, 16, 23, 25, 29, 30, 31, 32, 33, 34, 36, 43, 48, 49, 55, 66, ]},
    { "JP": [7, 16, 17, 23, 24, 26, 27, 29, 30, 31, 32, 33, 34, 36, 38, 39, 40, 42, 44, 45, 46, 47, 48, 49, 51, 52, 54, 56, 57, 58, 62, 64, 65, 69, ]},
    { "US": [16, 23, 25, 29, 30, 32, 33, 36, 48, 49, ]}
]
inference_bias_kr = [ # questions that showed inference-bias, with each query language as key
    { "KR": [1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 57, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69, 70]},
    { "CN": [1, 3, 6, 7, 11, 12, 13, 15, 16, 17, 18, 19, 20, 22, 24, 25, 27, 28, 29, 30, 31, 32, 36, 37, 38, 47, 49, 51, 52, 58, 59, 62, 64, 68, 69, 70]},
    { "JP": [1, 3, 6, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22, 23, 25, 28, 29, 30, 31, 32, 33, 34, 36, 37, 43, 49, 50, 51, 53, 68, 70]},
    { "US": [1, 2, 3, 6, 12, 15, 16, 17, 18, 21, 22, 23, 26, 27, 28, 29, 30, 32, 33, 37, 38, 39, 40, 45, 49, 51, 54, 57, 61, 62, 63, 66, 70]}
]
no_match_kr = [ # questions that showed no-match-bias, with each query language as key
    { "KR": [5, 9, 19, 35, 38, 50, 53, 58, 63, ]},
    { "CN": [2, 4, 5, 8, 9, 10, 14, 21, 26, 35, 39, 40, 41, 42, 44, 45, 46, 50, 53, 54, 56, 57, 60, 61, 63, 65, 67, ]},
    { "JP": [2, 4, 5, 8, 9, 19, 21, 35, 41, 55, 59, 60, 61, 63, 66, 67, ]},
    { "US": [4, 5, 7, 8, 9, 10, 11, 13, 14, 19, 20, 24, 31, 34, 35, 41, 42, 43, 44, 46, 47, 50, 52, 53, 55, 56, 58, 59, 60, 64, 65, 67, 68, 69, ]}
]

# CN
model_bias_cn = [
    { "KR": [16, 17, 25, 29, 30, 31, 32, 49, 53, ]},
    { "CN": [1, 4, 8, 9, 12, 15, 16, 20, 22, 24, 26, 28, 29, 30, 31, 32, 35, 38, 41, 43, 49, 50, 51, 52, 58, 59, 61, 63, 69, ]},
    { "JP": [28, 29, 30, 31, 32, 49, 52, 69, ]},
    { "US": [16, 29, 30, 31, 32, 36, ]}
]
inference_bias_cn = [
    { "KR": [2, 4, 5, 6, 11, 12, 15, 16, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 34, 43, 44, 48, 49, 52, 66, 68, 69, ]},
    { "CN": [1, 4, 8, 9, 12, 15, 16, 20, 22, 24, 26, 28, 29, 30, 31, 32, 35, 38, 41, 43, 49, 50, 51, 52, 58, 59, 61, 63, 69, ]},
    { "JP": [1, 3, 4, 5, 6, 8, 12, 13, 17, 20, 22, 23, 24, 25, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 43, 46, 47, 48, 49, 51, 59, 64, ]},
    { "US": [1, 2, 3, 5, 6, 11, 16, 17, 18, 20, 21, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 37, 38, 39, 43, 44, 48, 51, 52, 53, 55, 57, 59, 62, 63, 66, 68, 70, ]}
]
no_match_cn = [
    { "KR": [1, 3, 7, 8, 9, 10, 13, 14, 18, 19, 20, 21, 27, 28, 35, 36, 37, 38, 39, 40, 41, 42, 45, 46, 47, 50, 51, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 70, ]},
    { "CN": [2, 3, 5, 6, 7, 10, 11, 13, 14, 17, 18, 19, 21, 23, 25, 27, 33, 34, 36, 37, 39, 40, 42, 44, 45, 46, 47, 48, 53, 54, 55, 56, 57, 60, 62, 64, 65, 66, 67, 68, 70, ]},
    { "JP": [2, 7, 9, 10, 11, 14, 15, 16, 18, 19, 21, 26, 39, 40, 41, 42, 44, 45, 50, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63, 65, 66, 67, 68, 70, ]},
    { "US": [4, 7, 8, 9, 10, 12, 13, 14, 15, 19, 22, 28, 35, 40, 41, 42, 45, 46, 47, 49, 50, 54, 56, 58, 60, 61, 64, 65, 67, 69, ]}
]

# JP
model_bias_jp = [
    { "KR": [16, 23, 29, 30, 31, 33, 34, 49, ]},
    { "CN": [16, 21, 23, 24, 29, 30, 31, 34, 46, 49, ]},
    { "JP": [1, 2, 3, 4, 6, 8, 13, 16, 17, 20, 21, 22, 23, 24, 26, 29, 30, 31, 32, 33, 34, 36, 37, 43, 44, 45, 47, 48, 49, 53, 59, ]},
    { "US": [8, 13, 16, 17, 23, 29, 30, 31, 32, 33, 34, 49, 50, ]}
]
inference_bias_jp = [
    { "KR": [1, 2, 4, 6, 8, 12, 13, 16, 17, 19, 23, 24, 25, 29, 30, 31, 33, 34, 43, 45, 46, 49, 50, ]},
    { "CN": [1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 16, 17, 20, 22, 25, 26, 28, 29, 30, 31, 33, 36, 37, 43, 44, 47, 48, 49, 50, 51, 53, 66, 67, ]},
    { "JP": [1, 2, 3, 4, 6, 8, 13, 16, 17, 20, 21, 22, 23, 24, 26, 29, 30, 31, 32, 33, 34, 36, 37, 43, 44, 45, 47, 48, 49, 53, 59, ]},
    { "US": [1, 2, 3, 4, 5, 6, 7, 11, 16, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 43, 45, 46, 48, 49, 51, 53, 59, 63, 64, 65, 66, 67, 69, 70, ]}
]
no_match_jp = [
    { "KR": [3, 5, 7, 9, 10, 11, 14, 15, 18, 20, 21, 22, 26, 27, 28, 32, 35, 36, 37, 38, 39, 40, 41, 42, 44, 47, 48, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, ]},
    { "CN": [6, 9, 14, 15, 18, 19, 27, 32, 35, 38, 39, 40, 41, 42, 45, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 68, 69, 70, ]},
    { "JP": [5, 7, 9, 10, 11, 12, 14, 15, 18, 19, 25, 27, 28, 35, 38, 39, 40, 41, 42, 46, 50, 51, 52, 54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, ]},
    { "US": [9, 10, 12, 14, 15, 18, 27, 41, 42, 44, 47, 52, 54, 55, 56, 57, 58, 60, 61, 62, 68, ]}
]

# US
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
no_match_us = [
    {"KR": [5, 7, 8, 9, 10, 14, 18, 23, 28, 31, 32, 33, 34, 35, 38, 39, 40, 41, 46, 48, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, ]},
    {"CN": [9, 10, 14, 23, 33, 34, 35, 38, 39, 40, 41, 42, 43, 44, 48, 49, 53, 54, 55, 56, 57, 60, 62, 65, 66, 67, ]},
    {"JP": [4, 9, 10, 14, 15, 18, 35, 36, 38, 39, 40, 41, 45, 46, 48, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 64, 65, 66, 67, ]},
    {"US": [8, 9, 10, 14, 15, 24, 25, 26, 27, 35, 36, 38, 39, 40, 41, 42, 46, 48, 53, 54, 55, 56, 57, 58, 59, 60, 63, 66, 67, ]}
]

# GPT-4
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
no_match_gpt4 = [
    { "KR": [3, 7, 9, 14, 20, 27, 28, 36, 38, 39, 40, 42, 45, 46, 50, 51, 54, 55, 56, 57, 58, 59, 60, 61, 64, 65, 66, 68, ]},
    { "CN": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 18, 19, 20, 21, 22, 24, 27, 28, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 48, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 70, ]},
    { "JP": [7, 9, 19, 20, 22, 28, 35, 38, 39, 40, 41, 42, 45, 46, 52, 54, 55, 56, 57, 58, 59, 61, 64, 65, 66, 67, 68, ]},
    { "US": [3, 5, 8, 9, 10, 11, 18, 19, 20, 24, 28, 33, 34, 36, 37, 38, 39, 40, 41, 42, 45, 46, 47, 50, 52, 53, 54, 55, 56, 57, 58, 59, 63, 64, ]}
]

# ========== Structured bias data ==========
bias_data = {
    "kr": {
        "model": model_bias_kr,
        "inference": inference_bias_kr,
        "no_match": no_match_kr
    },
    "cn": {
        "model": model_bias_cn,
        "inference": inference_bias_cn,
        "no_match": no_match_cn
    },
    "jp": {
        "model": model_bias_jp,
        "inference": inference_bias_jp,
        "no_match": no_match_jp
    },
    "us": {
        "model": model_bias_us,
        "inference": inference_bias_us,
        "no_match": no_match_us
    },
    "gpt4": {
        "model": model_bias_gpt4,
        "inference": inference_bias_gpt4,
        "no_match": no_match_gpt4
    }
}

# ========== Question type for each index ==========
qtypes_index = [
    { "Overview": [1, 2, 3, 4, 5, 6, 7, 8, 9 ] },
    { "Geograpy": [10, 11, 12, 13, 14, 15, 16] },
    { "Politics": [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34] },
    { "Military": [ 35, 36] },
    { "Economics": [ 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50] },
    { "Society": [ 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67] },
    { "Etc": [ 68, 69, 70] },
]

# ========== Rate of each question type ==========
qtype_counts = defaultdict(int)
for group in qtypes_index:
    for qtype, qids in group.items():
        qtype_counts[qtype] += len(qids)
total_count = sum(qtype_counts.values())

for qtype, count in qtype_counts.items():
    qtype_counts[qtype] = round(count / total_count * 100, 1)

print("=== Question Type Percentages ===")
for qtype, percentage in qtype_counts.items():
    print(f"{qtype}: {percentage}%")

# ========== Calculate bias percentages for each national model for each query language ==========
# qid to type mapping
qid_to_type = {}
for group in qtypes_index:
    for qtype, qids in group.items():
        for qid in qids:
            qid_to_type[qid] = qtype
all_qids = set(qid_to_type.keys())

# extract the indices from the bias list based on the query language
def extract_indices(bias_list, query_lang):
    for entry in bias_list:
        if query_lang in entry:
            return set(entry[query_lang])
    return set()

# calculate the bias percentages for each question type
def calc_bias_percentages(model_name, query_lang, bias_data):
    result = defaultdict(lambda: {"model_bias": 0, "inference_bias": 0, "no_response": 0})
    
    model_set = extract_indices(bias_data[model_name]["model"], query_lang)
    inference_set = extract_indices(bias_data[model_name]["inference"], query_lang)
    no_match_set = extract_indices(bias_data[model_name]["no_match"], query_lang)

    qtype_counts = defaultdict(list)
    for qid in all_qids:
        qtype = qid_to_type[qid]
        qtype_counts[qtype].append(qid)

    for qtype, qids in qtype_counts.items():
        total = len(qids)
        model_count = len(set(qids) & model_set)
        inference_count = len(set(qids) & inference_set)
        no_match_count = len(set(qids) & no_match_set)

        result[qtype]["model_bias"] = round(model_count / total * 100, 1)
        result[qtype]["inference_bias"] = round(inference_count / total * 100, 1)
        result[qtype]["no_response"] = round(no_match_count / total * 100, 1)

    return result

# print all bias percentages for each model
def print_all_bias_percentages(bias_data):
    for model_name in ["kr", "cn", "jp", "us", "gpt4"]:
        print(f"\n=== {model_name.upper()} model bias by question type ===")
        for query_lang in ["KR", "CN", "JP", "US"]:
            print(f"-- Query Language: {query_lang} --")
            stats = calc_bias_percentages(model_name, query_lang, bias_data)
            for qtype in stats.keys():
                s = stats[qtype]
                print(f"{qtype}: model-bias {s['model_bias']}%, inference-bias {s['inference_bias']}%, no-response {s['no_response']}%")
            print()

print_all_bias_percentages(bias_data)
