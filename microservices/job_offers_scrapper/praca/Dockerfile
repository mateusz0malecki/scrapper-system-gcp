FROM python:3.10-slim

ENV PYTHONUNBUFFERED True
ENV PORT 5000

COPY . ./

RUN pip install -r requirements.txt

CMD python app.py
