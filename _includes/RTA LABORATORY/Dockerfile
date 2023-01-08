FROM python:3.10

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5050

ENTRYPOINT ["python"]
CMD ["app.py"]
