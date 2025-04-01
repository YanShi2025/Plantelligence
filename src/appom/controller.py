# appom/controller.py

class PlantingController:
    """
    Uses the trained model to control planter settings dynamically.
    """

    def __init__(self, model):
        self.model = model

    def adjust_parameters(self, sensor_data):
        """
        Predict and return optimal planter settings from environmental input.

        Args:
            sensor_data (pd.DataFrame): Real-time sensor data (one or more rows).

        Returns:
            dict: Recommended parameters (e.g., depth, spacing, speed).
        """
        predictions = self.model.predict(sensor_data)

        if predictions.ndim == 1:
            depth, spacing, speed = predictions[0], None, None
        else:
            depth, spacing, speed = predictions[0]

        return {
            "depth": float(depth),
            "spacing": float(spacing) if spacing is not None else None,
            "speed": float(speed) if speed is not None else None
        }
