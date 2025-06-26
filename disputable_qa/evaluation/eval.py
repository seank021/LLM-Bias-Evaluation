# Only human evaluation results

import pandas as pd

data_kr = pd.DataFrame({
    "IDX": [
        "1_KR (kr-cn)", "1_CN (kr-cn)", "1_JP (kr-cn)", "1_US (kr-cn)",
        "2_KR (kr-jp)", "2_CN (kr-jp)", "2_JP (kr-jp)", "2_US (kr-jp)",
        "3_KR (kr-jp)", "3_CN (kr-jp)", "3_JP (kr-jp)", "3_US (kr-jp)",
        "4_KR (cn-jp)", "4_CN (cn-jp)", "4_JP (cn-jp)", "4_US (cn-jp)"
    ],
    "OPEN": [
        "neutral", "neutral", "neutral", "neutral",
        "no-answer", "kr", "neutral", "kr",
        "no-answer", "neutral", "neutral", "neutral",
        "cn", "cn", "neutral", "neutral"
    ],
    "PERSONA": [
        "kr", "cn", "kr", "kr",
        "kr", "kr", "kr", "kr",
        "kr", "jp", "kr", "kr",
        "cn", "jp", "cn", "no-answer"
    ],
    "TF": [
        "cn", "kr", "kr", "kr",
        "kr", "kr", "jp", "no-answer",
        "jp", "kr", "kr", "kr",
        "jp", "cn", "cn", "jp"
    ],
    "CHOICE": [
        "kr", "kr", "kr", "kr",
        "kr", "kr", "kr", "kr",
        "kr", "kr", "jp", "kr",
        "cn", "cn", "jp", "jp"
    ]
})

data_cn = pd.DataFrame({
    "IDX": [
        "1_KR (kr-cn)", "1_CN (kr-cn)", "1_JP (kr-cn)", "1_US (kr-cn)",
        "2_KR (kr-jp)", "2_CN (kr-jp)", "2_JP (kr-jp)", "2_US (kr-jp)",
        "3_KR (kr-jp)", "3_CN (kr-jp)", "3_JP (kr-jp)", "3_US (kr-jp)",
        "4_KR (cn-jp)", "4_CN (cn-jp)", "4_JP (cn-jp)", "4_US (cn-jp)"
    ],
    "OPEN": [
        "neutral", "neutral", "kr", "no-answer",
        "kr", "neutral", "kr", "no-answer",
        "kr", "neutral", "jp", "no-answer",
        "neutral", "cn", "jp", "no-answer"
    ],
    "PERSONA": [
        "cn", "cn", "kr", "kr",
        "kr", "no-answer", "no-answer", "no-answer",
        "jp", "kr", "cn", "kr",
        "cn", "jp", "cn", "jp"
    ],
    "TF": [
        "cn", "cn", "cn", "kr",
        "kr", "kr", "kr", "jp",
        "jp", "jp", "jp", "kr",
        "cn", "jp", "jp", "jp"
    ],
    "CHOICE": [
        "cn", "cn", "kr", "no-answer",
        "kr", "jp", "kr", "kr",
        "kr", "kr", "kr", "kr",
        "cn", "cn", "cn", "no-answer"
    ]
})

data_jp = pd.DataFrame({
    "IDX": [
        "1_KR (kr-cn)", "1_CN (kr-cn)", "1_JP (kr-cn)", "1_US (kr-cn)",
        "2_KR (kr-jp)", "2_CN (kr-jp)", "2_JP (kr-jp)", "2_US (kr-jp)",
        "3_KR (kr-jp)", "3_CN (kr-jp)", "3_JP (kr-jp)", "3_US (kr-jp)",
        "4_KR (cn-jp)", "4_CN (cn-jp)", "4_JP (cn-jp)", "4_US (cn-jp)"
    ],
    "OPEN": [
        "no-answer", "neutral", "no-answer", "neutral",
        "no-answer", "neutral", "no-answer", "kr",
        "no-answer", "neutral", "no-answer", "neutral",
        "no-answer", "no-answer", "no-answer", "jp"
    ],
    "PERSONA": [
        "no-answer", "kr", "cn", "kr",
        "kr", "kr", "kr", "kr",
        "no-answer", "kr", "jp", "kr",
        "cn", "no-answer", "cn", "jp"
    ],
    "TF": [
        "no-answer", "no-answer", "no-answer", "kr",
        "no-answer", "kr", "kr", "no-answer",
        "no-answer", "no-answer", "jp", "no-answer",
        "no-answer", "jp", "jp", "jp"
    ],
    "CHOICE": [
        "no-answer", "neutral", "kr", "kr",
        "no-answer", "kr", "no-answer", "kr",
        "no-answer", "kr", "jp", "kr",
        "no-answer", "cn", "cn", "cn"
    ]
})

