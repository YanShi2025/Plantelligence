# appom/data_loader.py

import pandas as pd

def load_environmental_data(file_path):
    """
    Load and preprocess environmental sensor data from CSV.

    Args:
        file_path (str): Path to the raw CSV file.

    Returns:
        pd.DataFrame: Cleaned and structured data.
    """
    try:
        df = pd.read_csv(file_path)
        df = df.dropna()
        return df
    except Exception as e:
        raise IOError(f"Error loading environmental data: {e}")
