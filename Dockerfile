# Iron Man HUD – FastAPI + Render Optimized

FROM python:3.12-slim

WORKDIR /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Use Render's dynamic $PORT environment variable
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

