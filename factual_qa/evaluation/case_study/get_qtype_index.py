import json
from collections import defaultdict

# 입력 파일 경로
input_path = "factual_qa/dataset/dataset.json"
# 출력 파일 경로
output_path = "factual_qa/dataset/q_index.json"

# 타입별 인덱스를 저장할 딕셔너리
type_to_indices = defaultdict(list)

# JSON 파일 읽기
with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 데이터 순회하며 type별 인덱스 수집
for group in data:
    for item in group:
        question_type = item["type"]
        idx = item["idx"]
        try:
            number_part = int(idx.split("_")[0])
            type_to_indices[question_type].append(number_part)
        except:
            print(f"Invalid idx format: {idx}")

# 중복 제거 및 정렬
for key in type_to_indices:
    type_to_indices[key] = sorted(set(type_to_indices[key]))

# 결과 저장
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(type_to_indices, f, indent=4, ensure_ascii=False)
