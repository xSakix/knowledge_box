from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
    MilvusClient
)

client = MilvusClient(uri="http://localhost:19530")  
res = client.list_collections()
print(res)

