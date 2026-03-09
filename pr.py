import streamlit as st
from groq import Groq

# page title
st.title("CodeRefine - AI Code Review Engine")

# API client
client = Groq(api_key="YOUR_API_KEY")

# code input
code = st.text_area("Paste your code here", height=300)

# button
if st.button("Review Code"):

    if code.strip() == "":
        st.warning("Please enter code first")
    else:

        prompt = f"""
        Review the following code.

        1. Find bugs
        2. Suggest optimizations
        3. Provide improved code

        Code:
        {code}
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        result = response.choices[0].message.content

        st.subheader("AI Review Result")

        st.write(result)