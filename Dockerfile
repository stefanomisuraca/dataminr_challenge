FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# dockerize
ENV DOCKERIZE_VERSION v0.6.1
RUN wget -qO - https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz \
    | tar -xzC /usr/local/bin

COPY requirements.in /app/
RUN pip install pip-tools
RUN pip-compile requirements.in -o requirements.txt
RUN pip install -r requirements.txt
COPY . /app/