FROM python:3.10-slim

WORKDIR /app

# Copy the entire project folder contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (for Render or local use)
EXPOSE 8080

# Set environment variables (optional, better to pass securely at runtime)
ENV AWS_DEFAULT_REGION=us-east-1

# Run the Flask app using Python
CMD ["python", "app.py"]
