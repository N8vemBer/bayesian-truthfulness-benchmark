FROM python:3.11-slim

WORKDIR /app

# Copy everything from the repo into the container
COPY . /app

# If you later add dependencies, uncomment:
# RUN pip install --no-cache-dir -r requirements.txt

# Default command: run the agent entrypoint
CMD ["python", "agent.py"]
