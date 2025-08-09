import os
import streamlit as st
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.agents import Tool, initialize_agent

import asyncio
asyncio.set_event_loop(asyncio.new_event_loop())

# 1. Setup API key and working directory
os.environ["GOOGLE_API_KEY"] = "AIzaSyDUH7JAHV6yt9KOd5vEBy1Im0bp7cnt9C8"
os.chdir("d:/projects/tutor")

# 2. Subject and PDF files
pdf_files = {
    "CNS": "CNS.pdf",
    "DBMS": "DBMS.pdf",
    "SPOS": "SPOS.pdf",
    "TOC": "TOC.pdf"
}
subjects = list(pdf_files.keys())

# 3. Embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

aa = """
# Create vector DB for each subject
for subject, path in pdf_files.items():
    loader = PyMuPDFLoader(path)
    docs = loader.load()
    chunks = splitter.split_documents(docs)
    vectorstore = FAISS.from_documents(chunks, embedding=embeddings)
    vectorstore.save_local(f"{subject}_db")
"""

# 4. Load FAISS vector stores

vectorstores = {
    subject: FAISS.load_local(f"{subject}_db", embeddings, allow_dangerous_deserialization=True)
    for subject in subjects
}

# 5. Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)

# 6. Create subject-specific tools
tools = []
for subject, vs in vectorstores.items():
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vs.as_retriever())
    tools.append(
        Tool(
            name=f"{subject}Tool",
            func=qa_chain.run,
            description=f"Use this tool to answer questions related to {subject}."
        )
    )

# 7. Create agent using initialize_agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# 8. Streamlit UI
st.set_page_config(page_title="TutorBot", page_icon="📘")
st.title("📘 RAG Based Tutor chatbot")

query = st.text_input("🧠 Ask a technical question:")
if query:
    with st.spinner("Thinking..."):
        response = agent.invoke(query)
        st.markdown("### 📘 Answer")
        st.write(response)
