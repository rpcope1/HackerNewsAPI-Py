# HackerNewsAPI
HackerNewsAPI is an unofficial Python implementation of the [Hacker News API](https://github.com/HackerNews/API), that
utilizes the Python requests packages. The package can be installed via

```
    python setup.py install
```

## Usage
An example script (example.py is included). You can get latest story info by doing

```python
from HackerNewsAPI import HackerNewsAPI
api = HackerNewsAPI()
stories = [api.get_item(item_num) for item_num in api.get_top_stories()]
```

Note that the API does have a built in rate-limiter that defaults to 50 milliseconds.
