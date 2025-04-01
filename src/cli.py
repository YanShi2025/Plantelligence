# cli.py

"""
Command-line interface for running APPOM + RAPO simulation.

This script:
1. Loads processed environmental data
2. Trains the APPOM model
3. Runs a simulated real-time adaptive planting loop using RAPO
"""

import pandas as pd
from appom.data_loader import load_environmental_data
from appom.model import PrecisionPlantingModel
from appom.controller import PlantingController
from rapo.decision_engine import DecisionEngine
from rapo.adaptation_loop import AdaptationLoop

def main():
    # Step 1: Load and prepare data
    print("[INFO] Loading environmental data...")
    data = load_environmental_data("data/processed/cleaned_data.csv")

    features = data[["temp_C", "soil_moisture", "humidity", "altitude"]]
    targets = data[["seed_depth", "spacing", "speed"]]

    # Step 2: Train APPOM model
    print("[INFO] Training APPOM model...")
    model = PrecisionPlantingModel()
    model.train(features, targets)

    # Step 3: Set up RAPO system
    controller = PlantingController(model)
    decision_engine = DecisionEngine()
    loop = AdaptationLoop(model, controller, decision_engine)

    # Step 4: Simulate streaming data
    print("[INFO] Starting real-time adaptive loop...")
    def simulated_data_stream():
        for _, row in data.iterrows():
            yield row

    loop.run(simulated_data_stream(), delay=1.0)

if __name__ == "__main__":
    main()
