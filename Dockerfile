# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your Python code
COPY main.py .

# Install Flask
RUN pip install flask

# Expose Flask port
EXPOSE 5000

# Run Flask app
CMD ["python", "main.py"]
