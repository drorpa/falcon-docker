FROM python:3.8-slim

EXPOSE 80

WORKDIR /code

# Install gunicorn & falcon
# RUN pip install gunicorn falcon
COPY requirements.txt .
RUN pip install -r requirements.txt

# Add demo app
COPY src/ .

CMD ["gunicorn", "-b", "0.0.0.0:80", "main:app"]
