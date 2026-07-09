import streamlit as st
import google.generativeai as genai
import os

# 1. SYSTEM SECURITY & API INITIALIZATION
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    st.error("🔑 System Error: GEMINI_API_KEY missing in Streamlit Secrets.")

# Set up the active production model
model_name = "gemini-3.5-flash"  # Correct production-active model string
model = genai.GenerativeModel(model_name)

# 2. APP UI CONFIGURATION
st.set_page_config(page_title="GSBC Project Portal", layout="wide")

st.title("💼 GSBC Global Executive PMO Workspace")
st.caption("Lead Developer: GSBC Global Holding LLC (Tysons, VA) | Project: Western Liberty Corridor ($5.565B)")

st.markdown("---")
st.subheader("🛠️ GSBC Global Executive PMO Portal")
st.write("Inter-subsidiary integration, financial models, and spatial data audits.")

# 3. SELECT INSTITUTION (All original profiles restored)
institution = st.sidebar.selectbox(
    "Select Your Institution Group:",
    [
        "Select Profile", 
        "GSBC Global Executive PMO", 
        "Government of Liberia Representative",
        "US Government / USTDA",
        "Development Finance Institutions (DFIs)"
    ]
)

# 4. WORKSPACE ROUTING LOGIC
if institution == "GSBC Global Executive PMO":
    st.markdown("### 🧠 Query the Project Intelligence Agent")
    
    # Input prompt from user
    user_prompt = st.text_area("Enter your prompt or strategic directive below:", height=150)
    
    if st.button("Run Intelligence Engine"):
        if user_prompt:
            # Build full contextual framework prompt
            full_prompt = f"Context: Western Liberty Corridor ($5.565B Project Framework). {user_prompt}"
            
            # Run the loading spinner while processing the API request
            with st.spinner("Processing complex binaries, tracking maps, and calculating matrices..."):
                try:
                    # Execute network request to Google AI
                    response = model.generate_content(full_prompt)
                    
                    st.markdown("### 📄 Generated Strategic Framework Output")
                    if response and response.text:
                        st.markdown(response.text)
                    else:
                        st.warning("⚠️ The model returned an empty response.")
                        
                except Exception as e:
                    st.error(f"Error accessing intelligence model: {e}")
        else:
            st.warning("Please enter a prompt before running the engine.")
            
elif institution != "Select Profile":
    # Fallback message for other institutional views
    st.info(f"Welcome to the {institution} portal. Select 'GSBC Global Executive PMO' to open the query console.")
else:
    st.info("Please select an institutional group from the sidebar to activate the workspace.")
