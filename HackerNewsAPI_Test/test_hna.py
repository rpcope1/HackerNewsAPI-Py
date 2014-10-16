__author__ = 'Robert P. Cope'

import unittest
from HackerNewsAPI import HackerNewsAPI
import time

class HackerNewsAPIBasicTests(unittest.TestCase):
    def test_getitem(self):
        try:
            api = HackerNewsAPI()
            api.get_item(8863)
            api.get_item(8863, raw=True)
            time.sleep(1)  # Delay to ensure no flooding, since API will get respawned.
        except Exception as e:
            self.fail('Faulted with exception {} on get_item for test item 8863'.format(e))

    def test_getuser(self):
        try:
            api = HackerNewsAPI()
            api.get_user('jl')
            api.get_user('jl', raw=True)
            time.sleep(1)
        except Exception as e:
            self.fail('Faulted with exception {} on get_user for user jl'.format(e))

    def test_gettopstories(self):
        try:
            api = HackerNewsAPI()
            api.get_top_stories()
            time.sleep(1)
        except Exception as e:
            self.fail('Faulted with exception {} on get_top_stories'.format(e))

    def test_getmaxitem(self):
        try:
            api = HackerNewsAPI()
            api.get_max_item()
            time.sleep(1)
        except Exception as e:
            self.fail('Faulted with exception {} on get_max_item'.format(e))

    def test_getrecentupdates(self):
        try:
            api = HackerNewsAPI()
            api.get_recent_updates()
            time.sleep(1)
        except Exception as e:
            self.fail('Faulted with exception {} on get_recent_updates'.format(e))

if __name__ == '__main__':
    unittest.main()
