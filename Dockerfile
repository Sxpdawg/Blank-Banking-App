# Use an official lightweight Python image
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (needed for MySQL connector)
RUN apt-get update && apt-get install -y \
    build-essential \
    libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Expose the port (if running as a web service)
EXPOSE 8080

# Command to run the application (placeholder for web entrypoint)
CMD ["python", "app.py"]
