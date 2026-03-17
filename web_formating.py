import streamlit as st
import st_yled
from loading_css import local_css
from susans_meds import SUSANSMEDS

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
    st_yled.title("Prescription Schedule", color = "#9aadba", font_size = "2.5rem")
    st.header("Hello Susan!")
    st.subheader("Known when to take your subscriptions!")

elif pages == "Symptom Logging":
     st_yled.title("Symptom Logging", color = "#9aadba", font_size = "2.5rem")
     st.header("Hello Susan!")
     st.caption("How are you feeling today?")







