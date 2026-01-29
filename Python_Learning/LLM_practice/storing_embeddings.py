from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def vector_store(doc , chunking_size = 500 ,chunk_overlap = 50 ,embeddingmodel = None , FAISS_path = "FAISS_Store"):
    if embeddingmodel == None:
        embeddingmodel = HuggingFaceEmbeddings()

    splitter = CharacterTextSplitter(
        chunk_size=chunking_size,
        chunk_overlap=chunk_overlap,
    )

    chunks = []
    for i in doc:
        chunk = splitter.split_text(i)
        chunks.extend(chunk)

    vector = FAISS.from_texts(chunks,embeddingmodel)
    vector.save_local(FAISS_path)
    return vector

documents = [
    "LangChain is a framework for building applications with large language models.",
    "FAISS is a library for efficient similarity search and clustering of dense vectors."
]

faiss_store = vector_store(documents,FAISS_path="faiss_path")

query = "What is LangChain?"
results = faiss_store.similarity_search(query, k=2)
for r in results:
    print(r.page_content)
