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
        st.error("Each team must have exactly 2 players.")
    else:
        # Identify bench players (players not currently playing)
        current_players = set(current_team_a + current_team_b)
        previous_players = set(previous_team_a + previous_team_b)
        bench_players = [p for p in players if p not in current_players]

        if losing_team == "Team A":
            if len(bench_players) < 2:
                st.warning("Not enough players on the bench to replace Team A.")
            else:
                # Suggest replacement for Team A
                next_pair = random.sample(bench_players, 2)
                st.success(f"Suggested next Team A: {next_pair}")
        elif losing_team == "Team B":
            if len(bench_players) < 2:
                st.warning("Not enough players on the bench to replace Team B.")
            else:
                # Suggest replacement for Team B
                next_pair = random.sample(bench_players, 2)
                st.success(f"Suggested next Team B: {next_pair}")
        else:
            st.info("No changes made as no team lost.")
