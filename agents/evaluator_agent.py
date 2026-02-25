import ollama
import re

def evaluate_answers(hr_answer, tech_answer):
    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "system",
                "content": """
You are a STRICT interview evaluator.

Rules:
- Nonsense / random text → 0–2
- Very short / weak → 3–4
- Average answer → 5–6
- Good explanation → 7–8
- Excellent structured answer → 9–10

Reply ONLY in this format:
FINAL_SCORE: <number>
FEEDBACK: <short feedback>
"""
            },
            {
                "role": "user",
                "content": f"""
HR Answer:
{hr_answer}

Tech Answer:
{tech_answer}
"""
            }
        ]
    )

    text = response["message"]["content"]

    match = re.search(r"FINAL_SCORE:\s*(\d+)", text)
    score = int(match.group(1)) if match else 2

    return score, text


 
