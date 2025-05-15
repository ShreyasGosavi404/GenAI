import os
import streamlit as st
import time
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Load environment variables (e.g., OpenAI API key)
load_dotenv()

st.title("RockyBot: News Research Tool 📈")
st.sidebar.title("News Article URLs")

# Collect URLs
urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
main_placeholder = st.empty()

# Initialize OpenAI Chat model (gpt-3.5-turbo)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)

# Directory to persist FAISS vector store
persist_dir = "faiss_index"

# Process and embed news articles
if process_url_clicked:
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading... Started... ✅")
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitting... Started... ✅")
    docs = text_splitter.split_documents(data)

    embeddings = OpenAIEmbeddings()
    main_placeholder.text("Building Embedding Vectors... ✅")

    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local(persist_dir)
    main_placeholder.text("Embeddings Successfully Stored in FAISS! ✅")
    time.sleep(1)

# Question answering using stored FAISS index
query = main_placeholder.text_input("Question: ")
if query:
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local(persist_dir, embeddings)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=True
    )

    result = qa_chain({"query": query})

    st.header("Answer")
    st.write(result["result"])

    source_docs = result.get("source_documents", [])
    if source_docs:
        st.subheader("Sources:")
        for doc in source_docs:
            st.write(doc.metadata.get("source", "[Unknown Source]"))
