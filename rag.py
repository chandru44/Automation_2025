from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def create_vector_db(docs):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(docs, embeddings)
