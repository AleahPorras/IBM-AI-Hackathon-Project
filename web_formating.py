import streamlit as st
import st_yled
from loading_css import local_css
from susans_meds import SUSANSMEDS

st_yled.init()
local_css("style.css")






if "medications" not in st.session_state:
    st.session_state.medications = SUSANSMEDS

st.sidebar.title("Ctrl+Care")
st.sidebar.info("**Susan Martinez**\n\nAge 68 · 4 medications")
pages = st.sidebar.radio("Directory", ["Prescription Hub", "Prescription Schedule", "Symptom Logging"])

if pages == "Prescription Hub":
    st_yled.title("Prescription Hub", color = "#9aadba", font_size = "2.5rem")
    st_yled.title("Hello Susan!", font_size = "2.0rem")
    st.caption("Check out and add new subscriptions!")

elif pages == "Prescription Schedule":
    st_yled.title("Prescription Schedule", color = "#9aadba", font_size = "2.5rem")
    st.header("Hello Susan!")
    st.subheader("Known when to take your subscriptions!")

elif pages == "Symptom Logging":
     st_yled.title("Symptom Logging", color = "#9aadba", font_size = "2.5rem")
     st.header("Hello Susan!")
     st.caption("How are you feeling today?")