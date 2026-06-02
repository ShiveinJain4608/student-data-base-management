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

uploaded_file = st.sidebar.file_uploader(
    "Upload Python File",
    type=["py"]
)

code = ""

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")
    functions = 0
imports = 0
lines = 0

if code:
    lines = len(code.splitlines())

    try:
        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):
                functions += 1

            elif isinstance(node, ast.Import):
                imports += len(node.names)

            elif isinstance(node, ast.ImportFrom):
                imports += 1

    except:
        pass
    
    
