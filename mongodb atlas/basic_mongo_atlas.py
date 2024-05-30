import pymongo
import openai
import os
from llama_index import VectorStoreIndex, StorageContext, SimpleDirectoryReader
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from llama_index.storage.storage_context import StorageContext
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
mongo_uri = os.getenv("MONGO_URI")


mongodb_client = pymongo.MongoClient(mongo_uri)

if mongodb_client :
    print("Connection is successful!")
else:
    print("Connection is not successful!")

store = MongoDBAtlasVectorSearch(mongodb_client)
# print(store)

storage_context = StorageContext.from_defaults(
    vector_store=store
)

documents = SimpleDirectoryReader("input/text").load_data()
index = VectorStoreIndex.from_documents(documents, storage_context= storage_context)
#print(index)

query_engine = index.as_query_engine()
response = query_engine.query("<query>")
print(response)