import json
import csv
import sys

def json_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Check if the data is a list of dictionaries
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON file must contain a list of dictionaries")
    
    # Get the keys from the first dictionary as the CSV headers
    headers = data[0].keys()
    
    # Open the CSV file and write the data
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python converter.py <input_json_file> <output_csv_file>")
    else:
        json_to_csv(sys.argv[1], sys.argv[2])
