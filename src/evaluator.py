def evaluate(llm_output: str) -> dict:
    return {
        "clarity": 0,
        "drift": 0,
        "hallucination": 0,
        "didactic": 0
    }
