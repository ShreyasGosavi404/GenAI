# RockyBot: AI-Powered News Research Assistant

🧠 GenAI-powered news research tool using LangChain, OpenAI, FAISS, and Streamlit to extract insights from financial articles with LLM-based Q&amp;A.

RockyBot is an end-to-end Generative AI (GenAI) application designed to automate and enhance financial news analysis using Large Language Models (LLMs). It empowers analysts and researchers to extract meaningful insights from multiple news articles using tools like LangChain, OpenAI GPT-3.5, FAISS, and Streamlit.

![image](https://github.com/user-attachments/assets/469e738e-3916-4c2d-88b1-e7151e5788f7)

# 📌 Use Case
In financial sectors like equity research and mutual funds, analysts must comb through countless news sources to stay updated. RockyBot automates this by letting users input article URLs, semantically indexing them, and then querying them like a chatbot.


## ⚙️ Features

- 🔗 Accepts multiple financial article URLs (e.g., from MoneyControl, Economic Times)
- 🧠 Uses OpenAI's GPT-3.5 for intelligent, context-aware answers
- 🧱 Utilizes FAISS for efficient vector-based semantic search
- 📚 Returns answers with cited sources for transparency
- 💾 Saves vector index locally for faster reuse
- 🖥 Built with Streamlit for an interactive and clean UI
  
# 🧠 System Architecture
User Inputs URLs → Document Loading (LangChain) → Text Splitting → OpenAI Embeddings → FAISS Vector Store → RetrievalQA (LangChain) + GPT-3.5 → Answer with Sources

# 🖥️ How to Use
- Paste up to 3 news article URLs in the sidebar.

- Click “Process URLs” to:

- Fetch and clean the content

- Split the content into semantic chunks

- Convert chunks into vector embeddings

- Save them in a FAISS vector database

- Enter your question in the main input box.

- RockyBot retrieves relevant chunks and uses GPT-3.5 to answer.

- Answer and source URLs are displayed clearly.

# Usage/Examples
1. Run the Streamlit app by executing:
streamlit run main.py

2. The web app will open in your browser.

- On the sidebar, you can input URLs directly.

- Initiate the data loading and processing by clicking "Process URLs."

- Observe the system as it performs text splitting, generates embedding vectors, and efficiently indexes them using FAISS.

- The embeddings will be stored and indexed using FAISS, enhancing retrieval speed.

- The FAISS index will be saved in a local file path in pickle format for future use.

- One can now ask a question and get the answer based on those news articles

- In video tutorial, we used following news articles
https://www.moneycontrol.com/news/business/tata-motors-mahindra-gain-certificates-for-production-linked-payouts-11281691.html
https://www.moneycontrol.com/news/business/tata-motors-launches-punch-icng-price-starts-at-rs-7-1-lakh-11098751.html
https://www.moneycontrol.com/news/business/stocks/buy-tata-motors-target-of-rs-743-kr-choksey-11080811.html

# 🙌 Acknowledgements
Inspired by real-world equity research workflows and GenAI applications in financial services.
Thanks to LangChain, OpenAI, and the open-source community.
