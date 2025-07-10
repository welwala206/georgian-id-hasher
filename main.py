# MIT License
# 
# Copyright (c) 2025 Irakli Natsvlishvili
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse  # For parsing command-line arguments
import hashlib   # For hashing functionalities
import hmac      # For HMAC hashing
import logging   # For logging events and errors
import os        # For basic OS operations
import re        # For regex matching
from pathlib import Path  # For modern path handling

import pandas as pd  # For handling CSV and Excel files

# Setup logging configuration
logging.basicConfig(
    filename='file_processor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class FileProcessor:
    # Define the regular expression to match 11-digit IDs
    ID_PATTERN = re.compile(r'^\d{11}$')

    def __init__(self, path, secret_key):
        self.path = Path(path)  # Store the path as a Path object
        self.secret_key = secret_key.encode()  # Encode the secret key to bytes

    # Function to generate HMAC hash for a given ID
    def hmac_hash_id(self, id_value):
        return hmac.new(self.secret_key, str(id_value).encode(), hashlib.sha3_512).hexdigest()

    # Read file (either Excel or CSV) into a pandas DataFrame
    def read_file(self, file_path):
        logging.info(f"Reading file: {file_path}")
        return pd.read_excel(file_path, dtype=str) if file_path.suffix == '.xlsx' else pd.read_csv(file_path, dtype=str)

    # Write DataFrame back to file (Excel or CSV)
    def write_file(self, file_path, data):
        logging.info(f"Writing file: {file_path}")
        if file_path.suffix == '.xlsx':
            data.to_excel(file_path, index=False)
        else:
            data.to_csv(file_path, index=False)

    # Replace 11-digit IDs in the data and create mapping file
    def replace_ids(self, data, file_path):
        id_map = []

        for column in data.columns:
            mask = data[column].apply(lambda x: bool(self.ID_PATTERN.match(str(x))))
            if mask.any():
                original_values = data.loc[mask, column]
                data.loc[mask, column] = original_values.map(self.hmac_hash_id)
                id_map.extend(zip(original_values, data.loc[mask, column]))
                logging.info(f"Column '{column}' processed.")

        # Save the ID mapping if any IDs were replaced
        if id_map:
            map_df = pd.DataFrame(id_map, columns=["Original_ID", "Hashed_ID"])
            map_file = file_path.parent / f"map_{file_path.name}"
            self.write_file(map_file, map_df)

        return data

    # Process a single file: read, replace IDs, save hashed version
    def process_file(self, file_path):
        logging.info(f"Processing: {file_path}")
        try:
            data = self.read_file(file_path)
            data = self.replace_ids(data, file_path)
            output_path = file_path.parent / f"hashed_{file_path.name}"
            self.write_file(output_path, data)
        except Exception as e:
            logging.error(f"Failed processing {file_path}: {e}")

    # Process all applicable files within a directory
    def run(self):
        if self.path.is_dir():
            for file in self.path.glob('*.csv') | self.path.glob('*.xlsx'):
                self.process_file(file)
        elif self.path.is_file() and self.path.suffix in ('.csv', '.xlsx'):
            self.process_file(self.path)
        else:
            logging.error(f"Invalid path or unsupported file format: {self.path}")


# Helper function to load the HMAC key from arguments or file
def load_key(args):
    if args.key:
        return args.key
    if args.key_file:
        try:
            return Path(args.key_file).read_text().strip()
        except FileNotFoundError:
            logging.error("Key file not found.")
            exit(1)
    logging.warning("No key provided. Using empty key.")
    return ""


# Main execution block
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HMAC-hash 11-digit IDs in CSV/XLSX files or all files in a directory.')
    parser.add_argument('path', type=str, help='Path to file or directory')
    parser.add_argument('--key', type=str, help='Secret key for HMAC')
    parser.add_argument('--key-file', type=str, help='Path to file containing HMAC key')
    args = parser.parse_args()

    secret_key = load_key(args)  # Load HMAC key
    processor = FileProcessor(args.path, secret_key)  # Initialize processor
    processor.run()  # Start processing based on given path
