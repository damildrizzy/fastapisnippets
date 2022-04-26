FROM python:3.9

WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt

# Allow installing dev dependencies to run tests
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app
ENV PYTHONPATH=/app

CMD uvicorn app.main:app --host 0.0.0.0 --port 5000