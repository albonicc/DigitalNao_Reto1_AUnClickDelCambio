FROM python:3.8-slim

EXPOSE 8080

COPY ./example_app /example_app
COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "example_app.main:app", "--host", "0.0.0.0", "--port", "8080"]
