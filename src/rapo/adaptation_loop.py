# rapo/adaptation_loop.py

"""
Adaptation loop for RAPO

This module implements a continuous decision + action loop for intelligent planting.
"""

import time

class AdaptationLoop:
    def __init__(self, model, controller, decision_engine):
        """
        Set up the adaptive control system.

        Args:
            model: Trained prediction model (e.g., APPOM)
            controller: PlantingController instance
            decision_engine: DecisionEngine instance
        """
        self.model = model
        self.controller = controller
        self.decision_engine = decision_engine

    def run(self, data_stream, delay=1.0):
        """
        Run the real-time loop with incoming sensor data.

        Args:
            data_stream (iterable): Yields rows of environmental data (dicts or Series)
            delay (float): Delay between iterations in seconds (simulates real-time)
        """
        for row in data_stream:
            print(f"[INFO] Reading new sensor data: {row}")

            # Optional contextual modifications
            context = self.decision_engine.evaluate_conditions(row)

            # Prepare row for model
            features = row[["temp_C", "soil_moisture", "humidity", "altitude"]].to_frame().T

            # Predict parameters
            recommendation = self.controller.adjust_parameters(features)

            # Modify based on context
            if context.get("reduce_depth"):
                recommendation["depth"] *= 0.9
            if context.get("reduce_speed"):
                recommendation["speed"] *= 0.8

            print(f"[ACTION] Adjusted planting parameters: {recommendation}")
            time.sleep(delay)
