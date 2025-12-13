FROM python:3.11-slim

WORKDIR /app
COPY . /app

# No external dependencies needed for Phase 1 minimal runner
RUN python -m compileall -q .

CMD ["python", "run_btb.py", "--tasks", "tasks", "--out", "examples/results.json"]
