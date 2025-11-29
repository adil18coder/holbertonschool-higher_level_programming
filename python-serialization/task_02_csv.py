#!/usr/bin/env python3
"""Module to convert CSV data into JSON format"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts data from a CSV file into JSON format and writes to data.json
    Args:
        csv_filename (str): The name of the CSV file
    Returns:
        bool: True if conversion is successful, False otherwise
    """
    try:
        # Read CSV file using DictReader to convert each row into a dictionary
        with open(csv_filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data_list = list(reader)

        # Write JSON data to output file
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True
    except FileNotFoundError:
        # Return False if the file does not exist
        return False
    except Exception:
        # Return False for any unexpected error
        return False
