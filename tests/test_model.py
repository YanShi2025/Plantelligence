# tests/test_model.py

import pandas as pd
import pytest
from appom.model import PrecisionPlantingModel

def test_model_training_and_prediction():
    # Sample input features and target values
    X = pd.DataFrame({
        "temp_C": [18.5, 19.0, 18.8],
        "soil_moisture": [22.1, 23.0, 22.5],
        "humidity": [45.3, 44.0, 46.0],
        "altitude": [230, 230, 230]
    })

    y = pd.DataFrame({
        "seed_depth": [4.0, 4.2, 4.1],
        "spacing": [15.0, 14.8, 15.2],
        "speed": [5.2, 5.3, 5.1]
    })

    model = PrecisionPlantingModel()
    model.train(X, y)
    preds = model.predict(X)

    assert preds.shape == (3, 3)
    assert isinstance(preds[0][0], float)
