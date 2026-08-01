import streamlit as st
#app title

st.title("🌸Greeting app🌸")

# Text input
name = st.text_input("Please Enter Your Name😊")

#Button

if st.button("💖Greet Me"):
    if name.strip():
        st.balloons()


        st.markdown(f"""
        #🌸Welcome to my heart 💟🌹, {name}!🌸

        
        a 🌹 for the 🌹


        I'm so happy you are here!🥺😍🤗


        💟💟💟Have an amazing day!💟💟💟

       🤗 ❤ Keep Smiling ❤ 🤗

       """)
         
    else:
        st.warning("⚠️ Please enter your name first.")
