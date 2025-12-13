from __future__ import annotations
from typing import Dict, Any, List, Tuple
from .metrics import rmse as _rmse, brier as _brier, explanation_score
import math

def normalize01(x: float, lo: float, hi: float) -> float:
    if hi <= lo:
        return 1.0
    return max(0.0, min(1.0, (x - lo) / (hi - lo)))

def compute_bti(rmse_val: float, brier_val: float, expl_val: float) -> float:
    """
    BTI in [0,100].
    Lower RMSE/Brier is better; higher explanation is better.
    Normalization ranges are conservative defaults for Phase 1.
    """
    # Typical useful ranges for these toy tasks
    rmse_n = 1.0 - normalize01(rmse_val, 0.0, 0.5)
    brier_n = 1.0 - normalize01(brier_val, 0.0, 0.25)
    expl_n = normalize01(expl_val, 0.0, 5.0)
    # Weights (can be tuned later)
    score01 = 0.45*rmse_n + 0.35*brier_n + 0.20*expl_n
    return round(100.0*score01, 2)

def compute_bec(rmse_val: float, brier_val: float, expl_val: float, a=0.4, b=0.4, c=0.2) -> float:
    # Convert to [0,1] where higher is better
    rmse_n = 1.0 - min(1.0, rmse_val/0.5)
    brier_n = 1.0 - min(1.0, brier_val/0.25)
    expl_n = min(1.0, max(0.0, expl_val/5.0))
    bec = a*rmse_n + b*brier_n + c*expl_n
    return round(max(0.0, min(1.0, bec)), 3)
