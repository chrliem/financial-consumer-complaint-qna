from qa_chain import build_qa_chain

qa_chain = build_qa_chain()

queries = [
    "What are the most common issues reported about credit cards?",
    "Which companies receive the most complaints?",
    "What problems do consumers report with auto loans?",
    "Tell me about recurring problems in mortgage services."
]

for query in queries:
    print(f"❓ Query: {query}")
    result = qa_chain.invoke({"query": query})
    print("🧠 Answer:\n", result['result'])
    print("📚 Source documents:")
    for doc in result['source_documents']:
        print("-", doc.metadata['source'][:200])
    print("\n" + "=" * 80 + "\n")
