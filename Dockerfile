FROM python:3.6

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
RUN python -m spacy download de

COPY . /app

CMD ["python", "/app/main.py"]