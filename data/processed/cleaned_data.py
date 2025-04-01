# data/processed/cleaned_data.py

import pandas as pd

def get_cleaned_data():
    """
    Cleaned version of planting dataset, ready for model training.
    Contains numeric features and target values only.
    """
    data = {
        "temp_C": [18.5, 19.2, 17.9],
        "soil_moisture": [21.5, 19.8, 23.0],
        "humidity": [44.0, 46.5, 45.2],
        "altitude": [230, 230, 230],
        "seed_depth": [4.0, 4.1, 4.2],
        "spacing": [15.0, 14.8, 15.3],
        "speed": [5.2, 5.0, 5.3]
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = get_cleaned_data()
    print(df)
