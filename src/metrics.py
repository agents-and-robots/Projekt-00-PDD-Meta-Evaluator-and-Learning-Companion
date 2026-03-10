def compute_metrics(llm_output: str) -> dict:
    """
    Baseline-Metrics: liefert Nullwerte.
    """
    return {
        "clarity": 0,
        "drift_risk": 0,
        "hallucination_risk": 0,
        "didactic_quality": 0
    }
