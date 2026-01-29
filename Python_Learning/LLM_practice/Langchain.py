import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def parse_and_chunk_document(file_path: str):
    loader = PyPDFLoader(file_path)
    raw_documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,       
        chunk_overlap=100,      # Maintains semantic continuity
        separators=["\n\n", "\n", " ", ""] # Splits logically by paragraph then sentence
    )

    chunks = text_splitter.split_documents(raw_documents)
    
    print(f"Parsed {len(raw_documents)} pages into {len(chunks)} semantic chunks.")
    return chunks

chunks = parse_and_chunk_document("/Users/odetidhanraj/Documents/My-Learning-with-Technologies/Python_Learning/LLM_practice/Dhanraj_Resume.pdf")
print(chunks)