from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any, List, Tuple
import math

def bayes_update(prior: float, p_e_given_h: float, p_e_given_not_h: float) -> float:
    """Closed-form Bayes update for a binary hypothesis."""
    # Clamp to avoid divide-by-zero
    prior = min(max(prior, 0.0), 1.0)
    p_e_given_h = min(max(p_e_given_h, 0.0), 1.0)
    p_e_given_not_h = min(max(p_e_given_not_h, 0.0), 1.0)
    denom = p_e_given_h * prior + p_e_given_not_h * (1.0 - prior)
    if denom == 0.0:
        # If evidence impossible under both, posterior undefined; return prior as conservative fallback.
        return prior
    return (p_e_given_h * prior) / denom

def sequential_posterior(task: Dict[str, Any]) -> float:
    """Compute Bayesian posterior for possibly multiple independent evidence items (naïve independence assumption)."""
    p = float(task["prior"])
    for ev in task.get("evidence", []):
        p = bayes_update(p, float(ev["likelihood_given_H"]), float(ev["likelihood_given_not_H"]))
    return p
