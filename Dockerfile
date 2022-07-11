FROM python:latest
ADD . /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# CMD ["python", "main.py"]