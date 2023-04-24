# Commented out IPython magic to ensure Python compatibility.
# %env OPEN_AI_KEY=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

import streamlit as st
import openai

st.title("Text to Color Generator")

openai.api_key = "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"

def text_to_color(description):
    prompt = f"Convert the following text description to a color: {description}\nColor:"
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completions.choices[0].text.strip()
    return response

description = st.text_input("Enter a text description:")
if st.button("Generate Color"):
    color = text_to_color(description)
    st.write(f"The color for '{description}' is {color}.")
