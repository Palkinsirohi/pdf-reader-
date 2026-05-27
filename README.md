# Local RAG Application using Python, LangChain, Ollama, ChromaDB, and HuggingFace

## Project Overview

This project is a Local RAG (Retrieval-Augmented Generation) Application that allows users to ask questions from a PDF document using a locally running AI model.

The application reads PDF files, converts the text into embeddings, stores them inside a vector database, retrieves relevant information based on user questions, and generates accurate answers using a Large Language Model (LLM).

The entire system works locally without requiring OpenAI APIs or internet-based AI services.

---

# What is RAG?

RAG stands for:

Retrieval-Augmented Generation

RAG combines:

1. Information Retrieval
2. AI Text Generation

Instead of depending only on the knowledge stored inside an AI model, RAG first retrieves relevant information from external documents and then uses that information to generate better answers.

---

# Why Use RAG?

Traditional AI models may:
- Hallucinate
- Give incorrect answers
- Lack updated knowledge
- Not know private company data

RAG solves this by:
- Retrieving actual document data
- Reducing hallucinations
- Improving accuracy
- Supporting custom knowledge bases

---

# Project Workflow

```text
User Question
      ↓
Flask Web Application
      ↓
LangChain RAG Pipeline
      ↓
ChromaDB Vector Search
      ↓
Relevant PDF Chunks Retrieved
      ↓
Ollama Llama3 Generates Answer
      ↓
Final Response Displayed
```

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| LangChain | AI orchestration framework |
| Ollama | Run local LLM |
| Llama3 | Large Language Model |
| HuggingFace Embeddings | Convert text into vectors |
| ChromaDB | Vector database |
| PyPDFLoader | Read PDF files |
| HTML/CSS | User Interface |

---

# Concepts Explained

---

# 1. Python

Python is the main programming language used for this project.

Why Python?
- Easy syntax
- Massive AI ecosystem
- Best support for machine learning
- Large community support

Used For:
- Backend logic
- AI pipeline
- Data processing
- Flask application

Official Website:
https://www.python.org/

---

# 2. Flask

Flask is a lightweight Python web framework.

Purpose:
- Creates backend server
- Handles routes
- Receives user questions
- Sends AI responses to frontend

Example:

```python
@app.route("/")
def home():
    return "Hello"
```

Why Flask?
- Beginner friendly
- Lightweight
- Easy integration with AI apps

Official Website:
https://flask.palletsprojects.com/

---

# 3. LangChain

LangChain is a framework used for building applications powered by Large Language Models (LLMs).

It connects:
- LLMs
- Vector databases
- Documents
- APIs
- Memory systems

Purpose in this project:
- Build RAG pipeline
- Connect PDF → Embeddings → ChromaDB → LLM

Main Components Used:
- Document Loaders
- Text Splitters
- Embeddings
- Vector Stores
- RetrievalQA

Official Website:
https://www.langchain.com/

---

# 4. Ollama

Ollama allows you to run Large Language Models locally on your computer.

Purpose:
- Run Llama3 locally
- No OpenAI API needed
- Offline AI execution

Advantages:
- Free
- Private
- Offline
- No API cost

Command to run model:

```bash
ollama run llama3
```

Official Website:
https://ollama.com/

---

# 5. Llama3

Llama3 is a Large Language Model (LLM).

It is used for:
- Understanding questions
- Generating answers
- Language reasoning

In this project:
- Llama3 receives retrieved PDF chunks
- Generates final answer

Why Local LLM?
- Better privacy
- No cloud dependency
- No API billing

---

# 6. HuggingFace Embeddings

Embeddings convert text into numerical vectors.

Example:
"Artificial Intelligence" → [0.234, 0.991, ...]

These vectors help AI systems understand semantic meaning.

Used Model:
sentence-transformers/all-MiniLM-L6-v2

Purpose:
- Convert PDF chunks into vectors
- Convert user questions into vectors
- Perform semantic similarity search

Why Embeddings?
Because AI cannot search raw text efficiently.

Official Website:
https://huggingface.co/

---

# 7. ChromaDB

ChromaDB is a vector database.

Purpose:
- Store embeddings
- Search similar vectors
- Retrieve relevant chunks

Example:
User asks:
"What is supervised learning?"

ChromaDB retrieves chunks related to supervised learning.

Advantages:
- Lightweight
- Fast
- Local storage
- Easy integration

Official Website:
https://www.trychroma.com/

---

# 8. PyPDFLoader

PyPDFLoader reads PDF documents.

Purpose:
- Extract text from PDF
- Convert PDF into readable documents

Example:

```python
loader = PyPDFLoader("sample.pdf")
documents = loader.load()
```

---

# 9. Text Splitting

Large documents are split into smaller chunks.

