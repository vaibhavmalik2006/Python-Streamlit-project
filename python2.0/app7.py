import streamlit as st
import random


st.title("✊ 🤚 ✌️ Rock Paper Scissors Game")

# Choices
choices = ["Rock", "Paper", "Scissors"]
emoji = {"Rock": "✊", "Paper": "🤚", "Scissors": "✌️"}

# User choice
user_choice = st.radio("Choose your move:", choices, horizontal=True)

# When button clicked
if st.button("Play"):
    computer_choice = random.choice(choices)

    # Display choices
    st.markdown(f"**You chose:** {emoji[user_choice]} {user_choice}")
    st.markdown(f"**Computer chose:** {emoji[computer_choice]} {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a draw!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You win!"
    else:
        result = "💻 Computer wins!"

    st.subheader(result)
