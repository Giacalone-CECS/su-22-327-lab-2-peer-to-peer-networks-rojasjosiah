FROM python:3

ADD node.py /usr/src/app/
ADD /files/ /usr/src/app/

WORKDIR /usr/src/app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update
RUN apt-get install nmap -y

CMD ["python", "./node.py"]
