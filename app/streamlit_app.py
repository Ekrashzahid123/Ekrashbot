import sys
import os 


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

import streamlit as st
from rag.rag_chain import load_rag_chain


st.set_page_config(
    page_title="EkrashBot",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for nicer interface
st.markdown(
    """
    <style>
    .stTextInput>div>div>input {
        height: 45px;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        height: 45px;
        font-size: 16px;
        border-radius: 8px;
    }
    .stAlert {
        font-size: 16px;
        border-radius: 10px;
        padding: 15px;
    }
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #4CAF50;
    }
    .subtitle {
        font-size: 22px;
        color: #555;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown('<h1 class="title">🤖 EkrashBot</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your personal assistant for Ekrash Zahid\'s portfolio!</p>', unsafe_allow_html=True)
st.markdown(
    "Ask anything about **Ekrash Zahid's experience, projects, or skills**. "
    "I can provide detailed answers, links, and summaries!"
)

# Load QA chain
qa = load_rag_chain()

# Input section with columns for a cleaner look
col1, col2 = st.columns([4,1])
with col1:
    query = st.text_input("💬 Ask a question:")

with col2:
    if st.button("Ask"):
        query = query  # Trigger the query run

# Display answer
if query:
    with st.spinner("EkrashbotThinking... 🤔"):
        try:
            answer = qa.run(query)
            st.success(answer)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

# Footer
st.markdown("---")
st.markdown(
    "Created with ❤️ by **Ekrash Zahid** | "
    "[GitHub](https://github.com/Ekrashzahid123?tab=repositories) | "
    "[LinkedIn](https://www.linkedin.com/in/ekrash-zahid-51bb76256/)"
)
