FROM python:latest

LABEL key="Jose_Rodriguez"

WORKDIR /app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./ /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
