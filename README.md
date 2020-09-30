
# Pastebin Indexer

## Installation

You can run the solution in [docker-compose](https://docs.docker.com/compose/install/) or locally.

### docker-compose
After installing compose, cd insights_exercise and run:

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
cd insights_exercise and run:

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

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

