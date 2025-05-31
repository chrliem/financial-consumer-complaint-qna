import streamlit as st
from qa_chain import build_qa_chain

st.set_page_config(page_title="Financial Complaint QnA", layout="wide")

st.title("💬 Financial Consumer Complaint QnA")
st.write("Ask a question about financial consumer complaints from the CFPB dataset.")

@st.cache_resource
def load_chain():
    return build_qa_chain()

qa_chain = load_chain()

query = st.text_input("Enter your question:", "")

if query:
    with st.spinner("Generating answer..."):
        result = qa_chain.invoke({"query": query})
        st.subheader("🧠 Answer")
        st.write(result['result'])

        st.subheader("📚 Source Documents")
        for doc in result['source_documents']:
            st.markdown(f"- **{doc.metadata['source']}**")
