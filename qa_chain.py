from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from ingest import load_and_index

def build_qa_chain():
    pipe = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_new_tokens=512
    )
    llm = HuggingFacePipeline(pipeline=pipe)
    vectorstore = load_and_index()
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=True
    )
    return chain
