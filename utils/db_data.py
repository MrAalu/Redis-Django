"""
This Python Module creates a JSON File to Populate Database
"""

import json

# List to Store RAW data
data_list = []

# Create multiple RAW Json Data
for i in range(1, 1001):
    data = {"model": "api.custom_model", "pk": i, "fields": {"title": f"lorem {i}"}}
    data_list.append(data)


# Convert the list to JSON (JSON Format)
json_data = json.dumps(data_list, indent=2)


#  Save the JsonData into a JSON file
with open("populateDatabase.json", "w") as file:
    file.write(json_data)
