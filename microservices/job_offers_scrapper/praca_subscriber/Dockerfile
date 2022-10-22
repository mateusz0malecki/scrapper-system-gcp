FROM python:3.10-slim

ENV PYTHONUNBUFFERED True
ENV PORT 5000

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD password
ENV POSTGRES_HOST 192.168.0.3
ENV POSTGRES_PORT 5432
ENV POSTGRES_DB job-offers-pracuj

COPY . ./

RUN pip install -r requirements.txt

CMD python app.py