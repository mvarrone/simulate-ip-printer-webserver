FROM python:3.9.7

WORKDIR /usr/src

COPY requirements.txt ./

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD ["sh", "docker-entrypoint.sh"]
