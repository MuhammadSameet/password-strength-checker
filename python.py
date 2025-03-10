# append ka use variable ke andar new value ka add karega


import streamlit as st
import re

# Configure the page
st.set_page_config(page_title="Password Strength Checker")

# Title and description
st.title("🔐 Password Strength Checker")

st.markdown("""
## Welcome to the Ultimate Password Strength Checker
Use this tool to check the strength of your password and make it more **secure**.
""")

# User input for password
password = st.text_input("Enter your Password", type="password")

# Button to check password strength
if st.button("Check Password Strength"):
    feedback = []
    score = 0

    if password:
        # Check password length
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ Password must be at least 8 characters long.")

        # Check uppercase and lowercase letters
        if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("❌ Password must contain both uppercase and lowercase letters.")

        # Check for numbers
        if re.search(r'[0-9]', password):
            score += 1
        else:
            feedback.append("❌ Password must contain at least one number.")

        # Check for special characters
        if re.search(r'[!@#$%^&*]', password):
            score += 1
        else:
            feedback.append("❌ Password must contain at least one special character ( !@#$%^&* ).")

        # Strength evaluation
        if score == 4:
            feedback.append("✅ Your Password is Strong.")
        elif score == 3:
            feedback.append("🟡 Your Password is Medium strength, it could be stronger.")
        else:
            feedback.append("🔴 Your Password is Weak, please make it stronger.")

        # Display feedback
        st.markdown("## Password Strength")
        for tip in feedback:
            st.write(tip)
    else:
        st.info("Please enter your password to check its strength.")
