import streamlit as st
import pickle
import pandas as pd

# -----------------------------
# TEAMS & CITIES
# -----------------------------
teams = ['Sunrisers Hyderabad',
         'Mumbai Indians',
         'Royal Challengers Bangalore',
         'Kolkata Knight Riders',
         'Kings XI Punjab',
         'Chennai Super Kings',
         'Rajasthan Royals',
         'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

# -----------------------------
# LOAD MODEL
# -----------------------------
pipe = pickle.load(open('pipe.pkl', 'rb'))

# -----------------------------
# UI
# -----------------------------
st.title('🏏 IPL Win Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select Batting Team', sorted(teams))

with col2:
    bowling_team = st.selectbox('Select Bowling Team', sorted(teams))

selected_city = st.selectbox('Select Host City', sorted(cities))

target = st.number_input('Target Score', min_value=1)

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Current Score', min_value=0)

with col4:
    overs = st.number_input('Overs Completed', min_value=0.1, max_value=20.0, step=0.1)

with col5:
    wickets_out = st.number_input('Wickets Out', min_value=0, max_value=10)

# -----------------------------
# PREDICTION
# -----------------------------
if st.button('Predict Probability'):

    # VALIDATIONS
    if batting_team == bowling_team:
        st.error("Batting and Bowling teams must be different!")
        st.stop()

    if overs <= 0:
        st.error("Overs must be greater than 0")
        st.stop()

    if score > target:
        st.error("Score cannot exceed target")
        st.stop()

    # CALCULATIONS
    runs_left = target - score
    balls_left = 120 - int(overs * 6)
    wickets = 10 - wickets_out

    # -----------------------------
    # 🚨 MATCH END CONDITIONS
    # -----------------------------
    if wickets_out == 10:
        st.error("All wickets are gone. Batting team lost!")
        st.success(f"{bowling_team}: 100%")
        st.error(f"{batting_team}: 0%")
        st.stop()

    if balls_left <= 0:
        if score >= target:
            st.success(f"{batting_team}: 100%")
            st.error(f"{bowling_team}: 0%")
        else:
            st.success(f"{bowling_team}: 100%")
            st.error(f"{batting_team}: 0%")
        st.stop()

    if score == target:
        st.success(f"{batting_team} already won!")
        st.stop()

    # METRICS
    crr = score / overs
    rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

    # MODEL INPUT
    input_df = pd.DataFrame({
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'city': [selected_city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets': [wickets],
        'total_runs_x': [target],
        'crr': [crr],
        'rrr': [rrr]
    })

    # PREDICTION
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]

    # -----------------------------
    # 🚨 LOW WICKET CORRECTION (IMPORTANT)
    # -----------------------------
    if wickets <= 2:
        win = win * 0.4   # reduce win probability
        loss = 1 - win

    # -----------------------------
    # OUTPUT
    # -----------------------------
    st.subheader("Winning Probability")

    st.success(f"{batting_team}: {round(win * 100)}%")
    st.error(f"{bowling_team}: {round(loss * 100)}%")