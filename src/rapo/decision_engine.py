# rapo/decision_engine.py

"""
Decision engine for RAPO (Real-Time Adaptive Planter Optimization)

This module handles logic to interpret model predictions and environmental context,
enabling intelligent, real-time planting decisions.
"""

class DecisionEngine:
    def __init__(self, thresholds=None):
        """
        Initialize with configurable thresholds.

        Args:
            thresholds (dict): Optional thresholds for adjusting behavior.
                Example: {"soil_moisture_low": 20, "temp_high": 30}
        """
        self.thresholds = thresholds or {
            "soil_moisture_low": 20,
            "temp_high": 35
        }

    def evaluate_conditions(self, environment_row):
        """
        Make a contextual decision based on environmental conditions.

        Args:
            environment_row (dict or pd.Series): Single row of real-time data.

        Returns:
            dict: Modifiers or flags to influence planting behavior.
        """
        modifiers = {}

        if environment_row["soil_moisture"] < self.thresholds["soil_moisture_low"]:
            modifiers["reduce_depth"] = True

        if environment_row["temp_C"] > self.thresholds["temp_high"]:
            modifiers["reduce_speed"] = True

        return modifiers
