import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()


def main():
    # Document loading
    loader = TextLoader("./mediumblog1.txt", encoding="UTF-8")
    document = loader.load()

    # Text Splitting
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)

    # Embedding
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        output_dimensionality=1536,
    )

    # Ingesting
    print("Ingesting...")
    PineconeVectorStore.from_documents(
        texts, embeddings, index_name=os.environ["INDEX_NAME"]
    )


if __name__ == "__main__":
    main()
