#!/usr/bin/env python3
"""
download_data.py

This script downloads the ODI Men's Cricket Match Data (2002-2023) dataset from Kaggle
and extracts it to a local folder named 'data'.

Prerequisites:
- Install the Kaggle API: pip install kaggle
- Set up your Kaggle API credentials:
    - Place your kaggle.json file (downloaded from Kaggle) in the ~/.kaggle/ folder.
    - Ensure the permissions are set appropriately (e.g., chmod 600 ~/.kaggle/kaggle.json).

Usage:
    python download_data.py
"""

import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    # Initialize and authenticate the Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Define the dataset identifier from Kaggle
    dataset = 'utkarshtomar736/odi-mens-cricket-match-data-2002-2023'
    
    # Create a directory to save the data if it doesn't exist
    data_dir = 'data'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # Download and unzip the dataset to the data directory
    print("Downloading dataset...")
    api.dataset_download_files(dataset, path=data_dir, unzip=True)
    print("Download complete. Data is available in the 'data' folder.")

if __name__ == '__main__':
    download_dataset()