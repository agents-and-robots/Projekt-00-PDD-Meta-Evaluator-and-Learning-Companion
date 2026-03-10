def detect_hallucination(llm_output: str, real_structure: list[str]) -> dict:
    return {
        "hallucinated_files": [],
        "missing_files": []
    }
