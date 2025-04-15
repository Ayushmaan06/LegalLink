# Legal Link : A smart Legal Ecosystem

LegalLink is a decentralized platform designed to bring transparency and efficiency to the legal ecosystem. Our solution leverages blockchain for secure, immutable recording of legal document metadata and utilizes IPFS for decentralized document storage. Additionally, the platform features a modern, user-friendly frontend built with Vue.js and a multi-modal retrieval system for both legal documents and images.

## 🚨 Problem Statement

India’s judicial system is **overburdened, slow, and often inaccessible**, leading to denial or delay of justice. Despite the core principle of "Innocent until proven guilty", **wrongful punishments and undertrial detentions** are common.

### ❗ The Ground Reality:
- **5+ crore** cases pending in Indian courts (2024)
- Average resolution time: **5–10 years**
- **80%+** of Indian prisoners are undertrials, waiting years for a verdict
- Even then, innocents can be wrongfully punished

---

## 🐢 Why is Justice So Slow?
- **Severe judge shortage** – only ~21 judges per million (vs recommended 50)
- **Case overload** – over 2,000+ cases per judge annually
- **Manual verification of documents** – slow and error-prone
- **Poor preservation of legal documents** – risk of damage or forgery

---

## 🚪 Why is Justice Inaccessible?
- **Lack of awareness** – especially in rural and underprivileged areas
- **Fear of the legal process** – people avoid filing cases
- **Complexity of legal language and process** – too hard to navigate without help

---

## ⚠️ Why Are Innocents Still Punished?
- **Document forgery** – easy to manipulate legal papers
- **Confusing legal system** – vague and inconsistent interpretations
- **No secure way to store proof/evidence**
- **Lack of community-level legal helpers** or advisors

---

## 😟 Feeling Overwhelmed?

You’re not alone.  
We know the system wasn’t built with the common person in mind.

But that’s where **we** step in.

✅ We've studied the flaws.  
✅ We've mapped out the pain points.  
✅ And now, we’re here to build a **secure, smart, and accessible legal solution** for **everyone**.

---

## 🧠 The Multimodal RAG Assistant – Master of All Trades

### 🕵️‍♂️ Detective. Advisor. Counselor.
- Combines **LLMs (LLaMA, Grok, DeepSeek r1, Gemini 2.0 Flash)** for text, image, and PDF understanding
- **Reads contracts, scans documents, decodes medical reports**, and **detects fraud**
- Built with **LangChain** + **sklearn** for reasoning, retrieval, and contextual intelligence

### 💬 Emotionally Intelligent
- Capable of understanding **emotional cues** in voice/text
- Offers **empathy-driven responses** to people in distress
- Acts like a **therapist-lite** in emotionally charged situations

### 🩺 Offers Basic Medical Guidance Too
- Can analyze medical prescriptions, reports, and suggest **first-aid or next steps**
- Not a replacement for doctors, but a **smart medical wingman**

> This is more than a legal bot—this is your **case partner**, **life navigator**, and **AI wingman** in tough times.

---

## 🔐 Decentralized Secure Storage
- All documents and proofs are stored on **IPFS** with Blockchain for:
  - **Integrity**
  - **Tamper-proof history**
  - **Decentralized, censorship-resistant storage**

---

## 🧑‍🤝‍🧑 Community of Helpers
- Verified **legal/community volunteers**
- Matchmaking via our **Recommendation System** that suggests people who’ve faced similar issues
- Peer-led support that keeps the human touch alive

---

## 📂 Smart Record Keeping
- Dashboard for:
  - Your cases
  - Connected lawyers
  - Evidence and documentation
- Encrypted, organized, and easy to access

---

## 🌐 Tech Stack

| Layer           | Tech Used                                           |
|----------------|------------------------------------------------------|
| 🧠 AI Assistant | LangChain, sklearn, Grok, LLaMA, DeepSeek r1, Gemini |
| 🧑 Backend      | Django (REST APIs)                                   |
| 🔗 Storage      | Blockchain + IPFS                                    |
| 🧑‍🎨 Frontend    | Vue.js                                               |
| 🔍 Matching Sys | Content-based + Similar-case Recommendation Engine   |

---

## 🧩 Bonus Use-Cases
- 🧠 **Legal + Medical Document Analysis**
- 🫂 **Emotional Counseling & Suggestive Support**
- 🕵️ **Fraud Detection in Contracts**
- 🧾 **Document Summarization and Insight Extraction**

---

## Getting Started

### Prerequisites

- **Backend:**
  - Python 3.8+
  - Django 5.1+
- **Frontend:**
  - Node.js and npm (or Yarn)
- **Blockchain & IPFS:**
  - MetaMask installed on your browser
  - Access to an IPFS gateway (e.g., Infura)

### Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Ayushmaan06/LegalLink.git
   cd LegalLink
   ```

2. **Backend Setup:**

   - Navigate to the backend folder:
     ```bash
     cd LegalLink
     ```
   - Configure your `.env` file and update `settings.py` as needed.
   - Run migrations and start the server:
     ```bash
     python manage.py migrate
     python manage.py runserver
     ```

3. **Frontend Setup:**

   - Navigate to the frontend folder:
     ```bash
     cd ../frontend
     ```
   - Install dependencies:
     ```bash
     npm install
     ```
   - Run the development server:
     ```bash
     npm run serve
     ```

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Vue.js](https://vuejs.org/)
- [IPFS](https://ipfs.io/)
- The Ethereum community and developers behind [ethers.js](https://docs.ethers.io/)
- All contributors and open-source libraries that have made this project possible.



