from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def medical_dataconverter():
    # Load PDFs
    loader = DirectoryLoader("MEDIBOT/DATA", glob="**/*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    chunks = text_splitter.split_documents(documents)

    # Convert to list of objects (like your product_list)
    medical_list = []

    for doc in chunks:
        obj = {
            "content": doc.page_content,
            "source": doc.metadata.get("source", None)
        }
        medical_list.append(obj)

    # Convert objects to LangChain Documents
    docs = []
    for entry in medical_list:
        metadata = {"source": entry["source"]}
        doc = Document(page_content=entry["content"], metadata=metadata)
        docs.append(doc)

    return docs
print("Data conversion completed. Number of documents:", len(medical_dataconverter()))