Why?
LLMs cannot process huge PDFs directly.

Example:

```python
RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
```

Chunk Overlap:
Helps preserve context between chunks.

---

# 10. RetrievalQA

RetrievalQA is a LangChain chain.

Purpose:
1. Retrieve relevant chunks
2. Send chunks to LLM
3. Generate answer

---

# System Requirements

Minimum:
- 8 GB RAM
- Intel i5 or Ryzen 5
- Python 3.10+
- Internet for first-time model downloads

Recommended:
- 16 GB RAM
- SSD storage
- GPU (optional)

---

# Project Folder Structure

```text
local-rag-app/
│
├── app.py
├── rag_pipeline.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── pdfs/
│   └── sample.pdf
│
└── chroma_db/
```

---

# Step-by-Step Setup Guide

---

# Step 1 — Install Python

Download:
https://www.python.org/downloads/

IMPORTANT:
During installation select:

✅ Add Python to PATH

Verify installation:

```bash
python --version
```

---

# Step 2 — Install VS Code

Download:
https://code.visualstudio.com/

Install Extensions:
- Python
- Pylance

---

# Step 3 — Install Ollama

Download:
https://ollama.com/

After installation run:

```bash
ollama run llama3
```

This downloads Llama3 locally.

---

# Step 4 — Create Project Folder

```bash
mkdir local-rag-app
cd local-rag-app
```

---

# Step 5 — Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# What is Virtual Environment?

A virtual environment isolates project dependencies.

Benefits:
- Avoid package conflicts
- Cleaner development
- Project-specific libraries

---

# Step 6 — Install Dependencies

```bash
pip install flask langchain langchain-community langchain-core chromadb sentence-transformers pypdf ollama langchain-huggingface langchain-ollama
```

---

# Step 7 — Create requirements.txt

```txt
flask
langchain
langchain-community
langchain-core
chromadb
sentence-transformers
pypdf
ollama
langchain-huggingface
langchain-ollama
```

Install later using:

```bash
pip install -r requirements.txt
```

---

# Step 8 — Add PDF File

Create folder:

```text
pdfs/
```

Add:

```text
sample.pdf
```

---

# Step 9 — Create RAG Pipeline

Create file:

```text
rag_pipeline.py
```

Purpose:
- Load PDF
- Split text
- Create embeddings
- Store vectors
- Create retriever
- Create QA chain

---

# Step 10 — Create Flask App

Create:

```text
app.py
```

Purpose:
- Handle frontend requests
- Receive user questions
- Return AI answers

---

# Step 11 — Create Frontend

Create:
- HTML
- CSS

Purpose:
- User interaction
- Display answers

---

# Step 12 — Run Ollama

```bash
ollama run llama3
```

Keep terminal running.

---

# Step 13 — Run Flask App

```bash
python app.py
```

---

# Step 14 — Open Browser

```text
http://127.0.0.1:5000
```

---

# Example Questions

- What is AI?
- Explain machine learning.
- What is RAG?
- What is ChromaDB?
- Explain LangChain.
- What is reinforcement learning?

---

# How Semantic Search Works

Traditional Search:
Matches exact keywords.

Semantic Search:
Matches meaning.

Example:
Question:
"What is artificial intelligence?"

It can still retrieve:
"AI is a branch of computer science..."

because embeddings understand meaning.

---

# Advantages of This Project

- Runs locally
- No OpenAI API cost
- Beginner friendly
- Good AI portfolio project
- Real-world GenAI architecture
- Expandable system

---

# Future Improvements

## Beginner Level
- PDF upload
- Better UI
- Chat history

## Intermediate Level
- Multiple PDFs
- Source citations
- Streaming responses

## Advanced Level
- Docker deployment
- Authentication
- Voice assistant
- Cloud deployment

---

# Common Errors and Fixes

---

## Error:
ModuleNotFoundError

Fix:

```bash
pip install -r requirements.txt
```

---

## Error:
Ollama not running

Fix:

```bash
ollama run llama3
```

---

## Error:
Invalid PDF structure

Reason:
PDF is corrupted or fake PDF.

Fix:
Export proper PDF from Word or Google Docs.

---

# Learning Outcomes

After completing this project you will understand:
- RAG architecture
- LangChain basics
- Vector databases
- Embeddings
- Local LLM execution
- AI web applications
- Flask backend
- Semantic search

---

# Conclusion

This project demonstrates how modern AI systems combine:
- Document retrieval
- Vector databases
- Embeddings
- Large Language Models

to build intelligent applications capable of answering questions from private documents.

It is an excellent beginner-to-intermediate Generative AI project for:
- Final Year Projects
- AI Portfolios
- Internship Preparation
- LangChain Learning
- Local AI Systems

---
