# 🧠 Consumer Complaint QnA System

This project builds a Retrieval-Augmented Generation (RAG) pipeline to answer consumer complaint questions using a subset of U.S. financial service complaints.

## 🔧 Tech Stack

- 🧠 LLM: google/flan-t5-base (Hugging Face Transformers)
- 🔍 Vector Search: FAISS + MiniLM
- 🔄 RAG Framework: LangChain
- 📄 Dataset: Subset of 500 narratives from [Kaggle – Consumer Complaints](https://www.kaggle.com/datasets/sherrytp/consumer-complaints)

## 🚀 How to Run

```bash
pip install -r requirements.txt
python app.py

