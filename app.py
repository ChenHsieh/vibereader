import streamlit as st
from tools.news_fetcher import fetch_guardian_headlines
from tools.persona_generator import simulate_persona
from openai import OpenAI
import time
import os
import pandas as pd

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
if not client.api_key:
    raise ValueError("Missing OpenAI API key. Set OPENAI_API_KEY in your environment.")

def generate_poetic_response(headline: str, persona: dict) -> str:
    persona_summary = (
        f"A {persona['role']} currently in a state of {persona['mood']}, "
        f"driven by {persona['motivation']}, currently facing {persona['crisis']}, "
        f"who sees the world as '{persona['worldview']}', and holds a {persona['moral_alignment']} philosophy. "
        f"Attachment style: {persona['attachment_style']}."
    )

    system_prompt = "You are a fictional character reacting to news with poetic expression."
    user_prompt = (
        f"{persona_summary}\n\n"
        f"Given the headline:\n\"{headline}\"\n\n"
        f"How do you feel about it emotionally? Then write a short, surreal poem (3–5 lines) in your voice."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"(error: {e})"

st.title("VibeReader: Emotional News Persona Generator")

st.markdown(
    "Welcome to **VibeReader** — where current events meet imagined minds.\n\n"
    "Choose a headline below, and a unique fictional persona will react with a short surreal poem.\n"
    "Click 🔄 *Refresh Persona* to explore how different characters interpret the same news."
)

headlines = fetch_guardian_headlines()
st.markdown("### 📰 Select a Headline")
selected = st.radio("Pick a headline to process:", headlines)

if selected:
    st.markdown(f"**Selected Headline**: {selected}")

    persona = simulate_persona()
    st.markdown("### 👤 Generated Persona")
    if st.button("🔄 Refresh Persona"):
        persona = simulate_persona()
    persona_df = pd.DataFrame(
        [[k.replace('_', ' ').title(), v] for k, v in persona.items()],
        columns=["Attribute", "Value"]
    )
    st.table(persona_df)

    st.markdown("### ✍️ Poetic Responses")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### With Persona")
        poem = generate_poetic_response(selected, persona)
        st.markdown(poem)

    with col2:
        st.markdown("#### Baseline (No Persona)")
        baseline_prompt = (
            f"The headline is:\n\"{selected}\"\n\n"
            "React to this news headline with a short, surreal poem (3–5 lines). "
            "Do not assume any fictional persona or internal backstory."
        )
        try:
            baseline_response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a poetic AI responding to news."},
                    {"role": "user", "content": baseline_prompt}
                ]
            )
            st.markdown(baseline_response.choices[0].message.content)
        except Exception as e:
            st.markdown(f"(error: {e})")