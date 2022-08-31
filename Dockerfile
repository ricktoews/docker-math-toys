FROM python:3.9-alpine

RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
