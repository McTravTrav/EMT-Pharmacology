import streamlit as st
import random

# --- THE DATASET FUNCTION ---
def get_full_bank():
    return [
        {"q": "What are the three key responsibilities of an EMT regarding medication safety?", "choices": ["Diagnosis, prescription, and follow-up", "Cross-check, correct dose/route, and monitoring", "Billing, driving, and inventory", "Intubation and sedation"], "a": "Cross-check, correct dose/route, and monitoring", "reason": "Standard safety responsibility."},
        {"q": "What is the difference between enteral and parenteral administration?", "choices": ["Enteral is inhaled; Parenteral is ingested", "Enteral is ingested; Parenteral is injected/inhaled", "Enteral is for adults; Parenteral is for kids", "There is no difference"], "a": "Enteral is ingested; Parenteral is injected/inhaled", "reason": "Enteral = GI tract; Parenteral = Bypasses GI."},
        {"q": "Name the three main routes of injection used in EMS.", "choices": ["Oral, Rectal, Nasal", "SC, IM, IV", "Buccal, SL, PO", "Topical, Ocular, Nasal"], "a": "SC, IM, IV", "reason": "Subcutaneous, Intramuscular, and Intravenous."},
        {"q": "Define 'Pharmacodynamics'.", "choices": ["How the body moves a drug", "How a drug affects the body", "The cost of the drug", "The shelf life"], "a": "How a drug affects the body", "reason": "Dynamics = what the drug DOES to the body."},
        {"q": "What is the difference between generic and trade names?", "choices": ["Generic is brand; Trade is chemical", "Generic is chemical; Trade is brand", "Generic is liquid; Trade is solid", "They are the same"], "a": "Generic is chemical; Trade is brand", "reason": "Ibuprofen (Generic) vs Advil (Trade)."},
        {"q": "What is the difference between 'assisting' and 'administering'?", "choices": ["Assisting is for doctors", "Assisting is patient's med; Administering is EMS med", "Administering is for doctors", "No difference"], "a": "Assisting is patient's med; Administering is EMS med", "reason": "Scope of practice definition."},
        {"q": "What are the 'Six Rights'?", "choices": ["Patient, Drug, Dose, Route, Time, Documentation", "Person, Place, Thing, Time, Action, Price", "History, Vitals, Age, Weight, Sex, Race", "Drug, Bottle, Color, Size, Shape, Label"], "a": "Patient, Drug, Dose, Route, Time, Documentation", "reason": "Standard safety protocol."},
        {"q": "What is the adult dose for Aspirin for cardiac chest pain?", "choices": ["81 mg", "162 mg", "324 mg", "500 mg"], "a": "324 mg", "reason": "Four 81mg tablets."},
        {"q": "What is the mechanism of Aspirin?", "choices": ["Pain relief", "Anti-platelet aggregate", "Vasoconstrictor", "Bronchodilator"], "a": "Anti-platelet aggregate", "reason": "Prevents clots from growing."},
        {"q": "Aspirin is contraindicated in children due to:", "choices": ["Hypoglycemia", "Reye's Syndrome", "Asthma", "Tachycardia"], "a": "Reye's Syndrome", "reason": "Brain/liver swelling risk."},
        {"q": "Oral glucose is contraindicated if the patient is:", "choices": ["Hyperglycemic", "Unconscious/Unable to swallow", "Tachycardic", "Hypertensive"], "a": "Unconscious/Unable to swallow", "reason": "Aspiration risk."},
        {"q": "Standard adult dose of Epinephrine for anaphylaxis?", "choices": ["0.15 mg", "0.3 mg", "0.5 mg", "1.0 mg"], "a": "0.3 mg", "reason": "Standard IM dose."},
        {"q": "Standard pediatric dose of Epinephrine?", "choices": ["0.05 mg", "0.15 mg", "0.3 mg", "0.5 mg"], "a": "0.15 mg", "reason": "Standard IM dose for kids."},
        {"q": "Nitro is contraindicated if Systolic BP is below:", "choices": ["120", "110", "100", "90"], "a": "100", "reason": "Must be > 100."},
        {"q": "What is the dose for Nitroglycerin?", "choices": ["0.2 mg", "0.4 mg", "0.8 mg", "1.0 mg"], "a": "0.4 mg", "reason": "One tablet or spray."},
        {"q": "Nitro is contraindicated if PDE5 inhibitors taken in last:", "choices": ["12 hours", "24-48 hours", "1 week", "Month"], "a": "24-48 hours", "reason": "Severe hypotension risk."},
        {"q": "Albuterol is a:", "choices": ["Alpha-1 Agonist", "Beta-1 Agonist", "Beta-2 Agonist", "Beta blocker"], "a": "Beta-2 Agonist", "reason": "2 Lungs = Beta 2."},
        {"q": "Ipratropium (Atrovent) works by:", "choices": ["Stimulating Beta-2", "Blocking muscarinic receptors", "Lowering BP", "Increasing secretions"], "a": "Blocking muscarinic receptors", "reason": "Anticholinergic."},
        {"q": "220 lb patient weighs how many kg?", "choices": ["80 kg", "90 kg", "100 kg", "110 kg"], "a": "100 kg", "reason": "220 / 2.2 = 100."},
        {"q": "Suffix for Beta-Blockers:", "choices": ["-pril", "-sartan", "-olol", "-statin"], "a": "-olol", "reason": "e.g., Metoprolol."},
        {"q": "Suffix for ACE Inhibitors:", "choices": ["-pril", "-sartan", "-olol", "-prazole"], "a": "-pril", "reason": "e.g., Lisinopril."},
        {"q": "Suffix for ARBs:", "choices": ["-pril", "-sartan", "-olol", "-zepam"], "a": "-sartan", "reason": "e.g., Losartan."},
        {"q": "Suffix for Proton Pump Inhibitors (PPIs):", "choices": ["-sone", "-prazole", "-statin", "-terol"], "a": "-prazole", "reason": "e.g., Omeprazole."},
        {"q": "Suffix for Benzodiazepines:", "choices": ["-zepam/-zolam", "-pril", "-olol", "-ide"], "a": "-zepam/-zolam", "reason": "e.g., Diazepam."},
        {"q": "Suffix for Corticosteroids:", "choices": ["-sone/-ide", "-olol", "-pril", "-sartan"], "a": "-sone/-ide", "reason": "e.g., Prednisone."},
        {"q": "Metformin is used for:", "choices": ["Type 1 DM", "Type 2 DM", "Asthma", "High BP"], "a": "Type 2 DM", "reason": "Oral anti-diabetic."},
        {"q": "Primary danger of Opioid narcotics:", "choices": ["Seizures", "Hypoventilation/Apnea", "Tachycardia", "Hypertension"], "a": "Hypoventilation/Apnea", "reason": "Respiratory depression."},
        {"q": "Primary risk for Anticoagulants (Warfarin/Aban):", "choices": ["Sugar", "Serious bleeding from minor trauma", "Seizures", "Asthma"], "a": "Serious bleeding from minor trauma", "reason": "Clotting inhibited."},
        {"q": "DuoDote drugs are:", "choices": ["Epi/Narcan", "Atropine/Pralidoxime", "Nitro/ASA", "Albuterol/Atrovent"], "a": "Atropine/Pralidoxime", "reason": "Atropine + 2-PAM."},
        {"q": "What is the standard adult dose for activated charcoal?", "choices": ["1-2 mg", "25-50 g", "100 mg/kg", "15-25 g"], "a": "25-50 g", "reason": "Adult standard dose."},
        {"q": "Mechanism of Narcan:", "choices": ["Sedative", "Competitive opioid antagonist", "Beta-blocker", "Benzodiazepine"], "a": "Competitive opioid antagonist", "reason": "Competes for receptors."},
        {"q": "Zofran blocks which receptor?", "choices": ["H1", "Mu", "5-HT3", "Beta-2"], "a": "5-HT3", "reason": "Serotonin antagonist."},
        {"q": "Glucagon raises sugar by:", "choices": ["Fat to sugar", "Hepatic glycogenolysis", "Blocking insulin", "GI absorption"], "a": "Hepatic glycogenolysis", "reason": "Liver conversion."},
        {"q": "Dose of Benadryl:", "choices": ["5-10 mg", "25-50 mg", "75-100 mg", "0.3 mg"], "a": "25-50 mg", "reason": "Adult standard range."},
        {"q": "How many lb in 1 kg?", "choices": ["1.1", "2.2", "3.3", "4.4"], "a": "2.2", "reason": "Standard conversion."},
        {"q": "What is pharmacodynamics?", "choices": ["Body on drug", "Drug on body", "Drug cost", "Drug weight"], "a": "Drug on body", "reason": "Action/Effect."},
        {"q": "Side effect vs Untoward effect:", "choices": ["Same", "Predictable vs Harmful/Unexpected", "Kids vs Adults", "Desired vs Boring"], "a": "Predictable vs Harmful/Unexpected", "reason": "Definition of clinical effects."},
        {"q": "Levothyroxine treats:", "choices": ["Hyperthyroid", "Hypothyroid", "Diabetes", "Seizures"], "a": "Hypothyroid", "reason": "Synthetic T4."},
        {"q": "DuoNeb is:", "choices": ["Epi/Narcan", "Albuterol/Ipratropium", "ASA/Nitro", "O2/Glucose"], "a": "Albuterol/Ipratropium", "reason": "2.5mg Albuterol/0.5mg Atrovent."},
        {"q": "H1 receptor blocker:", "choices": ["Albuterol", "Diphenhydramine", "ASA", "Nitro"], "a": "Diphenhydramine", "reason": "Antihistamine."},
        {"q": "PPI purpose:", "choices": ["Slow HR", "Lower BP", "Reduce stomach acid", "Stop itching"], "a": "Reduce stomach acid", "reason": "Stomach protection."},
        {"q": "Anticonvulsant purpose:", "choices": ["Stop BP", "Reduce seizure risk", "Stop asthma", "Acid reduction"], "a": "Reduce seizure risk", "reason": "Maintenance med."},
        {"q": "Statins treat:", "choices": ["BP", "Sugar", "Cholesterol", "Pain"], "a": "Cholesterol", "reason": "e.g., Lipitor."},
        {"q": "Calcium Channel Blocker suffix:", "choices": ["-olol", "-pril", "-dipine", "-sartan"], "a": "-dipine", "reason": "e.g., Amlodipine."},
        {"q": "Aspirin form:", "choices": ["Gel", "Gas", "Chewable tablet", "Liquid"], "a": "Chewable tablet", "reason": "Speeds absorption."},
        {"q": "Narcan goal:", "choices": ["Wake up", "Breathe", "Stop pain", "Stop vomiting"], "a": "Breathe", "reason": "Restore ventilation."},
        {"q": "Nitro route:", "choices": ["PO", "SL", "IM", "IN"], "a": "SL", "reason": "Sublingual."},
        {"q": "Epi route:", "choices": ["SC", "IM", "IV", "PO"], "a": "IM", "reason": "Intramuscular lateral thigh."},
        {"q": "Glucose route:", "choices": ["PO", "SL", "Buccal", "IM"], "a": "Buccal", "reason": "Cheek/Gum."},
        {"q": "Charcoal route:", "choices": ["IM", "IV", "PO", "IN"], "a": "PO", "reason": "Oral slurry."},
        {"q": "O2 goal:", "choices": ["100% SpO2", "94-99% SpO2", "Stop pain", "Awaken"], "a": "94-99% SpO2", "reason": "Normal physiological range."},
        {"q": "ASA indication:", "choices": ["Headache", "Cardiac Chest Pain", "Fever", "Broken leg"], "a": "Cardiac Chest Pain", "reason": "Anti-platelet for AMI."},
        {"q": "Glucose indication:", "choices": ["Hyperglycemia", "Hypoglycemia", "Heart Attack", "Stroke"], "a": "Hypoglycemia", "reason": "Blood sugar < 60-70."},
        {"q": "Epi indication:", "choices": ["Itching", "Anaphylaxis + Airway/BP", "Asthma", "High BP"], "a": "Anaphylaxis + Airway/BP", "reason": "Life-threatening allergy."},
        {"q": "Nitro indication:", "choices": ["Headache", "Chest Pain/Angina", "Hypotension", "Seizure"], "a": "Chest Pain/Angina", "reason": "Vasodilation."},
        {"q": "Narcan indication:", "choices": ["Seizure", "Opioid OD + Resp Depression", "Cardiac arrest", "Hypoglycemia"], "a": "Opioid OD + Resp Depression", "reason": "Antidote."},
        {"q": "Albuterol indication:", "choices": ["Chest pain", "Bronchospasm/Asthma", "Overdose", "Low sugar"], "a": "Bronchospasm/Asthma", "reason": "Bronchodilation."},
        {"q": "Zofran indication:", "choices": ["Pain", "Nausea/Vomiting", "Seizure", "Bleeding"], "a": "Nausea/Vomiting", "reason": "Antiemetic."},
        {"q": "Benadryl indication:", "choices": ["Severe asthma", "Allergic reaction/Urticaria", "Low BP", "Chest pain"], "a": "Allergic reaction/Urticaria", "reason": "H1 blocker."},
        {"q": "Glucagon indication:", "choices": ["High sugar", "Hypoglycemia (no IV access)", "Pain", "Nausea"], "a": "Hypoglycemia (no IV access)", "reason": "IM sugar backup."},
        {"q": "DuoDote indication:", "choices": ["Opioids", "Nerve Agent/Organophosphate", "AMI", "Stroke"], "a": "Nerve Agent/Organophosphate", "reason": "Antidote."},
        {"q": "DuoNeb indication:", "choices": ["Heart failure", "COPD/Asthma exacerbation", "Pain", "Nausea"], "a": "COPD/Asthma exacerbation", "reason": "Dual bronchodilators."},
        {"q": "Suffix for Bronchodilators:", "choices": ["-olol", "-pril", "-terol", "-sartan"], "a": "-terol", "reason": "Beta-2 agonists."},
        {"q": "Suffix for Cholesterol meds:", "choices": ["-statin", "-statin", "-statin", "-statin"], "a": "-statin", "reason": "HMG-CoA inhibitors."},
        {"q": "Atropine purpose in DuoDote:", "choices": ["Stop bleeding", "Dry secretions/Increase HR", "Lower sugar", "Induce sleep"], "a": "Dry secretions/Increase HR", "reason": "Parasympatholytic."},
        {"q": "2-PAM purpose in DuoDote:", "choices": ["Stop pain", "Reactivate Acetylcholinesterase", "Lower BP", "Stop seizure"], "a": "Reactivate Acetylcholinesterase", "reason": "Chemical antidote."},
        {"q": "Metoprolol is a:", "choices": ["ACE Inhibitor", "Beta-Blocker", "ARB", "Statin"], "a": "Beta-Blocker", "reason": "-olol suffix."},
        {"q": "Lisinopril is a:", "choices": ["ACE Inhibitor", "Beta-Blocker", "ARB", "Statin"], "a": "ACE Inhibitor", "reason": "-pril suffix."},
        {"q": "Losartan is a:", "choices": ["ACE Inhibitor", "Beta-Blocker", "ARB", "Statin"], "a": "ARB", "reason": "-sartan suffix."},
        {"q": "Omeprazole is a:", "choices": ["PPI", "Beta-Blocker", "ARB", "Statin"], "a": "PPI", "reason": "-prazole suffix."},
        {"q": "Diazepam is a:", "choices": ["Benzodiazepine", "Opioid", "Anticoagulant", "Statin"], "a": "Benzodiazepine", "reason": "-zepam suffix."}
        ### PASTE THE LIST OF QUESTIONS FROM STEP 2 HERE ###
    ]

