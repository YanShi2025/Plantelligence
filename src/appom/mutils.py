# appom/utils.py

from sklearn.metrics import r2_score

def calculate_efficiency(actual, predicted):
    """
    Compute the R² score to evaluate model performance.

    Args:
        actual (array-like): Ground truth values.
        predicted (array-like): Model predictions.

    Returns:
        float: R² score.
    """
    return r2_score(actual, predicted)

def log_performance(metrics: dict, file_path="results/reports/performance_log.txt"):
    """
    Log performance metrics to a file.

    Args:
        metrics (dict): Dictionary of metric names and values.
        file_path (str): Path to the output log file.
    """
    with open(file_path, "a") as f:
        for key, value in metrics.items():
            f.write(f"{key}: {value:.4f}\n")
        f.write("-" * 40 + "\n")
