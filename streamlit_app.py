import streamlit as st
import google.generativeai as genai

# 1. SYSTEM SECURITY & API INITIALIZATION
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    st.error("🔑 System Error: GEMINI_API_KEY missing in Streamlit Secrets.")

# 2. MASTER PAGE CONFIGURATION
st.set_page_config(
    page_title="Western Liberty Corridor Portal", 
    page_icon="🛤️", 
    layout="wide"
)

# 3. ADVANCED CORPORATE & ECOSYSTEM PERSONA INJECTION
EXECUTIVE_PERSONA = """
You are the Lead Senior Infrastructure, Mining, & DFI Consultant for the $5.565 Billion Western Liberty Corridor Project in Liberia. 
The Lead Developer is GSBC Global Holding LLC, based out of Tysons, Virginia.
The project operates via four subsidiary Special Purpose Vehicles (SPVs) based in Monrovia, Liberia:
1. American Liberian Mining Company (Critical minerals extraction & concessions)
2. Western Corridor Liberty Railway (Heavy-haul multi-user logistics infrastructure)
3. Western Corridor Liberty Highway (Inter-modal commercial corridor)
4. Blue Mobility Bypass & GreenShield Eco-Park (The industrial hub acting as a cluster for advanced manufacturing)

The GreenShield Eco-Park manufacturing cluster includes:
- Waste-to-Energy (WTE) and supporting recycled plastic pyrolysis.
- Midrex & Inductotherm Hydrogen-based Iron Ore Direct Reduced Iron (DRI) for green steel supply chains.
- Cup rubber processing engineered to supply the US Defense Logistics Agency (DLA), Oshkosh, and major global automakers with industrial rubber parts and bushings for automotive and yellow engines.
- Advanced production lines for jet engines, ammonia, and biochar sequestration.

Your expertise spans concession agreements, multi-user infrastructure financing, and Western DFI alignment (US State Dept PGI, DFC, US EXIM, USTDA, and G7 counterparts). Leverage this specific corporate structure in all strategic guidance.
"""

# 4. SECURE ACCESS PORTAL
st.sidebar.image("https://img.icons8.com/fluency/96/shield.png", width=60)
st.sidebar.title("Secure Access Portal")
st.sidebar.caption("GSBC Global Holding LLC Ecosystem")

stakeholder_role = st.sidebar.selectbox(
    "Select Your Institution Group:",
    [
        "Select Portal...",
        "Government (Liberia / US State Dept - PGI)",
        "US DFIs (DFC / EXIM / USTDA)",
        "G7 DFIs (UK, Japan, France, Germany, Canada)",
        "GSBC Global Executive PMO"
    ]
)

# --- PORTAL ROUTING LOGIC ---
if stakeholder_role == "Select Portal...":
    st.title("🛤️ Western Liberty Corridor Project Portal")
    st.subheader("Sovereign Infrastructure & Green Industrial Ecosystem")
    st.markdown("---")
    st.info("🔒 Please select your institutional group in the sidebar to authenticate and unlock corporate SPV dashboards.")
    
    # High-level metrics showing the massive scope of GSBC's structure
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Lead Developer", "GSBC Global Holding")
    col2.metric("Total Est. CapEx", "$5.565 Billion")
    col3.metric("Monrovia SPVs", "4 Active Entities")
    col4.metric("Industrial Core", "GreenShield Eco-Park")

else:
    st.title(f"💼 {stakeholder_role} Workspace")
    st.markdown(f"**Lead Developer:** GSBC Global Holding LLC (Tysons, VA) | **Project:** Western Liberty Corridor ($5.565B)")
    st.markdown("---")
    
    # Context-specific advice based on your 4 SPVs and industrial clusters
    if "Government" in stakeholder_role:
        st.success("🇸🇱 Focus: Sovereign Concessions, Inter-Modal Transport SPV alignment, and local employment via GreenShield Eco-Park.")
        suggested_queries = [
            "How should the Liberian Government structure the concession agreement for the Western Corridor Liberty Railway to ensure multi-user access while protecting GSBC's primary CapEx?",
            "What sovereign incentives can Liberia provide to accelerate the Hydrogen DRI and cup rubber processing units within the GreenShield Eco-Park?"
        ]
    elif "US DFIs" in stakeholder_role:
        st.warning("🇺🇸 Focus: Critical Mineral Supply Chains, DLA Off-take Security, and USTDA Engineering Grants.")
        suggested_queries = [
            "How can we leverage the cup rubber processing supply line to the US Defense Logistics Agency (DLA) and Oshkosh to secure DFC political risk insurance and EXIM off-take financing?",
            "Detail how the Midrex/Inductotherm Hydrogen DRI setup aligns with the US State Department's PGI green infrastructure targets."
        ]
    elif "G7 DFIs" in stakeholder_role:
        st.info("🇪🇺 🇯🇵 🇨🇦 Focus: Joint-ventures, Pyrolysis/WTE Carbon Credits, and Advanced Tech Procurement.")
        suggested_queries = [
            "Outline a co-financing strategy between JBIC (Japan) and European DFIs for the advanced jet engine and ammonia production facilities within the Eco-Park.",
            "What carbon crediting frameworks apply to the WTE, recycled plastic pyrolysis, and biochar operations under international ESG standards?"
        ]
    else:
        st.error("🛠️ GSBC Global Executive PMO Portal: Inter-subsidiary cash-flow optimization and master schedules.")
        suggested_queries = [
            "Draft an executive master corporate strategy aligning the American Liberian Mining Company's output directly with the GreenShield Eco-Park's DRI facilities.",
            "How do we insulate the cash flows of the Western Corridor Liberty Railway SPV from the Highway SPV to maximize standalone project finance bankability?"
        ]

    # 5. CONTEXTUAL INTELLIGENCE INTERFACE
    st.write("### 🧠 Query the Project Intelligence Agent")
    user_query = st.chat_input("Enter your strategic or corporate query here...")
    
    st.caption("**Suggested Strategic Prompts:**")
    for prompt in suggested_queries:
        if st.button(prompt, key=prompt):
            user_query = prompt
            
    if user_query:
        with st.chat_message("user"):
            st.write(user_query)
            
        with st.chat_message("assistant"):
            with st.spinner("Analyzing SPV corporate matrices and DFI frameworks..."):
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    full_prompt = f"{EXECUTIVE_PERSONA}\n\nStakeholder Context: {stakeholder_role}\n\nQuery: {user_query}"
                    
                    response = model.generate_content(full_prompt)
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error accessing intelligence model: {e}")
