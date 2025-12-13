from __future__ import annotations
from typing import Dict, Any
from evaluator.verifier import sequential_posterior

def run_purple_agent(task: Dict[str, Any]) -> Dict[str, Any]:
    """
    Baseline Purple Agent: returns the Bayes-optimal posterior with a short explanation.
    This makes the whole pipeline runnable end-to-end without external APIs.
    Replace later with calls to real LLMs.
    """
    p = sequential_posterior(task)
    expl = (
        f"I start from the prior P(H)={task['prior']}. "
        f"I update using the provided likelihoods P(E|H) and P(E|¬H) via Bayes' rule. "
        f"This yields posterior P(H|E)≈{p:.4f}."
    )
    return {"posterior": float(f"{p:.6f}"), "explanation": expl}
