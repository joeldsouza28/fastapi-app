FROM python:3.13-slim



RUN apt-get update && \
    apt-get install -y nginx && \
    rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/


EXPOSE 80

ENTRYPOINT ["/bin/bash", "-c",  "nginx && gunicorn -w 4 -k uvicorn.workers.UvicornWorker blog.main:app" ]