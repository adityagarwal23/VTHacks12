# syntax=docker/dockerfile:1.4
FROM python

WORKDIR /code

COPY requirements.txt /code
RUN pip install -r requirements.txt

COPY . /code

ENTRYPOINT ["python3"]
CMD ["app.py"]
