#!/usr/bin/env python3
"""
Automatically downloads the CIC-IDS2018 dataset from Kaggle
"""

import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Setup paths
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(DATA_DIR, exist_ok=True)

def download_dataset():
    """Download and extract dataset from Kaggle"""
    try:
        # Initialize Kaggle API
        api = KaggleApi()
        api.authenticate()

        # Download dataset
        print("Downloading dataset from Kaggle...")
        api.dataset_download_files(
            'solarmainframe/ids-intrusion-csv',
            path=DATA_DIR,
            unzip=True,
            quiet=False
        )

        # Verify download
        expected_file = os.path.join(DATA_DIR, '03-02-2018.csv')
        if os.path.exists(expected_file):
            print(f"Successfully downloaded dataset to {expected_file}")
        else:
            raise FileNotFoundError("Dataset file not found after download")

    except Exception as e:
        print(f"Error downloading dataset: {str(e)}")
        raise

if __name__ == "__main__":
    download_dataset()