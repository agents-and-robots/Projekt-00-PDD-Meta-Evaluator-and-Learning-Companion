def detect_drift(project_a: dict, project_b: dict) -> dict:
    """
    Baseline-Drift-Detector: erkennt keinen Drift.
    """
    return {
        "structural": False,
        "semantic": False,
        "methodological": False
    }
