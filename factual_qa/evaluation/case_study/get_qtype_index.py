import json
from collections import defaultdict

input_path = "factual_qa/dataset/dataset.json"
output_path = "factual_qa/dataset/q_index.json"

type_to_indices = defaultdict(list)

with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

for group in data:
    for item in group:
        question_type = item["type"]
        idx = item["idx"]
        try:
            number_part = int(idx.split("_")[0])
            type_to_indices[question_type].append(number_part)
        except:
            print(f"Invalid idx format: {idx}")

for key in type_to_indices:
    type_to_indices[key] = sorted(set(type_to_indices[key]))

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(type_to_indices, f, indent=4, ensure_ascii=False)
