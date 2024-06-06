import pymongo
import openai
import os
from llama_index.core import VectorStoreIndex, StorageContext, SimpleDirectoryReader
from llama_index.core.storage.docstore import MongoDocumentStore
from llama_index.core.storage.index_store import MongoIndexStore
from llama_index.core.storage.storage_context import StorageContext
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
mongo_uri = os.getenv("MONGO_URI")


mongodb_client = pymongo.MongoClient(mongo_uri)

if mongodb_client :
    print("Connection is successful!")
else:
    print("Connection is not successful!")

storage_context = StorageContext.from_defaults(
    docstore=MongoDocumentStore.from_uri(uri=mongo_uri),
    index_store=MongoIndexStore.from_uri(uri=mongo_uri),
)


#index_store=MongoIndexStore.from_uri(uri=mongo_uri, db_name=mongodb_database),
documents = SimpleDirectoryReader("input/text").load_data()
index = VectorStoreIndex.from_documents(documents, storage_context= storage_context)
print(index)

query_engine = index.as_query_engine()
response = query_engine.query("<query>")
print(response)