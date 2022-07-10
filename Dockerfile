FROM python:latest
ADD . /app
WORKDIR /app
COPY requirements.txt requirements.txt
# RUN pip3 install pymongo
RUN pip3 install -r requirements.txt
# CMD ["pip3", "list"]
CMD ["python", "main.py"]