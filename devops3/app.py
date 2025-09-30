from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Dockerized Flask!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Use official Python image
#FROM python:3.12-slim

# Set working directory
#WORKDIR /app

# Copy app files
#COPY . .

# Install dependencies
#RUN pip install --no-cache-dir -r requirements.txt

# Run the app
#CMD ["python", "app.py"]
