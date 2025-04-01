# tests/test_rapo.py

import pandas as pd
from appom.model import PrecisionPlantingModel
from appom.controller import PlantingController
from rapo.decision_engine import DecisionEngine
from rapo.adaptation_loop import AdaptationLoop

def test_decision_engine_logic():
    engine = DecisionEngine(thresholds={"soil_moisture_low": 20, "temp_high": 30})
    row = pd.Series({"temp_C": 32, "soil_moisture": 18})
    result = engine.evaluate_conditions(row)
    assert result["reduce_depth"] is True
    assert result["reduce_speed"] is True

def test_adaptation_loop_step():
    # Mock data and model
    df = pd.DataFrame({
        "temp_C": [18.5],
        "soil_moisture": [22.1],
        "humidity": [45.3],
        "altitude": [230],
        "seed_depth": [4.0],
        "spacing": [15.0],
        "speed": [5.2]
    })

    X = df[["temp_C", "soil_moisture", "humidity", "altitude"]]
    y = df[["seed_depth", "spacing", "speed"]]

    model = PrecisionPlantingModel()
    model.train(X, y)

    controller = PlantingController(model)
    engine = DecisionEngine()
    loop = AdaptationLoop(model, controller, engine)

    def one_step_stream():
        for _, row in df.iterrows():
            yield row

    # Simulate one iteration (should not raise any error)
    loop.run(one_step_stream(), delay=0.1)
