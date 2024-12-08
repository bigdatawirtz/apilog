import requests
from pymongo import MongoClient
import time

import os
MONGO_URL = os.getenv('MONGO_URL')
INTERVAL = os.getenv('INTERVAL')

if MONGO_URL==None:
    print('Lembra indicar a variable MONGO_URL')
    print('p.ex: export MONGO_URL=url_de_mongodb')
    print('p.ex: docker run --rm -e MONGO_URL=mongodb://localhost:27017/')
    exit(1)

if INTERVAL==None:
    print('Intevalo predeterminado de 120 segundos entre peticións')
    INTERVAL=120

# configuration variables
api_url = "http://api.citybik.es/v2/networks/bicicorunha"
mongo_url = MONGO_URL
mongo_db_name = "citybik_database"
mongo_db_collection_name = "bicicorunha_stations"

# get data from api
def get_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data from API: {e}")
        return None
    
# store data in MongoDB
def mongo_store(stations,collection):
    if stations is not None:
        try:
            collection.insert_many(stations)
            print("Data stored successfully in MongoDB")
        except Exception as e:
            print(f"Failed to store data in MongoDB: {e}")
    else:
        print("Failed to retrieve data from API")

# Set up MongoDB connection
try:
    client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
    db = client[mongo_db_name]
    collection = db[mongo_db_collection_name]
except pymongo.errors.ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")
    exit(1)

# Main loop to fetch and store data at specified intervals
try:
    while True:
        data = get_data(api_url)
        stations = data['network']['stations']
        mongo_store(stations,collection)
        time.sleep(int(INTERVAL))  
except KeyboardInterrupt:
    print("\nInterrupted by user. Exiting")

