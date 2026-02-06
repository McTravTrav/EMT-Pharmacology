import streamlit as st
import random

# Initialize the full bank of 71 questions
def get_full_bank():
    return [
        {"q": "What are the three key responsibilities of an EMT regarding medication safety?", "choices": ["Diagnosis, prescription, and follow-up", "Cross-check, correct dose/route, and monitoring", "Billing, driving, and inventory", "Intubation, sedation, and surgery"], "a": "Cross-check, correct dose/route, and monitoring", "reason": "EMTs ensure safety through standardized double-checks and post-admin observation."},
        {"q": "Enteral medication administration refers to which route?", "choices": ["Injection", "Inhalation", "Ingestion (GI tract)", "Intravenous"], "a": "Ingestion (GI tract)", "reason": "Enteral involves the digestive system, like oral glucose."},
        {"q": "What is the standard adult dose for Aspirin?", "choices": ["81 mg", "162 mg", "324 mg", "500 mg"], "a": "324 mg", "reason": "Standard protocol is four 81mg baby aspirins."},
        {"q": "Which suffix identifies a Beta-Blocker?", "choices": ["-pril", "-sartan", "-olol", "-statin"], "a": "-olol", "reason": "Beta-blockers like Metoprolol end in -olol."},
        {"q": "What is the primary mechanism of Albuterol?", "choices": ["Alpha-1 Agonist", "Beta-2 Agonist", "Beta-1 Blocker", "Parasympathetic Antagonist"], "a": "Beta-2 Agonist", "reason": "Beta-2 targets the lungs to cause bronchodilation."},
        {"q": "What is the pediatric dose of Epinephrine via auto-injector?", "choices": ["0.3 mg", "0.5 mg", "0.15 mg", "0.1 mg"], "a": "0.15 mg", "reason": "The green Epi-Pen Jr is 0.15mg."},
        {"q": "Nitro is contraindicated if the Systolic BP is below what?", "choices": ["120 mmHg", "100 mmHg", "90 mmHg", "110 mmHg"], "a": "100 mmHg", "reason": "Standard EMS protocol requires a Systolic BP of at least 100."},
        {"q": "A medication's 'Trade Name' refers to what?", "choices": ["The chemical name", "The brand name (e.g. Tylenol)", "The government name", "The manufacturer's serial code"], "a": "The brand name (e.g. Tylenol)", "reason": "Trade names are proprietary brand names; Generic is the chemical name."},
        {"q": "What is the intended effect of Naloxone?", "choices": ["Pain relief", "Seizure control", "Restore spontaneous breathing", "Increase blood sugar"], "a": "Restore spontaneous breathing", "reason": "Narcan reverses opioid-induced respiratory depression."},
        {"q": "What does pharmacodynamics describe?", "choices": ["How the body moves a drug", "How the drug affects the body", "The cost of the drug", "The shelf life of a drug"], "a": "How the drug affects the body", "reason": "Dynamics = what the drug does to the body; Kinetics = what the body does to the drug."},
        # ... [Remaining 61 questions added here in your local file]
    ]

# --- SESSION STATE MANAGEMENT ---
if 'master_bank' not in st.session_state:
    st.session_state.master_bank = get_full_bank()
    random.shuffle(st.session_state.master_bank)

if 'current_round' not in st.session_state:
    st.session_state.current_round = st.session_state.master_bank[:20]
    st.session_state.master_bank = st.session_state.master_bank[20:]

if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'score' not in st.session_state: st.session_state.score = 0
if 'ans_submitted' not in st.session_state: st.session_state.ans_submitted = False

st.title("🚑 EMT Pharmacology: 20-Question Chunks")
st.write(f"Bank Remaining: {len(st.session_state.master_bank)} questions")

# --- QUIZ LOGIC ---
if st.session_state.q_idx < len(st.session_state.current_round):
    item = st.session_state.current_round[st.session_state.q_idx]
    
    st.subheader(f"Question {st.session_state.q_idx + 1} of 20")
    st.info(item['q'])
    
    user_choice = st.radio("Choose one:", item['choices'], key=f"choice_{st.session_state.q_idx}")

    if st.button("Submit Answer"):
        st.session_state.ans_submitted = True

    if st.session_state.ans_submitted:
        if user_choice == item['a']:
            st.success(f"Correct! {item['reason']}")
        else:
            st.error(f"Incorrect. The answer is: {item['a']}. {item['reason']}")
        
        if st.button("Next"):
            if user_choice == item['a']: st.session_state.score += 1
            st.session_state.q_idx += 1
            st.session_state.ans_submitted = False
            st.rerun()

else:
    # END OF ROUND LOGIC
    st.balloons()
    st.header("Round Complete!")
    st.write(f"You scored {st.session_state.score} / 20 this round.")
    
    if len(st.session_state.master_bank) > 0:
        if st.button("Start Next 20 Questions"):
            # Pull next 20
            next_chunk = st.session_state.master_bank[:20]
            st.session_state.master_bank = st.session_state.master_bank[20:]
            st.session_state.current_round = next_chunk
            st.session_state.q_idx = 0
            st.session_state.score = 0
            st.rerun()
    else:
        st.write("### You have completed the entire 71-question bank!")
        if st.button("Reshuffle and Restart Everything"):
            st.session_state.master_bank = get_full_bank()
            random.shuffle(st.session_state.master_bank)
            st.session_state.current_round = st.session_state.master_bank[:20]
            st.session_state.master_bank = st.session_state.master_bank[20:]
            st.session_state.q_idx = 0
            st.session_state.score = 0
            st.rerun()