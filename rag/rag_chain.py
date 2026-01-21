import os
from langchain_community.vectorstores import FAISS
from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings
from langchain.chains import RetrievalQA
from rag.prompt import rag_prompt
from dotenv import load_dotenv

load_dotenv()

def load_rag_chain():
    embeddings = MistralAIEmbeddings(
        model="mistral-embed",
        api_key=os.getenv("MISTRAL_API_KEY")
    )

    vectorstore = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    llm = ChatMistralAI(
        model="mistral-large-latest",
        temperature=0.2,
        api_key=os.getenv("MISTRAL_API_KEY")
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
        chain_type_kwargs={"prompt": rag_prompt}
    )

    return qa_chain
