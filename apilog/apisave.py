from pymongo import MongoClient
import pandas as pd

import os
MONGO_URL = os.getenv('MONGO_URL')


if MONGO_URL==None:
    print('Lembra indicar a variable MONGO_URL')
    print('p.ex: export MONGO_URL=url_de_mongodb')
    print('p.ex: docker run --rm -e MONGO_URL=mongodb://localhost:27017/')
    exit(1)

mongo_url = MONGO_URL
mongo_db_name = "citybik_database"
mongo_db_collection_name = "bicicorunha_stations"

    
# load data from MongoDB
def load_data_mongo(collection):
    # Define the aggregation pipeline
    pipeline = [
        {
        "$addFields": {
            "uid": "$extra.uid",
            "last_updated": "$extra.last_updated",
            "slots": "$extra.slots",
            "normal_bikes": "$extra.normal_bikes",
            "ebikes": "$extra.ebikes",
        }
        },
        {
        "$project": {
            "_id": 0,
            "id": 1,
            "name": 1,
            "timestamp": 1,
            "free_bikes": 1,
            "empty_slots": 1,
            "uid": 1,
            "last_updated": 1,
            "slots": 1,
            "normal_bikes": 1,
            "ebikes": 1,
        }
    }
    ]
    result = list(collection.aggregate(pipeline))
    return result

# Set up MongoDB connection
try:
    client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
    db = client[mongo_db_name]
    collection = db[mongo_db_collection_name]
except pymongo.errors.ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")
    exit(1)

# Main
print('Cargando datos...')
data = load_data_mongo(collection)
print('Creando DataFrame')
df = pd.DataFrame(data)
print('Escribindo CSV')
df.to_csv('bicicorunha_data.csv')
print('Escribindo PARQUET')
df.to_parquet('bicicorunha_data.parquet')

    

