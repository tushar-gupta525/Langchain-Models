# LangChain Models Repository

This repository demonstrates how to build and run **LLMs, Chatbots, and Embedding Models**
using **LangChain** with:

- **OpenAI**
- **Google Gemini**
- **Hugging Face (Free models)**

The models are used in two ways:
1. **API-based usage** (using API keys)
2. **Local usage** (downloading models and running them on your system)

---

## 📌 What You Will Find in This Repository

This repo covers practical implementations of:

### 🔹 Large Language Models (LLMs)
Models capable of understanding and generating human-like text.

### 🔹 Chatbots
Conversational AI models that can:
- Answer questions
- Hold conversations
- Generate stories and explanations

### 🔹 Embedding Models
Models that convert text into numerical vectors, useful for:
- Semantic search
- Similarity matching
- Retrieval-Augmented Generation (RAG)

### 🔹 NLP Tasks Covered
- **Text Generation**
- **Text Summarization**

---


---

## ⚙️ Environment Setup

We strongly recommend using a **virtual environment** to keep dependencies isolated.

### 1️⃣ Create a virtual environment named `jarvis`

python -m venv jarvis

### Activate the virtual environment:

jarvis\Scripts\activate

Once activated, you should see:

(jarvis)

in your terminal.

**Install required dependencies**
pip install -r requirements.txt

### 2. API Keys Setup

Some models require API keys.

**Create a .env file in the root directory**

Add your keys:

OPENAI_API_KEY=your_openai_key_here
GOOGLE_API_KEY=your_gemini_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here

### 3. How to Run the Code
after activating environment run bellow given code
python ChatModels/chatmodel_google_api_1.py

