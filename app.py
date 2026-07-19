import streamlit as st
from ai_helper import generate_minutes
st.set_page_config(
    page_title="AI Meeting Minutes Generator",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Meeting Minutes Generator")

st.write(
    "Paste your meeting notes below and click **Generate Minutes**."
)

meeting_notes = st.text_area(
    "Meeting Notes",
    height=250
)

if st.button("Generate Minutes"):

    if meeting_notes.strip() == "":
        st.warning("Please enter meeting notes.")
    else:
        with st.spinner("Generating Meeting Minutes..."):

            result = generate_minutes(meeting_notes)

        st.success("Meeting Minutes Generated Successfully!")

        st.markdown(result)