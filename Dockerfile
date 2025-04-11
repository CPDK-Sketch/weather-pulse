# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirement files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Default command (runs app.main.py and waits for input)
CMD ["python", "app/main.py"]
