# tests/test_controller.py

import pandas as pd
from appom.model import PrecisionPlantingModel
from appom.controller import PlantingController

def test_controller_adjust_parameters():
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
    controller = PlantingController(model)

    result = controller.adjust_parameters(X.iloc[[0]])
    assert isinstance(result, dict)
    assert "depth" in result and "spacing" in result and "speed" in result
    assert isinstance(result["depth"], float)
