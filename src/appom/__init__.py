# appom/__init__.py

"""
APPOM - Adaptive Precision Planter Optimization Model

This module integrates data loading, model training, and planting parameter control
to support precision agriculture under climate variability.
"""

from .data_loader import load_environmental_data
from .model import PrecisionPlantingModel
from .controller import PlantingController
from .utils import calculate_efficiency, log_performance
