import os
from langchain_chroma import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

# Define the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db", "chroma_db")

# Define the embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") # Update to a valid embedding model if needed

# Load the existing vector store with the embedding function
db = Chroma(persist_directory=persistent_directory,
            embedding_function=embeddings)

# Define the user's question
query = "What is Theano?"

# Way 1: Retrieve relevant documents based on the query
retriever = db.as_retriever(
    #search_type="similarity_score_threshold",
    #search_kwargs={"k": 3, "score_threshold": 0.5}, 
    search_type="mmr",
    search_kwargs={"k": 2, "fetch_k": 5}

)

#relevant_docs = retriever.invoke(query)

# Way 2: Retrieve relevant documents based on the query
relevant_docs = db.similarity_search(query, k=1)

# Display the relevant results with metadata
print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")
    if doc.metadata:
        print(f"Source: {doc.metadata.get('source', 'Unknown')}\n")