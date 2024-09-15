# Use official Python 3.11 base image for efficiency
FROM python:3.11-slim

# Set environment variables to avoid Python creating .pyc files and to run in unbuffered mode
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies in one layer
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the FastAPI port
EXPOSE 5000

# Default command for running in development mode
CMD ["fastapi", "dev", "app/main.py", "--host", "0.0.0.0", "--port", "5000"]

# Optional: Switch to production mode
# Uncomment this if you're building for production
# CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "5000"]