import streamlit as st
from PyPDF2 import PdfReader

from agents.hr_agent import ask_hr_question
from agents.tech_agent import ask_tech_question
from agents.evaluator_agent import evaluate_answers

st.title("🤖 Multi-Agent AI Interview Panel")

# ---------------- SESSION STATE ----------------
if "resume_uploaded" not in st.session_state:
    st.session_state.resume_uploaded = False
if "hr_done" not in st.session_state:
    st.session_state.hr_done = False

# ---------------- RESUME UPLOAD ----------------
st.subheader("📄 Upload Your Resume (PDF)")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

resume_text = ""

if uploaded_file:
    reader = PdfReader(uploaded_file)
    for page in reader.pages:
        resume_text += page.extract_text()

    st.session_state.resume_uploaded = True
    st.success("Resume uploaded successfully")

# ---------------- SKILL EXTRACTION ----------------
def extract_skills(text):
    text = text.lower()
    skills = []

    if "python" in text:
        skills.append("python")
    if "sql" in text:
        skills.append("sql")
    if "java" in text:
        skills.append("java")
    if "machine learning" in text or "ml" in text:
        skills.append("ml")

    return skills

skills = extract_skills(resume_text)

if st.session_state.resume_uploaded:
    st.info(f"Detected skills: {', '.join(skills) if skills else 'No skills detected'}")

# ---------------- HR INTERVIEW ----------------
if st.session_state.resume_uploaded and not st.session_state.hr_done:
    st.subheader("👤 HR Interview")

    hr_question = ask_hr_question()
    st.write(hr_question)

    hr_answer = st.text_area("Your HR Answer")

    if st.button("Submit HR Answer"):
        if hr_answer.strip() == "":
            st.error("Please answer the HR question")
        else:
            st.session_state.hr_answer = hr_answer
            st.session_state.hr_done = True
            st.success("HR round completed")

# ---------------- TECH INTERVIEW ----------------
if st.session_state.hr_done:
    st.subheader("💻 Tech Interview")

    tech_question = ask_tech_question(skills)
    st.write(tech_question)

    tech_answer = st.text_area("Your Tech Answer")

    if st.button("Evaluate Interview"):
        if tech_answer.strip() == "":
            st.error("Please answer the tech question")
        else:
            score, feedback = evaluate_answers(
                st.session_state.hr_answer,
                tech_answer
            )

            st.subheader("📊 Evaluation Result")
            st.write(f"**Score:** {score}/10")
            st.success(feedback)





