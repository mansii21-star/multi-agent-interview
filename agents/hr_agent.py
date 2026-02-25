import ollama

def ask_hr_question():
    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an HR interviewer. "
                    "Ask ONLY one behavioral or situational HR interview question. "
                    "Do NOT ask math, aptitude, puzzles, or technical questions."
                )
            },
            {
                "role": "user",
                "content": "Ask a suitable HR interview question for a fresher."
            }
        ]
    )
    return response["message"]["content"]








