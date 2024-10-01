# from pymongo import MongoClient
# from datetime import datetime

# # Connect to MongoDB (replace <username>, <password>, <dbname> with your details)
# client = MongoClient('mongodb+srv://kothapallisantoshece22:6zPFY03uyofZn3oV@cluster0.iyzydsp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
# db = client['test']  # Select database
# collection = db['cars']   # Select collection

# # Example function to extract data from images (your existing extraction code)
# def extract_data_from_image(image):
#     # Your data extraction logic goes here (e.g., speed, fuel level, temperature)
#     data = {
#         'speed': '85 km/h',
#         'fuelLevel': '60%',
#         'temperature': '95°C',
#         'timestamp': datetime.now()  # Store the current timestamp
#     }
#     return data

# # Function to insert extracted data into MongoDB
# def store_data_in_mongodb(data):
#     try:
#         result = collection.insert_one(data)
#         print(f"Data inserted with ID: {result.inserted_id}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# image = 'dashboard_image.png'  # Placeholder for actual image
# extracted_data = extract_data_from_image(image)  # Call to your image processing function
# store_data_in_mongodb(extracted_data)  # Insert the data into MongoDB

import requests

url = 'http://localhost:3000/add'

# JSON data to be sent
json_data = {
    'speed': '85 km/h',
    'fuelLevel': '60%',
    'distanceTravelled': '100',
}

# Sending the POST request with JSON data
response = requests.post(url, json=json_data)

# Print the response
# print(f"Status Code: {response.status_code}")
# print(f"Response Text: {response.text}")


if response.status_code == 201:
    print('Success:', response.json())
else:
    print('Failed:', response.text)
