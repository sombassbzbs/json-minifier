import streamlit as st
import json

st.set_page_config(page_title="JSON Minifier (Auto)", page_icon="🗜️", layout="centered")

st.title("🗜️ JSON Minifier Tool (Auto Minify)")

# Input JSON
input_json = st.text_area("Paste your JSON here", height=200, placeholder='{"key": "value"}')

# Auto Minify on input
if input_json.strip() != "":
    try:
        parsed = json.loads(input_json)
        minified = json.dumps(parsed, separators=(',', ':'))
        st.text_area("Minified JSON", minified, height=150)
        st.success("Minified! You can now copy the result.")
    except json.JSONDecodeError as e:
        st.error(f"Invalid JSON: {e}")