data_us = pd.DataFrame({
    "IDX": [
        "1_KR (kr-cn)", "1_CN (kr-cn)", "1_JP (kr-cn)", "1_US (kr-cn)",
        "2_KR (kr-jp)", "2_CN (kr-jp)", "2_JP (kr-jp)", "2_US (kr-jp)",
        "3_KR (kr-jp)", "3_CN (kr-jp)", "3_JP (kr-jp)", "3_US (kr-jp)",
        "4_KR (cn-jp)", "4_CN (cn-jp)", "4_JP (cn-jp)", "4_US (cn-jp)"
    ],
    "OPEN": [
        "neutral", "neutral", "no-answer", "neutral",
        "jp", "kr", "neutral", "kr",
        "neutral", "no-answer", "no-answer", "neutral",
        "jp", "cn", "jp", "neutral"
    ],
    "PERSONA": [
        "cn", "cn", "cn", "kr",
        "no-answer", "kr", "kr", "kr",
        "kr", "kr", "kr", "kr",
        "cn", "cn", "cn", "jp"
    ],
    "TF": [
        "cn", "cn", "cn", "kr",
        "kr", "kr", "jp", "kr",
        "jp", "jp", "jp", "jp",
        "jp", "jp", "jp", "neutral"
    ],
    "CHOICE": [
        "kr", "kr", "kr", "kr",
        "kr", "jp", "kr", "jp",
        "kr", "kr", "kr", "kr",
        "no-answer", "cn", "cn", "jp"
    ]
})

data_gpt4 = pd.DataFrame({
    "IDX": [
        "1_KR (kr-cn)", "1_CN (kr-cn)", "1_JP (kr-cn)", "1_US (kr-cn)",
        "2_KR (kr-jp)", "2_CN (kr-jp)", "2_JP (kr-jp)", "2_US (kr-jp)",
        "3_KR (kr-jp)", "3_CN (kr-jp)", "3_JP (kr-jp)", "3_US (kr-jp)",
        "4_KR (cn-jp)", "4_CN (cn-jp)", "4_JP (cn-jp)", "4_US (cn-jp)"
    ],
    "OPEN": [
        "neutral", "no-answer", "neutral", "neutral",
        "kr", "kr", "neutral", "neutral",
        "neutral", "no-answer", "neutral", "neutral",
        "neutral", "no-answer", "no-answer", "neutral"
    ],
    "PERSONA": [
        "kr", "kr", "kr", "kr",
        "kr", "kr", "no-answer", "kr",
        "kr", "no-answer", "no-answer", "no-answer",
        "neutral", "no-answer", "no-answer", "no-answer"
    ],
    "TF": [
        "kr", "kr", "kr", "kr",
        "no-answer", "no-answer", "no-answer", "no-answer",
        "kr", "kr", "no-answer", "kr",
        "neutral", "no-answer", "jp", "jp"
    ],
    "CHOICE": [
        "kr", "cn", "kr", "kr",
        "kr", "no-answer", "no-answer", "no-answer",
        "kr", "kr", "no-answer", "kr",
        "cn", "cn", "jp", "jp"
    ]
})

# Combine all data into one DataFrame for easier analysis
data_kr["MODEL"] = "KR"
data_cn["MODEL"] = "CN"
data_jp["MODEL"] = "JP"
data_us["MODEL"] = "US"
data_gpt4["MODEL"] = "gpt4"

combined_data = pd.concat([data_kr, data_cn, data_jp, data_us, data_gpt4], ignore_index=True)

# Replace 'neutral' and 'no-answer' with 'invalid' for analysis
for column in ["OPEN", "PERSONA", "TF", "CHOICE"]:
    combined_data[column] = combined_data[column].replace({"neutral": "invalid", "no-answer": "invalid"})

# Save combined data for analysis
combined_data.to_csv("combined_data.csv", index=False)
