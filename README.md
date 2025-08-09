# 📚 Agentic RAG System for Educational Support

An **LLM-powered Retrieval-Augmented Generation (RAG)** system designed to provide **accurate, context-aware answers** for educational queries.  
Built using **LangChain**, **Google Gemini Pro**, **FAISS**, and **Streamlit**, the project demonstrates how to combine **agents, memory, and tools** for intelligent document-based Q&A.

---

## 🚀 Features

- **Agentic Workflow** — Uses LangChain Agents to dynamically choose tools based on query type.
- **Context-Aware Answers** — Retrieval-Augmented Generation with FAISS for precise responses.
- **Multi-Tool Integration** — Supports document retrieval, summarization, and keyword search.
- **Streamlit UI** — Clean, interactive frontend for seamless user interaction.
- **Memory-Enabled** — Keeps conversation context for follow-up questions.

---

## 🛠️ Tech Stack

| Component         | Technology Used |
|-------------------|-----------------|
| **LLM**           | Google Gemini Pro |
| **Framework**     | LangChain |
| **Vector Store**  | FAISS |
| **Frontend**      | Streamlit |
| **Language**      | Python |
| **Libraries**     | `langchain`, `faiss-cpu`, `streamlit`, `pandas`, `dotenv`, `requests` |

---

## 📂 Project Structure

📦 agentic-rag
├── 📄 app.py # Streamlit UI and main workflow
├── 📄 agent.py # LangChain agent initialization
├── 📄 retriever.py # FAISS vector store setup and document retrieval logic
├── 📄 tools.py # Custom tool definitions
├── 📄 requirements.txt # Dependencies
├── 📄 .env.example # Environment variable template
└── 📂 data # Educational PDFs and documents

yaml
Copy
Edit

---

## ⚙️ Workflow

**1. Document Ingestion**
- Educational PDFs are loaded and split into chunks.
- Chunks are embedded using `GoogleGenerativeAIEmbeddings` and stored in FAISS.

**2. Query Handling**
- User enters a question via the Streamlit UI.
- Query is passed to the **LangChain Agent**.

**3. Tool Selection**
- Agent decides whether to:
  - Retrieve data from FAISS
  - Summarize results
  - Answer directly from LLM

**4. Contextual Answer Generation**
- Retrieved chunks are combined with the original query.
- Gemini Pro generates an accurate, context-aware answer.

**5. Response Display**
- Answer is shown in Streamlit, along with relevant sources.

---
