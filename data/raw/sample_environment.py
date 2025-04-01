# data/raw/sample_environment.py

import pandas as pd

def get_sample_raw_data():
    """
    Simulated raw sensor data representing field environment snapshots.
    Returns a DataFrame resembling real-world input before processing.
    """
    data = {
        "timestamp": [
            "2025-04-01 07:00:00",
            "2025-04-01 07:10:00",
            "2025-04-01 07:20:00"
        ],
        "location": ["Field_A", "Field_A", "Field_A"],
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
    df = get_sample_raw_data()
    print(df)
