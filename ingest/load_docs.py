import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_documents():
    docs = []

    resume = os.path.join(DATA_DIR, "resume.pdf")
    github = os.path.join(DATA_DIR, "github.txt")
    linkedin = os.path.join(DATA_DIR, "linkedin.txt")

    docs.extend(PyPDFLoader(resume).load())
    docs.extend(TextLoader(github).load())
    docs.extend(TextLoader(linkedin).load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    return splitter.split_documents(docs)
