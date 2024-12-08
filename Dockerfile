FROM python:3.12-slim

COPY requirements.txt /

COPY ./apilog/apilog.py /app/

RUN pip install -r requirements.txt

CMD ["python", "/app/apilog.py"]