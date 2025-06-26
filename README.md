# A Dual-Layered Evaluation of Geopolitical and Cultural Bias in LLMs

This repository contains the dataset, evaluation scripts, and results for analyzing geopolitical and cultural biases in large language models (LLMs). The study is structured into two evaluation phases: factual QA (objective knowledge) and disputable QA (politically sensitive disputes). We explore how LLMs exhibit model bias (training-induced) and inference bias (query language-induced) when answering questions in different languages.

## 1. Overview of the Study
This study investigates biases in LLMs through two phases:
1. **Factual QA Evaluation**: Measures how models handle objective knowledge in different languages.
2. **Disputable QA Evaluation**: Analyzes how models respond to geopolitical and historical disputes.

We define two bias types:
- **Model Bias**: The tendency to generate answers aligned with the model's primary training language.
- **Inference Bias**: The tendency to generate answers aligned with the language of the query.

## 2. Dataset Construction
The dataset includes:
- **Factual QA (Objective Knowledge)**: 70 factual questions covering country names, government structure, and official policies.
- **Disputable QA (Geopolitical Conflicts)**: 4 major disputes analyzed using open-ended, persona-based, true/false, and multiple-choice questions.

Translations were generated using GPT-4o and manually verified.

## 3. Evaluation Approach
We evaluate responses using:
1. **Model-based Evaluation (GPT-4o)**: Determines if responses match expected answers.
2. **Human Evaluation**: Classifies responses based on national perspective, neutrality, or refusal to answer.
*Only human evaluation was done for phase 2, preventing additional model-bias for sensitive topics*

**Evaluation Metrics**:
- **Model Bias Rate** = (# of model-language-aligned responses) / (Total questions)
- **Inference Bias Rate** = (# of input-language-aligned responses) / (Total questions)
- Neutral Response Rate = (# of responses that do not match any national stance) / (Total questions)

## 4. Key Findings
- Inference bias dominates factual QA: Responses tend to align with the query language rather than training data.
- Model bias is stronger in political disputes: LLMs tend to align with national perspectives in subjective topics.
- gpt4 & US models attempt neutrality but exhibit topic-dependent biases.
- Question structure influences responses: Open-ended questions lead to avoidance, while multiple-choice enforces clear biases.

## 5. How to Run This Code
### Generating Responses
For example, to generate responses from gpt4 for phase 2:
```
cd disputable_qa/model_response
python get_response.py
```

### Running Evaluations
For example, to run evaluations for phase 2:
```
cd disputable_qa/evaluation
python eval.py
```

For example, for factual QA (phase 1) model_based evaluations:
```
cd factual_qa/evaluation/model_based
python gpt4.py  # (or cn.py, jp.py, kr.py, us.py)
```