# --- SESSION STATE MANAGEMENT ---
if 'master' not in st.session_state:
    st.session_state.master = get_full_bank()
    random.shuffle(st.session_state.master)
    # Pull first 20
    st.session_state.current_20 = st.session_state.master[:20]
    st.session_state.remaining = st.session_state.master[20:]
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.submitted = False

st.title("🚑 EMT Pharma Mastery: The Full 71")
st.write(f"Questions left in total bank: {len(st.session_state.remaining) + (len(st.session_state.current_20) - st.session_state.idx)}")

# --- QUIZ INTERFACE ---
if st.session_state.idx < len(st.session_state.current_20):
    item = st.session_state.current_20[st.session_state.idx]
    st.subheader(f"Question {st.session_state.idx + 1} of 20")
    st.info(item['q'])
    
    choice = st.radio("Select your answer:", item['choices'], key=f"q{st.session_state.idx}_{len(st.session_state.remaining)}")

    if st.button("Submit Answer"):
        st.session_state.submitted = True

    if st.session_state.submitted:
        if choice == item['a']:
            st.success(f"CORRECT! {item['reason']}")
        else:
            st.error(f"INCORRECT. The answer is: {item['a']}. {item['reason']}")
        
        if st.button("Move to Next Question"):
            if choice == item['a']: st.session_state.score += 1
            st.session_state.idx += 1
            st.session_state.submitted = False
            st.rerun()
else:
    # --- END OF ROUND ---
    st.balloons()
    st.header("Round Complete!")
    st.write(f"You scored {st.session_state.score} / 20")
    
    if len(st.session_state.remaining) > 0:
        if st.button("Start Next 20 Questions"):
            st.session_state.current_20 = st.session_state.remaining[:20]
            st.session_state.remaining = st.session_state.remaining[20:]
            st.session_state.idx = 0
            st.session_state.score = 0
            st.rerun()
    else:
        st.success("🎉 You have mastered all 71 questions!")
        if st.button("Reset and Reshuffle Entire Bank"):
            del st.session_state.master
            st.rerun()