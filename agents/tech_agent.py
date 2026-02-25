def ask_tech_question(skills):
    skills = [s.lower() for s in skills]

    if "python" in skills:
        return "Explain a Python project you have worked on."
    elif "sql" in skills:
        return "What is JOIN in SQL and why is it used?"
    elif "java" in skills:
        return "Explain OOP concepts in Java."
    elif "ml" in skills:
        return "What is overfitting in Machine Learning?"
    else:
        return "Explain any technical concept you are comfortable with."



