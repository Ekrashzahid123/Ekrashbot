import os
from ingest.load_docs import load_documents
from langchain_community.vectorstores import FAISS
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def build_vectorstore():
    documents = load_documents()

    embeddings = MistralAIEmbeddings(
        model="mistral-embed",
        api_key=os.getenv("MISTRAL_API_KEY")
    )

    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local("vectorstore")

    print("✅ Vectorstore created successfully")

if __name__ == "__main__":
    build_vectorstore()
