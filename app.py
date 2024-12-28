import streamlit as st
import random

# List of players (1-9)
players = list(range(1, 10))

# App title
st.title("Badminton Team Rotation")

# Input for current and previous teams
st.header("Current Match")
current_team_a = st.multiselect("Select Team A Players", players, key="current_a")
current_team_b = st.multiselect("Select Team B Players", players, key="current_b")

st.header("Previous Match")
previous_team_a = st.multiselect("Select Previous Team A Players", players, key="previous_a")
previous_team_b = st.multiselect("Select Previous Team B Players", players, key="previous_b")

# Losing team selection
st.header("Match Result")
losing_team = st.selectbox("Which team lost?", ["Team A", "Team B", "None"])

# Suggest next players
if st.button("Get Next Pair"):
    if not current_team_a or not current_team_b:
        st.error("Please select players for both current teams.")
    else:
        # Identify bench players (players not currently playing)
        current_players = set(current_team_a + current_team_b)
        previous_players = set(previous_team_a + previous_team_b)
        bench_players = [p for p in players if p not in current_players]

        if losing_team == "Team A":
            # Suggest replacement for Team A
            next_pair = random.sample(bench_players, 2)
            st.success(f"Suggested next Team A: {next_pair}")
        elif losing_team == "Team B":
            # Suggest replacement for Team B
            next_pair = random.sample(bench_players, 2)
            st.success(f"Suggested next Team B: {next_pair}")
        else:
            st.info("No changes made as no team lost.")
