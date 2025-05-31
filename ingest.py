import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document

def load_and_index(path="data/subset_complaints.csv"):
    df = pd.read_csv(path)
    df = df[df['Consumer complaint narrative'].notnull()].reset_index(drop=True)
    
    docs = []
    for _, row in df.iterrows():
        content = row['Consumer complaint narrative']
        metadata = f"Product: {row['Product']} | Issue: {row['Issue']} | Company: {row['Company']}"
        docs.append(Document(page_content=content, metadata={"source": metadata}))
    
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore
