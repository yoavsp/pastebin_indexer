
# Pastebin Indexer
A simple web crawler in Python 3.

The crawler crawls the site: https://pastebin.com/ every 2 minutes and stores the most recent "pastes" in a structured data model.

## Installation

You can run the solution in [docker-compose](https://docs.docker.com/compose/install/) or locally.

### docker-compose
After installing compose, cd pastebin_indexer and run:

```bash
docker-compose up
```
### local
The local solution assumes python 3.8.

Create a virtual environment:

```bash
python3 -m venv /path/to/new/virtual/environment
. /path/to/new/virtual/environment/bin/activate
```
cd pastebin_indexer and run:

```bash
pip install -r requirements.txt
```

Run:

```python
mkdir .env
touch path/to/db/file  #e.g. /tmp/pastedb
echo path/to/db/file > .env/TINYDB_FILE_PATH
```

then run:

```bash
python -m pastebin_indexer.app
``` 

