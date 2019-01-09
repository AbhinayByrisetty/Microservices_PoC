FROM ubuntu:16.04
ENV http_proxy http://138.85.224.137:8080
ENV https_proxy https://138.85.224.137:8080

RUN apt-get update -y && \
    apt-get install -y curl \
            vim \
            wget \
            python-pip \
            python-dev && \
    apt-get remove -y python-pip python3-pip && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
ENV http_proxy ""
ENV https_proxy ""
RUN mkdir -p /database
COPY todo.json /database/
COPY todo.py /app/

ENTRYPOINT ["python"]
CMD ["todo.py"]

