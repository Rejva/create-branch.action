from python:3.8

WORKDIR /action
COPY . .
RUN pip install .

ENTRYPOINT ["create-branch"]
