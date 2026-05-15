import streamlit as st
from agent import run_research_agent

# --- Page setup ---
st.set_page_config(
    page_title="AI Product Research Agent",
    page_icon="🔍",
    layout="wide"
)

# --- Header ---
st.title("🔍 AI Product Research Agent")
st.markdown("Type a product idea → get a full competitive brief in ~60 seconds")
st.divider()

# --- Example buttons ---
st.markdown("**💡 Try one of these examples:**")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("AI study buddy for German MBA students"):
        st.session_state.idea = "AI study buddy for German MBA students"
with col2:
    if st.button("Sustainable meal planning app in Berlin"):
        st.session_state.idea = "Sustainable meal planning app in Berlin"
with col3:
    if st.button("B2B invoicing tool for freelancers"):
        st.session_state.idea = "B2B invoicing tool for freelancers"

# --- Text input ---
idea = st.text_input(
    "Or type your own product idea:",
    value=st.session_state.get("idea", ""),
    placeholder="e.g. AI flashcard tool for medical students in Europe"
)

# --- Run button ---
if st.button("🚀 Research This Idea", type="primary", disabled=not idea):
    with st.spinner("Agent is searching the web and thinking... (30–90 seconds) ⏳"):
        try:
            result = run_research_agent(idea)
            st.success("✅ Research complete!")
            st.divider()
            st.markdown(result)
        except Exception as e:
            st.error(f"Something went wrong: {e}")

# --- Footer ---
st.divider()
st.caption("Built with LangChain · LangGraph · OpenAI GPT-4o-mini · Tavily · Streamlit")