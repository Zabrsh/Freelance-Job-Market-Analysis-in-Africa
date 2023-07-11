from google.cloud import storage
import json

# Create a client using the default credentials
storage_client = storage.Client()

bucket_name = 'jobs_bucket01'
file_path = 'jobs.json'  # Replace with the path to your JSON file

with open(file_path, 'r') as file:
    json_data = json.load(file)

# Remove empty objects from the JSON data
json_data = [data for data in json_data if data]

blob_name = 'jobs.json'  # Destination blob name in the bucket

bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.upload_from_string(json.dumps(json_data), content_type='application/json')

print(f'Filtered JSON data from {file_path} uploaded to {blob_name} in {bucket_name}.')
