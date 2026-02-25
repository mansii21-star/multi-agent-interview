from agents.hr_agent import ask_hr_question
from agents.tech_agent import ask_tech_question
from agents.evaluator_agent import evaluate_answers

print("---- HR INTERVIEW ----")
print(ask_hr_question())
hr_answer = input("Your answer: ")

print("\n---- TECH INTERVIEW ----")
print(ask_tech_question())
tech_answer = input("Your answer: ")

print("\n---- EVALUATION ----")
score, feedback = evaluate_answers(hr_answer, tech_answer)
print("Score:", score, "/10")
print("Feedback:", feedback)



