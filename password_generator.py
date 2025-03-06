import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Always include letters
    
    if use_digits:
        characters += string.digits  # Add digits if selected
    
    if use_special:  # Fix indentation here
        characters += string.punctuation  # Add special characters if selected

    return ''.join(random.choice(characters) for _ in range(length))  # Generate password

st.title("Password Generator")

length = st.slider("Select password length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Use digits")
use_special = st.checkbox("Use special characters")

if st.button("Generate password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated password: `{password}`")
    st.write("------------------------")
