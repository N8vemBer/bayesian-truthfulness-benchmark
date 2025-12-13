from __future__ import annotations
from typing import Dict, Any, List
import math

def rmse(errors: List[float]) -> float:
    if not errors:
        return 0.0
    return math.sqrt(sum(e*e for e in errors)/len(errors))

def brier(preds: List[float], ys: List[int]) -> float:
    if not preds:
        return 0.0
    return sum((p - y)**2 for p, y in zip(preds, ys))/len(preds)

def explanation_score(expl: str) -> float:
    """
    Minimal rubric placeholder (0-5) for Phase 1.
    You can replace with human scores or LLM-judge later.
    Heuristic: mentions prior and evidence likelihoods -> higher.
    """
    if not expl:
        return 0.0
    e = expl.lower()
    score = 1.5
    if "prior" in e or "p(h)" in e:
        score += 1.0
    if "likelihood" in e or "p(e|h" in e or "p(e|¬h" in e or "p(e|not" in e:
        score += 1.5
    if "uncertain" in e or "confidence" in e or "calibr" in e:
        score += 0.5
    return max(0.0, min(5.0, score))
