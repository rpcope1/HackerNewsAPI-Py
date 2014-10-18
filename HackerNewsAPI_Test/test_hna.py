__author__ = 'Robert P. Cope'

import unittest
from HackerNewsAPI import HackerNewsAPI
import time
import traceback

from expected_data import *

class HackerNewsAPIBasicTests(unittest.TestCase):
    def test_getitem(self):
        try:
            api = HackerNewsAPI()
            assert api.get_item(8863) is not None
            time.sleep(1)
            data_8863 = api.get_item(8863, raw=True)
            assert data_8863
            check_content(data_8863, story_8863, ["by", "id", "time", "title", "type", "url"])
            time.sleep(1)  # Delay to ensure no flooding, since API will get respawned.
        except Exception as e:
            traceback.print_exc()
            self.fail("Faulted with exception '{}' on get_item for test item 8863".format(e))

    def test_getitem_fault(self):
        try:
            api = HackerNewsAPI()
            self.assertRaises(ValueError, api.get_item, 'notanumber')
            self.assertRaises(ValueError, api.get_item, -1)
            time.sleep(1)  # Delay to ensure no flooding, since API will get respawned.
        except Exception as e:
            traceback.print_exc()
            self.fail("Faulted with incorrect exception '{}' on get_item for garbage test items".format(e))

    def test_getuser(self):
        try:
            api = HackerNewsAPI()
            assert api.get_user('jl') is not None
            time.sleep(1)
            data_jl = api.get_user('jl', raw=True)
            assert data_jl
            check_content(data_jl, user_jl, ["created", "id", "delay"])
            time.sleep(1)
        except Exception as e:
            traceback.print_exc()
            self.fail("Faulted with exception '{}' on get_user for user jl".format(e))

    def test_getuser_fault(self):
        try:
            api = HackerNewsAPI()
            self.assertRaises(ValueError, api.get_user, 'NOTAREALUSERREALLYNOTAREALUSER')
            time.sleep(1)
        except Exception as e:
            traceback.print_exc()
            self.fail("Faulted with incorrect exception '{}' on get_item for garbage test user".format(e))


    def test_gettopstories(self):
        try:
            api = HackerNewsAPI()
            assert api.get_top_stories() is not None
            time.sleep(1)
        except Exception as e:
            traceback.print_exc()
            self.fail("Faulted with exception '{}' on get_top_stories".format(e))

    def test_getmaxitem(self):
        try:
            api = HackerNewsAPI()
            assert api.get_max_item() is not None
            time.sleep(1)
        except Exception as e:
            traceback.print_exc()
            self.fail("Faulted with exception '{}' on get_max_item".format(e))

    def test_getrecentupdates(self):
        try:
            api = HackerNewsAPI()
            assert api.get_recent_updates() is not None
            time.sleep(1)
        except Exception as e:
            traceback.print_exc()
            self.fail("Faulted with exception '{}' on get_recent_updates".format(e))

if __name__ == '__main__':
    unittest.main()
