FROM python:3.7-alpine
WORKDIR /Project
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python","wsgi.py"]
