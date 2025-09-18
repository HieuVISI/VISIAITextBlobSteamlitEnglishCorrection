import streamlit as st
from textblob import TextBlob

st.title("Spell Checker with TextBlob")

# Input box
user_input = st.text_input("Enter words separated by spaces:")

if st.button("Check"):
    if user_input.strip():
        words = user_input.split()
        st.write("### Results:")
        for word in words:
            blob = TextBlob(word)
            corrected = str(blob.correct())
            if corrected.lower() == word.lower():
                st.success(f"✅ {word} is correct")
            else:
                st.error(f"❌ {word} → {corrected}")
    else:
        st.warning("Please enter at least one word.")
