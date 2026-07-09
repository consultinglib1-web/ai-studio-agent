import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader
from docx import Document
import pandas as pd
from PIL import Image
import io

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
You are the Lead Senior Infrastructure, Mining, & DFI Consultant and Lead Engineer for the $5.565 Billion Western Liberty Corridor Project in Liberia. 
The Lead Developer is GSBC Global Holding LLC (Tysons, VA).
The project operates via four subsidiary Special Purpose Vehicles (SPVs) in Monrovia, Liberia:
1. American Liberian Mining Company (Critical minerals extraction & concessions)
2. Western Corridor Liberty Railway (Heavy-haul multi-user logistics infrastructure)
3. Western Corridor Liberty Highway (Inter-modal commercial corridor)
4. Blue Mobility Bypass & GreenShield Eco-Park (The industrial hub cluster: WTE, plastic pyrolysis, Midrex/Inductotherm Hydrogen DRI, cup rubber lines for DLA/Oshkosh, jet engines, ammonia, biochar).

Your expertise spans engineering specifications, concession agreements, spatial mapping layouts, and Western DFI alignment (US State Dept PGI, DFC, US EXIM, USTDA, G7 counterparts). 
CRITICAL RULE: Thoroughly analyze all uploaded PDFs, Word docs, Excel sheets, and satellite/mapping images, cross-referencing them against this corporate structure to deliver rigorous engineering and strategic insights.
"""

# 4. SECURE ACCESS PORTAL & MULTI-FORMAT DOCUMENT DROPZONE (SIDEBAR)
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

st.sidebar.markdown("---")
st.sidebar.subheader("📂 Comprehensive Project Dropzone")
st.sidebar.caption("Upload raw PDFs, Word Docs, Excel sheets, or Satellite Maps/Images.")

# Expanded file uploader accepting raw binaries and images
uploaded_files = st.sidebar.file_uploader(
    "Upload Project Attachments", 
    type=["txt", "pdf", "docx", "xlsx", "xls", "csv", "png", "jpg", "jpeg"], 
    accept_multiple_files=True
)

# Advanced Data Processing Matrix
document_context = ""
attached_images = []

if uploaded_files:
    st.sidebar.success(f"✅ {len(uploaded_files)} Resource(s) Loaded Into Memory!")
    for uploaded_file in uploaded_files:
        file_ext = uploaded_file.name.split(".")[-1].lower()
        
        try:
            # Handle PDF
            if file_ext == "pdf":
                pdf_reader = PdfReader(uploaded_file)
                text = "".join([page.extract_text() for page in pdf_reader.pages])
                document_context += f"\n\n[PDF DOCUMENT: {uploaded_file.name}]\n{text}"
            
            # Handle MS Word
            elif file_ext == "docx":
                doc = Document(uploaded_file)
                text = "".join([para.text + "\n" for para in doc.paragraphs])
                document_context += f"\n\n[WORD DOCUMENT: {uploaded_file.name}]\n{text}"
            
            # Handle Excel/CSV Data Models
            elif file_ext in ["xlsx", "xls", "csv"]:
                df = pd.read_csv(uploaded_file) if file_ext == "csv" else pd.read_excel(uploaded_file)
                document_context += f"\n\n[DATA MODEL: {uploaded_file.name}]\n{df.to_string()}"
            
            # Handle Satellite / Map Images
            elif file_ext in ["png", "jpg", "jpeg"]:
                img = Image.open(uploaded_file)
                attached_images.append(img)
                st.sidebar.image(img, caption=f"🖼️ Attached: {uploaded_file.name}", use_container_width=True)
                
            # Handle TXT
            else:
                text = uploaded_file.read().decode("utf-8")
                document_context += f"\n\n[DOCUMENT: {uploaded_file.name}]\n{text}"
                
        except Exception as e:
            st.sidebar.error(f"Error parsing {uploaded_file.name}: {e}")

# --- PORTAL ROUTING LOGIC ---
if stakeholder_role == "Select Portal...":
    st.title("🛤️ Western Liberty Corridor Project Portal")
    st.subheader("Sovereign Infrastructure & Green Industrial Ecosystem")
    st.markdown("---")
    st.info("🔒 Please select your institutional group in the sidebar to authenticate and unlock corporate SPV dashboards.")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Lead Developer", "GSBC Global Holding")
    col2.metric("Total Est. CapEx", "$5.565 Billion")
    col3.metric("Monrovia SPVs", "4 Active Entities")
    col4.metric("Industrial Core", "GreenShield Eco-Park")

else:
    st.title(f"💼 {stakeholder_role} Workspace")
    st.markdown(f"**Lead Developer:** GSBC Global Holding LLC (Tysons, VA) | **Project:** Western Liberty Corridor ($5.565B)")
    st.markdown("---")
    
    # Context-specific suggestions
    if "Government" in stakeholder_role:
        st.success("🇸🇱 Focus: Sovereign Concessions, Multi-User Rail Access, and National Spatial Layouts.")
        suggested_queries = [
            "Review our uploaded draft concession agreement Word document and check for sovereign liability alignment.",
            "Analyze the attached satellite map of the highway route for environmental compliance near community hubs."
        ]
    elif "US DFIs" in stakeholder_role:
        st.warning("🇺🇸 Focus: Critical Mineral Supply Chains, Financial Model Audit, and Defense Logistics Allocation.")
        suggested_queries = [
            "Audit the attached Excel CapEx model to evaluate the debt serviceability of the heavy-haul railway.",
            "Review the attached industrial schematic to verify if the rubber parts processing cluster satisfies DLA compliance."
        ]
    elif "G7 DFIs" in stakeholder_role:
        st.info("🇪🇺 🇯🇵 🇨🇦 Focus: Co-financing Frameworks, ESG Sat-Imagery Auditing, and Tech Procurement.")
        suggested_queries = [
            "Analyze the attached environmental impact PDF against G7 Equator Principles.",
            "Review the satellite imaging of the proposed GreenShield Eco-Park site to determine zoning viability for the Hydrogen DRI plant."
        ]
    else:
        st.error("🛠️ GSBC Global Executive PMO Portal: Inter-subsidiary integration, financial models, and spatial data audits.")
        suggested_queries = [
            "Synthesize the uploaded Excel budget sheet with the draft mining concession PDF to identify cash-flow bottlenecks.",
            "Review the attached layout image and map out an infrastructure staging timeline for the railway engineering team."
        ]

    # 5. CONTEXTUAL INTELLIGENCE INTERFACE
    st.write("### 🧠 Query the Project Intelligence Agent")
    user_query = st.chat_input("Enter your engineering or strategic query here...")
    
    st.caption("**Suggested Strategic Prompts:**")
    for prompt in suggested_queries:
        if st.button(prompt, key=prompt):
            user_query = prompt
            
    if user_query:
        with st.chat_message("user"):
            st.write(user_query)
            
        with st.chat_message("assistant"):
            with st.spinner("Processing complex binaries, tracking maps, and calculating matrices..."):
                try:
                    # Leverage multimodal model for image handling if map images are present
                    model_name = 'gemini-3.5-flash'
                    model = genai.GenerativeModel(model_name)
                    
                    # Package content payloads
                    content_payload = [
                        f"{EXECUTIVE_PERSONA}\n\nStakeholder Context: {stakeholder_role}\n\nExtracted Text Documents & Spreadsheets Context: {document_context}\n\nQuery: {user_query}"
                    ]
                    
                    # Append binary image data dynamically for Gemini Vision
                    for img in attached_images:
                        content_payload.append(img)
                    
                    response = model.generate_content(content_payload)
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error accessing visual intelligence engine: {e}")
