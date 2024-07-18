import streamlit as st

def get_app_response(prediction):
  if prediction == 1: # CHANGE THIS!
    st.write("It is likely that you have heart disease 🙁")
  # ADD MORE IF / ELIF STATEMENTS HERE
  else:
    st.write("It is unlikely that you have heart disease 🙂")
