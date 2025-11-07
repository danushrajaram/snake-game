FROM python:3.10-slim

WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set PYTHONPATH so "app" can be imported anywhere
ENV PYTHONPATH=/app

EXPOSE 5000

# Run the Flask app
CMD ["python", "-m", "app.web_snake"]
