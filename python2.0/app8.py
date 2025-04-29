# ludo_game.py

import streamlit as st
import random

# Initialize session state
if 'positions' not in st.session_state:
    st.session_state.positions = {'Player 1': 0, 'Player 2': 0}
if 'turn' not in st.session_state:
    st.session_state.turn = 'Player 1'
if 'dice' not in st.session_state:
    st.session_state.dice = 0
if 'winner' not in st.session_state:
    st.session_state.winner = None

st.title("🎲 Simple Ludo Game")

st.write(f"**Current Turn:** {st.session_state.turn}")

if st.session_state.winner:
    st.success(f"🏆 {st.session_state.winner} wins the game!")
    if st.button("Play Again"):
        st.session_state.positions = {'Player 1': 0, 'Player 2': 0}
        st.session_state.turn = 'Player 1'
        st.session_state.dice = 0
        st.session_state.winner = None
    st.stop()

# Roll Dice
if st.button("Roll Dice"):
    dice_value = random.randint(1, 6)
    st.session_state.dice = dice_value
    st.success(f"{st.session_state.turn} rolled a {dice_value}")

    # Move player
    player = st.session_state.turn
    st.session_state.positions[player] += dice_value

    # Check for win condition
    if st.session_state.positions[player] >= 30:
        st.session_state.winner = player
    else:
        # Switch turns
        st.session_state.turn = 'Player 2' if player == 'Player 1' else 'Player 1'

# Display player positions
st.write("### Positions")
st.write(f"🚩 Player 1: {st.session_state.positions['Player 1']}")
st.write(f"🚩 Player 2: {st.session_state.positions['Player 2']}")

# Visualize progress (like a progress bar)
st.progress(min(st.session_state.positions['Player 1'], 30) / 30)
st.progress(min(st.session_state.positions['Player 2'], 30) / 30)
