FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies needed for PIL, Torch, OpenCV, etc.
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY streamlit_app/stRequirements.txt .
COPY streamlit_app/main.py .
COPY streamlit_app/pages ./pages

RUN pip install --no-cache-dir -r stRequirements.txt

COPY . .

RUN mkdir -p /app/data/processed
COPY data/processed/processed.csv /app/data/processed/processed.csv
COPY models /app/models

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
