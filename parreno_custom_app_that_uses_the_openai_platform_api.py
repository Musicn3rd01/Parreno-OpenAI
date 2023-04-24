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
