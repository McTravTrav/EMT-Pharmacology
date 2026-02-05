import streamlit as st
import random

# The 71 Question Bank from your Pharmacology Review
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = [
        # Principles
        {"q": "What are three key responsibilities of an EMT regarding medication safety?", "a": "Medication cross-check, correct dose/route, and monitoring after administration."},
        {"q": "What is the difference between enteral and parenteral?", "a": "Enteral = ingested (GI tract); Parenteral = injected/inhaled (bypasses GI)."},
        {"q": "Give one example of an enteral medication.", "a": "Oral glucose."},
        {"q": "Give one example of a parenteral medication.", "a": "Epinephrine (IM) or Oxygen."},
        {"q": "Name the three main routes of injection used in EMS.", "a": "Subcutaneous (SC), intramuscular (IM), and intravenous (IV)."},
        {"q": "List the 'Six Rights' of medication administration.", "a": "Right Patient, Right Medication, Right Dose, Right Route, Right Time, Right Documentation."},
        
        # Aspirin
        {"q": "What is the indication for Aspirin (ASA)?", "a": "Chest pain suggestive of AMI (Heart Attack)."},
        {"q": "What is the mechanism of action for Aspirin?", "a": "Anti-platelet aggregate (prevents clots from getting bigger)."},
        {"q": "What is the adult dose for Aspirin?", "a": "324mg (Four 81mg chewable baby aspirins)."},
        
        # Glucose & Epi
        {"q": "What is the route for Oral Glucose?", "a": "Buccal (between cheek and gum)."},
        {"q": "What is the adult dose for Epinephrine?", "a": "0.3 mg."},
        {"q": "What is the pediatric dose for Epinephrine?", "a": "0.15 mg."},
        {"q": "How long should you hold the Epi-Pen against the thigh?", "a": "10 seconds."},
        
        # Nitro
        {"q": "What are the 3 BP/Med requirements to give Nitro?", "a": "Prescribed to patient, Systolic BP > 100, and no ED meds in 24-48 hours."},
        {"q": "What is the dose and max doses for Nitroglycerin?", "a": "0.4 mg per dose; max of 3 doses (including what they took before EMS)."},
        
        # Chronic Suffixes (The heavy hitters for the exam)
        {"q": "What do Beta Blockers do and what is their suffix?", "a": "Lower HR/BP; suffix -olol (e.g., metoprolol)."},
        {"q": "What do ACE Inhibitors do and what is their suffix?", "a": "Lower BP; suffix -pril (e.g., lisinopril)."},
        {"q": "What do ARBs do and what is their suffix?", "a": "Lower BP; suffix -sartan (e.g., losartan)."},
        {"q": "What is the suffix for Benzodiazepines?", "a": "-zepam or -zolam (e.g., diazepam, alprazolam)."},
        {"q": "What suffix identifies Proton Pump Inhibitors (PPIs)?", "a": "-prazole (e.g., omeprazole)."},
        {"q": "What suffix is common for Beta-2 Agonist bronchodilators?", "a": "-terol (e.g., albuterol)."},
        {"q": "Why are PDE5 inhibitors (Viagra) contraindicated with Nitro?", "a": "Severe, life-threatening hypotension."}
        # ... (Note: Include all 71 questions here using the format above)
    ]
    random.shuffle(st.session_state.quiz_data)

# App State Setup
if 'count' not in st.session_state:
    st.session_state.count = 0
if 'score' not in st.session_state:
    st.session_state.score = 0

st.title("💊 EMT Pharmacology Module Review")
st.subheader("Fall 2025 Study Guide - 71 Questions")

# Progress Bar
progress = st.session_state.count / len(st.session_state.quiz_data)
st.progress(progress)

# Display Question
current_q = st.session_state.quiz_data[st.session_state.count]
st.write(f"### Question {st.session_state.count + 1}:")
st.info(current_q['q'])

# Answer Logic
if st.button("Show Answer"):
    st.success(f"CORRECT ANSWER: {current_q['a']}")

# Scoring
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ I Got It Right"):
        st.session_state.score += 1
        st.session_state.count += 1
        st.rerun()
with col2:
    if st.button("❌ I Missed It"):
        st.session_state.count += 1
        st.rerun()

st.write(f"Current Score: {st.session_state.score} / {st.session_state.count}")

# Reset logic
if st.session_state.count >= len(st.session_state.quiz_data):
    st.write("## Quiz Complete!")
    if st.button("Restart Quiz"):
        st.session_state.count = 0
        st.session_state.score = 0
        random.shuffle(st.session_state.quiz_data)
        st.rerun()