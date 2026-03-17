import streamlit as st
import st_yled
import datetime
from loading_css import local_css
from susans_meds import SUSANSMEDS
from susans_symps import SUSANSYMP

st_yled.init()
local_css("style.css")

if "medications" not in st.session_state:
    st.session_state.medications = SUSANSMEDS

st.sidebar.title("Ctrl+Care")

st.sidebar.markdown(
    """
    <div style="background-color:#bccfd9; padding:10px; border-color:#9aadba; border-radius:8px;">
        <b>Susan Martinez</b><br>
        Age 68 - 4 medications
    </div>
    """,
    unsafe_allow_html=True
)
pages = st.sidebar.radio("Directory", ["Prescription Hub", "Prescription Schedule", "Symptom Logging"])

if pages == "Prescription Hub":
    st_yled.title("Prescription Hub", color = "#9aadba", font_size = "2.5rem")
    st_yled.title("Hello Susan!", font_size = "2.0rem")
    st.caption("Check out and add new prescriptions!")
    st.divider()

    with st.expander("Add a Perscription"):
        with st.form(key="my_form"):
            drug_name = st.text_input("Perscription name")
            dose_amount = st.text_input("How much?")
            frequency_taken = st.text_input("How often each day do you need to take it?")
            time_taken = st.text_input("What time?")
            perscription_resoning = st.text_input("What is this medication for?")
            perscription_instructions = st.text_input("How should the perscription be taken?")
            adding_medication = st.form_submit_button("Add Perscription")

            if adding_medication and drug_name and frequency_taken and time_taken and perscription_resoning and perscription_instructions:
                
                st.session_state.medications.append({
                "name": drug_name,
                "dose": dose_amount,
                "frequency": frequency_taken,
                "time": time_taken,
                "purpose": perscription_resoning,
                "instructions": perscription_instructions
            })
            
                st.success(f"Added {drug_name}!")
            
            
        # "name": "Lisinopril",
        # "dose": "10mg",
        # "frequency": "Once daily",
        # "time": "8:00 AM",
        # "purpose": "Blood Pressure",
        # "instructions": "Take on empty stomach"
    for med in st.session_state.medications:
        container = st.container(border=True)
        container.markdown(f"**{med['name']}** — {med['dose']}")
        container.markdown(f"{med['frequency']} : {med['time']}")
        container.caption(f"{med['purpose']} — {med['instructions']}")

    


elif pages == "Prescription Schedule":
    st_yled.title("Prescription Hub", color = "#9aadba", font_size = "2.5rem")
    st_yled.title("Hello Susan!", font_size = "2.0rem")
    st.caption("Known when to take your subscriptions!")
    st.divider()
    

elif pages == "Symptom Logging":
    st_yled.title("Symptom Logging", color = "#9aadba", font_size = "2.5rem")
    st.header("Hello Susan!")
    st.caption("How are you feeling today?")
    st.divider()

    with st.form(key = "symptom_form"):
    ## use multiselect to choose symptoms
        symptom_opt1ons = st.multiselect(
        "What are your current symptoms?",
        ["Nausea", "Fatigue", "Rash", 
        "Shortness of Breath", "Dizziness", 
        "Headaches","Swelling","Chest Pain", "High Blood Pressure",
        "Low Blood Pressure", "Insomnia", "Weight Loss", "Weight Gain",
        "Cramping", "Confusion", "Diarrhea", "Vomiting", "Constipation"],
        accept_new_options=True,
    )

        ## Date of symptom

        d = st.date_input("When did symptom(s) first occur?", value = "today")

        ## rate severity of pain
        pain_options = st.number_input(
            "On a scale of 1-5, how severe are the symptoms?",
            min_value=1, max_value=5
            )

        ## for notes, allow user to write any extra information

        extra_notes = st.text_area(
            "Any other information?", value = "N/A"
        )

        adding_symptom = st.form_submit_button("Add Symptom")

        if adding_symptom and extra_notes and pain_options and d and symptom_opt1ons:
            st.session_state.symptoms.append({
                "date" : d,
                "symptom" : symptom_opt1ons,
                "severity" : pain_options,
                "notes" : extra_notes
            })
            st.success(f"Added symptom!")

    for symp in st.session_state.symptoms:
        container = st.container(border=True)
        container.markdown(f"**{symp['date']}**")
        container.markdown(f"**Symptom(s)**: {', '.join(symp['symptom'])}")
        container.markdown(f"**Pain Scale (1-5)**: {symp['severity']}")
        container.markdown(f"**Notes**: {symp['notes']}")





