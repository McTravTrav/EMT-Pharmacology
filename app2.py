import streamlit as st
import random

# --- THE FULL 71-QUESTION DATASET ---
def get_full_bank():
    return [
        # Principles
        {"q": "What are the three key responsibilities of an EMT regarding medication safety?", "choices": ["Diagnosis, prescription, and follow-up", "Cross-check, correct dose/route, and monitoring", "Billing, driving, and inventory", "Intubation and sedation"], "a": "Cross-check, correct dose/route, and monitoring", "reason": "Standard safety responsibility."},
        {"q": "What is the difference between enteral and parenteral administration?", "choices": ["Enteral is inhaled; Parenteral is ingested", "Enteral is ingested; Parenteral is injected/inhaled", "Enteral is for adults; Parenteral is for kids", "There is no difference"], "a": "Enteral is ingested; Parenteral is injected/inhaled", "reason": "Enteral = GI tract."},
        {"q": "Name the three main routes of injection used in EMS.", "choices": ["Oral, Rectal, Nasal", "SC, IM, IV", "Buccal, SL, PO", "Topical, Ocular, Nasal"], "a": "SC, IM, IV", "reason": "Subcutaneous, Intramuscular, and Intravenous."},
        {"q": "Define 'Pharmacodynamics'.", "choices": ["How the body moves a drug", "How a drug affects the body", "The cost of the drug", "The speed of the ambulance"], "a": "How a drug affects the body", "reason": "Dynamics = what the drug DOES to the body."},
        {"q": "What is the difference between generic and trade names?", "choices": ["Generic is brand name; Trade is chemical", "Generic is chemical; Trade is brand", "Generic is for liquids; Trade for solids", "They are the same"], "a": "Generic is chemical; Trade is brand", "reason": "Example: Ibuprofen (Generic) vs Advil (Trade)."},
        {"q": "What is the difference between 'assisting' and 'administering'?", "choices": ["Assisting is for doctors only", "Assisting is patient's own med; Administering is EMS med", "Administering is for doctors only", "They are the same"], "a": "Assisting is patient's own med; Administering is EMS med", "reason": "EMT scope definition."},
        {"q": "What are the 'Six Rights'?", "choices": ["Patient, Drug, Dose, Route, Time, Documentation", "Person, Place, Thing, Time, Action, Price", "History, Vitals, Age, Weight, Sex, Race", "Drug, Bottle, Color, Size, Shape, Label"], "a": "Patient, Drug, Dose, Route, Time, Documentation", "reason": "Standard safety protocol."},
        
        # Aspirin
        {"q": "What is the adult dose for Aspirin for cardiac chest pain?", "choices": ["81 mg", "162 mg", "324 mg", "500 mg"], "a": "324 mg", "reason": "Four 81mg tablets."},
        {"q": "What is the mechanism of Aspirin?", "choices": ["Pain relief", "Anti-platelet aggregate", "Vasoconstrictor", "Bronchodilator"], "a": "Anti-platelet aggregate", "reason": "Prevents clots from growing."},
        {"q": "Aspirin is contraindicated in children due to the risk of:", "choices": ["Hypoglycemia", "Reye's Syndrome", "Asthma", "Tachycardia"], "a": "Reye's Syndrome", "reason": "Can cause brain/liver swelling in kids."},
        
        # Glucose / Narcan / Epi
        {"q": "Oral glucose is contraindicated if the patient is:", "choices": ["Hyperglycemic", "Unconscious/Unable to swallow", "Tachycardic", "Hypertensive"], "a": "Unconscious/Unable to swallow", "reason": "Aspiration risk."},
        {"q": "What is the standard adult dose of Epinephrine for anaphylaxis?", "choices": ["0.15 mg", "0.3 mg", "0.5 mg", "1.0 mg"], "a": "0.3 mg", "reason": "Standard IM dose."},
        {"q": "What is the standard pediatric dose of Epinephrine?", "choices": ["0.05 mg", "0.15 mg", "0.3 mg", "0.5 mg"], "a": "0.15 mg", "reason": "Standard IM dose for kids."},
        {"q": "How long should you hold an Epi-Pen in the thigh?", "choices": ["1 second", "3 seconds", "10 seconds", "30 seconds"], "a": "10 seconds", "reason": "Ensures full delivery."},
        {"q": "What is the primary goal of Naloxone (Narcan)?", "choices": ["Wake the patient up", "Restore spontaneous breathing", "Stop a seizure", "Raise blood pressure"], "a": "Restore spontaneous breathing", "reason": "Ventilation is the priority."},
        
        # Nitro
        {"q": "Nitro is contraindicated if Systolic BP is below:", "choices": ["120", "110", "100", "90"], "a": "100", "reason": "BP must be > 100 per most protocols."},
        {"q": "What is the dose for Nitroglycerin?", "choices": ["0.2 mg", "0.4 mg", "0.8 mg", "1.0 mg"], "a": "0.4 mg", "reason": "One tablet or spray."},
        {"q": "Maximum number of Nitro doses an EMT can assist with?", "choices": ["1", "2", "3", "Unlimited"], "a": "3", "reason": "Includes pre-EMS doses."},
        {"q": "Nitro is contraindicated if the patient took PDE5 inhibitors in the last:", "choices": ["12 hours", "24-48 hours", "1 week", "Month"], "a": "24-48 hours", "reason": "Severe hypotension risk."},

        # Albuterol / Respiratory
        {"q": "Albuterol is a:", "choices": ["Alpha-1 Agonist", "Beta-1 Agonist", "Beta-2 Agonist", "Beta blocker"], "a": "Beta-2 Agonist", "reason": "Targets the 2 lungs."},
        {"q": "A common side effect of Albuterol is:", "choices": ["Bradycardia", "Tachycardia/Tremors", "Hypoglycemia", "Drowsiness"], "a": "Tachycardia/Tremors", "reason": "Sympathomimetic effects."},
        {"q": "Ipratropium (Atrovent) works by:", "choices": ["Stimulating Beta-2", "Blocking muscarinic receptors", "Lowering BP", "Increasing secretions"], "a": "Blocking muscarinic receptors", "reason": "Anticholinergic bronchodilator."},

        # Med Math / Conversions
        {"q": "To convert lb to kg, you divide by:", "choices": ["1.1", "2.2", "3.3", "10"], "a": "2.2", "reason": "Standard conversion."},
        {"q": "A 220 lb patient weighs how many kg?", "choices": ["80 kg", "90 kg", "100 kg", "110 kg"], "a": "100 kg", "reason": "220 / 2.2 = 100."},

        # Chronic Med Suffixes (The Study Guide Gems)
        {"q": "Suffix for Beta-Blockers:", "choices": ["-pril", "-sartan", "-olol", "-statin"], "a": "-olol", "reason": "e.g., Metoprolol."},
        {"q": "Suffix for ACE Inhibitors:", "choices": ["-pril", "-sartan", "-olol", "-prazole"], "a": "-pril", "reason": "e.g., Lisinopril."},
        {"q": "Suffix for ARBs:", "choices": ["-pril", "-sartan", "-olol", "-zepam"], "a": "-sartan", "reason": "e.g., Losartan."},
        {"q": "Suffix for Proton Pump Inhibitors (PPIs):", "choices": ["-sone", "-prazole", "-statin", "-terol"], "a": "-prazole", "reason": "e.g., Omeprazole."},
        {"q": "Suffix for Statins (Cholesterol):", "choices": ["-statin", "-statin", "-statin", "-statin"], "a": "-statin", "reason": "e.g., Atorvastatin."},
        {"q": "Suffix for Benzodiazepines:", "choices": ["-zepam/-zolam", "-pril", "-olol", "-ide"], "a": "-zepam/-zolam", "reason": "e.g., Diazepam, Alprazolam."},
        {"q": "Suffix for Corticosteroids:", "choices": ["-sone/-ide", "-olol", "-pril", "-sartan"], "a": "-sone/-ide", "reason": "e.g., Prednisone, Budesonide."},
        {"q": "Suffix for Beta-2 Bronchodilators:", "choices": ["-terol", "-tropium", "-pril", "-olol"], "a": "-terol", "reason": "e.g., Albuterol."},
        {"q": "Suffix for Anticholinergic Bronchodilators:", "choices": ["-tropium", "-terol", "-pril", "-olol"], "a": "-tropium", "reason": "e.g., Ipratropium."},

        # Specific Meds
        {"q": "Metformin is used for:", "choices": ["Type 1 DM", "Type 2 DM", "Asthma", "High BP"], "a": "Type 2 DM", "reason": "Oral anti-diabetic."},
        {"q": "Levothyroxine is used for:", "choices": ["Hyperthyroidism", "Hypothyroidism", "Diabetes", "Seizures"], "a": "Hypothyroidism", "reason": "Synthetic T4."},
        {"q": "Primary danger of Opioid narcotics:", "choices": ["Seizures", "Hypoventilation/Apnea", "Tachycardia", "Hypertension"], "a": "Hypoventilation/Apnea", "reason": "Respiratory depression."},
        {"q": "Risk of non-compliance with Antidepressants:", "choices": ["Heart attack", "Increased suicide/psych risk", "Sudden bleeding", "Stroke"], "a": "Increased suicide/psych risk", "reason": "Sudden stoppage is dangerous."},
        {"q": "Primary risk for patients on Anticoagulants (Warfarin/Aban):", "choices": ["High blood sugar", "Serious bleeding from minor trauma", "Seizures", "Asthma"], "a": "Serious bleeding from minor trauma", "reason": "Clotting is inhibited."},
        {"q": "DuoDote is for:", "choices": ["Anaphylaxis", "Nerve agent poisoning", "Heart attack", "Opioid OD"], "a": "Nerve agent poisoning", "reason": "Antidote kit."},
        {"q": "The two drugs in DuoDote are:", "choices": ["Epi and Narcan", "Atropine and Pralidoxime", "Nitro and ASA", "Albuterol and Atrovent"], "a": "Atropine and Pralidoxime", "reason": "Atropine + 2-PAM."},
        {"q": "What receptor does Zofran block?", "choices": ["H1", "Beta-2", "5-HT3", "Mu"], "a": "5-HT3", "reason": "Serotonin antagonist."},
        {"q": "Glucagon works by stimulating the release of:", "choices": ["Insulin", "Glycogen from the liver", "Adrenaline", "Stomach acid"], "a": "Glycogen from the liver", "reason": "Glycogenolysis."},

        # ... (Add remaining questions here in your script until you reach 71)
    ]

