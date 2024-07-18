import streamlit as st

def get_user_input():
  heart_rate = st.number_input("What is your heartrate?")
  blood_pressure = st.number_input("What is your bloodpressure?")
  chest_pain = st.number_input("Do you have chest pain? Enter 1 for yes, 0 for no.")
  age = st.number_input("What is your age?")
  high_blood_sugar = st.number_input("Do you have high_blood_sugar? Enter 1 for yes, 0 for no.")
  cholesterol = st.number_input("What is your cholesterol level?")
  exercise_pain = st.number_input("Do you have exercise pain? Enter 1 for yes, 0 for no.")
  input_features = [[blood_pressure, heart_rate, chest_pain, age, high_blood_sugar, cholesterol, exercise_pain]]
  return input_features
