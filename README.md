[![Circle CI](https://circleci.com/gh/rpcope1/HackerNewsAPI-Py.png?style=badge)](https://circleci.com/gh/rpcope1/HackerNewsAPI-Py)
[![PyPI version](https://badge.fury.io/py/HackerNewsAPI.svg)](http://badge.fury.io/py/HackerNewsAPI)
# HackerNewsAPI
HackerNewsAPI is an unofficial Python implementation of the [Hacker News API](https://github.com/HackerNews/API), that
utilizes the Python requests packages. The package can be installed via

```
    python setup.py install
```

or via

```
    pip install HackerNewsAPI
```

## Usage
An example script (example.py is included). You can get latest story info by doing

```python
from HackerNewsAPI import HackerNewsAPI
api = HackerNewsAPI()
stories = [api.get_item(item_num) for item_num in api.get_top_stories()]
```

Note that the API does have a built in rate-limiter that defaults to 250 milliseconds.
Tests are run by calling
```
python HackerNewsAPI_Test
```