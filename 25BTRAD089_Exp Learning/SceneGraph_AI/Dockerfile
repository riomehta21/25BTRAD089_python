FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Copy requirements from SceneGraph_Production
COPY SceneGraph_Production/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all application files from SceneGraph_Production directly into /app
COPY SceneGraph_Production/ .

# Expose ports
EXPOSE 8000 7860

# Launch FastAPI with dynamic port
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}"]
