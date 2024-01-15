import streamlit as st 
# Title of the app
st.title("My Streamlit App")

# Adding a text input widget
user_input = st.text_input("Enter your name", "John Doe")

# Displaying a message
st.write(f"Hello, {user_input}!")

# Adding a button
if st.button("Click me"):
    st.write("Button clicked!")