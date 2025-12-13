# Bayesian Truthfulness Benchmark (BTB) – Green Agent (Phase 1)

This repository contains a **minimal, end-to-end runnable** Green Agent implementation for the AgentX / AgentBeats Phase 1 submission.

It evaluates **Bayesian belief-updating behavior** using a deterministic Bayesian verifier and produces BTI/BEC summary scores.

## What’s included
- `tasks/` : JSON task instances (priors, likelihoods, evidence)
- `run_btb.py` : end-to-end runner (loads tasks → runs baseline purple agent → verifies → scores)
- `baseline_purple_agent.py` : deterministic baseline purple agent (Bayes-optimal posterior)
- `evaluator/` : verifier + metrics + aggregation
- `Dockerfile` : build and run end-to-end without manual intervention
- `benchmark.yaml` : benchmark metadata / entrypoint

> NOTE: The baseline purple agent is deterministic to keep Phase 1 fully runnable without external model APIs.
> Replace `run_purple_agent()` with API calls to GPT/Claude/Mistral in Phase 2.

## Run locally (no Docker)
```bash
python run_btb.py --tasks tasks --out examples/results.json
```

## Run with Docker (end-to-end)
```bash
docker build -t btb-agent .
docker run --rm btb-agent
```

Outputs are written to:
- `examples/results.json`

## Repository structure
```
btb-agent/
  tasks/
  evaluator/
  prompts/
  examples/
  run_btb.py
  baseline_purple_agent.py
  benchmark.yaml
  Dockerfile
  README.md
```

## License
MIT (you can change if needed).