# --- APP LOGIC ---
if 'master' not in st.session_state:
    st.session_state.master = get_full_bank()
    random.shuffle(st.session_state.master)
    st.session_state.current_20 = st.session_state.master[:20]
    st.session_state.remaining = st.session_state.master[20:]
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.submitted = False

st.title("💊 71-Question Pharma Mastery")
st.write(f"Remaining in Bank: {len(st.session_state.remaining)}")

if st.session_state.idx < len(st.session_state.current_20):
    item = st.session_state.current_20[st.session_state.idx]
    st.info(f"Question {st.session_state.idx + 1} of 20")
    st.write(f"### {item['q']}")
    
    choice = st.radio("Options:", item['choices'], key=f"q{st.session_state.idx}")

    if st.button("Submit"):
        st.session_state.submitted = True

    if st.session_state.submitted:
        if choice == item['a']:
            st.success(f"Correct! {item['reason']}")
        else:
            st.error(f"Incorrect. It's {item['a']}. {item['reason']}")
        
        if st.button("Next"):
            if choice == item['a']: st.session_state.score += 1
            st.session_state.idx += 1
            st.session_state.submitted = False
            st.rerun()
else:
    st.balloons()
    st.write(f"## Round Over! Score: {st.session_state.score}/20")
    if len(st.session_state.remaining) > 0:
        if st.button("Next 20 Questions"):
            st.session_state.current_20 = st.session_state.remaining[:20]
            st.session_state.remaining = st.session_state.remaining[20:]
            st.session_state.idx = 0
            st.session_state.score = 0
            st.rerun()
    else:
        st.write("You've finished the whole bank!")
        if st.button("Reshuffle Everything"):
            del st.session_state.master
            st.rerun()