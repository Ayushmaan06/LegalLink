import streamlit as st

# Set up Streamlit page
st.set_page_config(
    page_title="LegalLink",
    page_icon=":scales:",  # you may change the icon as desired
    initial_sidebar_state="expanded",
    layout="wide",
    menu_items={
        'Get Help': 'https://www.yourlegalink.com/help',
        'Report a bug': "https://www.yourlegalink.com/bug",
        'About': "# LegalLink\nYour AI‑Powered Legal Assistant offering insights and analysis for your legal documents."
    }
)

# Title of the web app
st.title("LegalLink - Your AI‑Powered Legal Assistant")

# Explanation for Users
st.write("""
**LegalLink** is an AI‑powered assistant designed to help you navigate and understand legal documents and texts. Whether you're dealing with contracts, case files, or regulatory documents, LegalLink can help extract key legal points, summarise content, and answer your legal queries.

### Features:
1. **Legal Document Analysis**:  
   Upload your legal documents (PDFs, Word files, etc.), and LegalLink will extract and summarise the key legal information to help you gain insights quickly.

2. **Legal Question Answering**:  
   Ask questions about legal texts or documents, and receive context-aware answers generated through advanced AI retrieval-augmented techniques.

### How It Works:
- **Document Analysis**: Upload a document, and the assistant analyses it, highlighting key sections, obligations, and important clauses.
- **Legal Q&A**: Once processed, you can ask detailed questions regarding the document or general legal inquiries. The assistant uses its analysis to provide accurate, helpful responses.

**Disclaimer**: LegalLink is intended for informational purposes only and is not a substitute for professional legal advice. Always consult a qualified solicitor for formal legal guidance.

Get started by uploading your document or posting your legal question below.
""")