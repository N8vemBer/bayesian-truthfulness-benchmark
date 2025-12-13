from __future__ import annotations
import argparse, json, glob, os, time
from typing import List, Dict, Any
from evaluator.verifier import sequential_posterior
from evaluator.metrics import rmse, brier, explanation_score
from evaluator.aggregate import compute_bti, compute_bec
from baseline_purple_agent import run_purple_agent

def load_tasks(tasks_dir: str) -> List[Dict[str, Any]]:
    files = sorted(glob.glob(os.path.join(tasks_dir, "*.json")))
    tasks = []
    for f in files:
        with open(f, "r", encoding="utf-8") as fh:
            tasks.append(json.load(fh))
    return tasks

def main():
    ap = argparse.ArgumentParser(description="BTB Green Agent (Phase 1 minimal runnable)")
    ap.add_argument("--tasks", default="tasks", help="Directory of task JSON files")
    ap.add_argument("--out", default="examples/results.json", help="Output results JSON path")
    args = ap.parse_args()

    tasks = load_tasks(args.tasks)
    errors = []
    preds = []
    ys = []  # For demo we assume y=1 for "H true"—in real tasks you'd define y per instance.
    expl_scores = []

    per_task = []
    for t in tasks:
        gt = sequential_posterior(t)
        resp = run_purple_agent(t)  # baseline
        pred = float(resp.get("posterior"))
        errors.append(pred - gt)
        preds.append(pred)
        ys.append(1)  # placeholder
        es = explanation_score(resp.get("explanation", ""))
        expl_scores.append(es)
        per_task.append({
            "task_id": t["task_id"],
            "ground_truth_posterior": gt,
            "agent_posterior": pred,
            "abs_error": abs(pred-gt),
            "explanation_score_0_5": es,
            "explanation": resp.get("explanation","")
        })

    rmse_val = rmse(errors)
    brier_val = brier(preds, ys)
    expl_val = sum(expl_scores)/len(expl_scores) if expl_scores else 0.0
    bti = compute_bti(rmse_val, brier_val, expl_val)
    bec = compute_bec(rmse_val, brier_val, expl_val)

    summary = {
        "rmse": rmse_val,
        "brier": brier_val,
        "avg_explanation_score_0_5": expl_val,
        "BTI_0_100": bti,
        "BEC_0_1": bec,
        "n_tasks": len(tasks)
    }

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump({"summary": summary, "per_task": per_task}, fh, indent=2)

    print("BTB run complete.")
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
