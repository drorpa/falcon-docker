FROM python:3.8-slim

WORKDIR /code

# Install gunicorn & falcon
# RUN pip install gunicorn falcon
COPY requirements.txt .
RUN pip install -r requirements.txt

# Add demo app
COPY src/ .

CMD ["gunicorn", "--bind", "0.0.0.0:80", "--timeout", "0", "main:app"]
