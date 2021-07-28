FROM python:alpine
WORKDIR /app

# Comandos para rodar
RUN apk update && apk add git
RUN git clone https://github.com/sfc-edrd/python-helloworld.git
RUN cp python-helloworld/*.py .
RUN cp python-helloworld/*.txt .
RUN rm -rf python-helloworld
RUN pip install -r requirements.txt

# Default comando
CMD ["python","app.py"]
