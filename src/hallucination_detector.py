def detect_hallucination(llm_output: str, real_structure: list[str]) -> dict:
    """
    Baseline-Halluzinations-Detector: erkennt keine Halluzinationen.
    """
    return {
        "hallucinated_files": [],
        "missing_files": []
    }
