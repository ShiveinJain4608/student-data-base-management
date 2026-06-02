import streamlit as st

st.set_page_config(
    page_title="Python Code Explainer",
    page_icon="🐍",
    layout="wide"
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select a Page",
 [
    "🏠 Home",
    "💻 Source Code",
    "📊 Code Analysis",
    "📄 Code Summary",
    "🔄 Program Flow",
    "▶️ Run Game"
]
)
