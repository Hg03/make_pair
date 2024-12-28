import streamlit as st
import random

# App title
st.title("Dynamic Badminton Team Rotation")

# Input total number of players
st.header("Setup")
total_players = st.number_input(
    "Enter the total number of players:", min_value=4, max_value=20, value=9, step=1
)
players = list(range(1, total_players + 1))

# Display player list
st.write(f"Total players: {players}")

# Input for current and previous teams
st.header("Current Match")
current_team_a = st.multiselect(
    "Select Team A Players", players, key="current_a", max_selections=2
)
current_team_b = st.multiselect(
    "Select Team B Players", players, key="current_b", max_selections=2
)

st.header("Previous Match")
previous_team_a = st.multiselect(
    "Select Previous Team A Players", players, key="previous_a", max_selections=2
)
previous_team_b = st.multiselect(
    "Select Previous Team B Players", players, key="previous_b", max_selections=2
)

# Losing team selection
st.header("Match Result")
losing_team = st.selectbox("Which team lost?", ["Team A", "Team B", "None"])

# Suggest next players
if st.button("Get Next Pair"):
    if not current_team_a or not current_team_b:
        st.error("Please select players for both current teams.")
    elif len(current_team_a) != 2 or len(current_team_b) != 2:
