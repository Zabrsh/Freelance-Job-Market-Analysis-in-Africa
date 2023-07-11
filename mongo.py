from pymongo import MongoClient
import json

# Connection URI
client = MongoClient("")

# Select database
db_name = 'africa-freelance'
collection_name = 'data'

# Load job titles from JSON file
with open('jobs.json', 'r') as f:
    data = json.load(f)
# Connect to MongoDB

db = client[db_name]
collection = db[collection_name]
# Try inserting data to MongoDB
try:
    collection.insert_many(data)
    print("Data inserted successfully.")
except Exception as e:
    print("An error occurred while trying to insert data to MongoDB:", str(e))

