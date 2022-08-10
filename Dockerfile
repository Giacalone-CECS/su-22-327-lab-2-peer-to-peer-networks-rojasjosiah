FROM python:3

ADD socket-server-test.py /usr/src/app/
ADD /files/ /usr/src/app/

WORKDIR /usr/src/app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./socket-server-test.py"]
