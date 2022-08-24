FROM python:3.10.6
ENV NEO4J_URI=bolt://a9b3d3bd6a2cd4b56b1b94e1b77842f0-1055723587.us-east-1.elb.amazonaws.com:7687
ENV USER_NAME=neo4j
ENV PASSWORD=1234
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN apt-get update && \
      apt-get -y install sudo
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
EXPOSE 4005
ENTRYPOINT ["uvicorn", "app.main:app","--host", "0.0.0.0", "--port", "4005"]
#,"--host", "0.0.0.0", "--port", "80"]
#ENTRYPOINT ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker","--host", "0.0.0.0", "--port", "80"]
#--bind 0.0.0.0:80