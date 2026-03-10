def compute_metrics(llm_output: str) -> dict:
    return {
        "clarity": 0,
        "drift_risk": 0,
        "hallucination_risk": 0,
        "didactic_quality": 0,
        "instruction_completeness": 0,
        "agentic_robustness": 0,
        "test_coverage": 0,
        "cognitive_load": 0,
        "llm_readiness": 0
    }
