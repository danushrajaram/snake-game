FROM python:3.10-slim

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
ENV PYTHONPATH=/app
CMD ["python", "-m", "app.web_snake"]
