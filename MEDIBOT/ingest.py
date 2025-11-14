from dotenv import load_dotenv
import os
from langchain_astradb import AstraDBVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from  MEDIBOT.data_conveter import medical_dataconverter as dataconveter

load_dotenv()

ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")

# Embedding Model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def ingestdata(status):
    # Create AstraDB VectorStore
    vstore = AstraDBVectorStore(
        embedding=embedding,
        collection_name="medicalchatbot",
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APPLICATION_TOKEN,
        namespace=ASTRA_DB_KEYSPACE,
    )
    storage=status
    if storage=="done":
        return vstore
    else:
        pass
    # Data Conversion
    
    docs = dataconveter()

    # Insert into AstraDB
    inserted_ids = vstore.add_documents(docs)

    print(f"Inserted {len(inserted_ids)} documents into Astra DB.")
    return vstore, inserted_ids


if __name__ == "__main__":
    ingestdata()
