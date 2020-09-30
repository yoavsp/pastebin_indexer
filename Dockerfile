FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD pastebin_indexer pastebin_indexer

CMD [ "python", "-m", "pastebin_indexer.app"]