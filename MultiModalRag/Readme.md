# Multi Modal Rag Application : Your Personal Optimized AI assistant
## Tech Stack
- **Backend:**
  - **LangChain:** Utilized for efficient multi-modal data ingestion and retrieval. LangChain seamlessly integrates with various ChatModels such as Cerebras, Google Gemini, Mistral AI, among others. It also supports HuggingFaceEmbeddings and Question-Answering pipelines, resulting in a robust and effective multi-modal Retrieval Augmented Generation (RAG) system.
  - **HuggingFace Embeddings:** Employed to convert document content into dense vector representations, enabling efficient similarity-based searches.
  - **FAISS:** An open-source library designed for fast and efficient similarity search and clustering of dense vectors. FAISS is highly optimized for large-scale data, offering nearest neighbor search capabilities, GPU acceleration, and flexible indexing techniques. It is widely used in recommendation systems, natural language processing, and other large-scale machine learning applications.

- **Language Models:**
  - **Google Gemini-2.0-flash**: A Multi-Modal model with the ability to parse multi-modal data such as complicated handwritten notes, graph plots , abstract paintings , documentations .
  - **Llama-3.3-70b**: Used to answer questions based on document or video content.
  - **Deepseek-r1-distill-llama-3.3-70b** : Used to perform complex reasoning and provide a comprehensive detailed answer 
  - **sentence-transformers/all-mpnet-base-v2**: This is a sentence-transformers model: It maps sentences & paragraphs to a 384 dimensional dense vector space and can be used for tasks like clustering or semantic search.
 
- **ML Libraries:**
  - **scikit-learn TF-IDF:** A statistical measure used to convert text into numerical features by weighting the importance of words in a document relative to a corpus. This approach aids in tasks like document classification, clustering, and information retrieval.
 
> Check the pages Readme for the WorkFlow
 
    
