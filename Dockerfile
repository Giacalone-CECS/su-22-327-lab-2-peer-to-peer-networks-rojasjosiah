FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#RUN apt update --help
#RUN apt install nmap

COPY . .

#CMD ["python", "./socket-server-test.py"]
#CMD ["nmap", "-sn", "-v", "192.168.1.0/24"]
# /usr/local/bin/python -m pip install --upgrade pip
CMD ["./usr/src/app/nmap", "-sT", "-p-", "localhost"]
