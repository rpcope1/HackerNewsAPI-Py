__author__ = 'Robert P. Cope'
import requests
import logging

from utils import rate_limit

hn_logger = logging.getLogger(__name__)
if not hn_logger.handlers:
    ch = logging.StreamHandler()
    hn_logger.addHandler(ch)
    hn_logger.setLevel(logging.INFO)


class HackerNewsAPI(object):
    """
        A simple API for interfacing with the official Hacker News API,
        at https://hacker-news.firebaseio.com, and https://github.com/HackerNews/API
    """

    API_BASE_URL = "https://hacker-news.firebaseio.com"
    WAIT_TIME_MS = 250  # Don't flood the server.

    def __init__(self):
        hn_logger.info('HackerNewsAPI module instantiated.')
        self.session = requests.Session()

    @rate_limit(wait_time=WAIT_TIME_MS)
    def _make_request(self, suburl):
        """
        Helper function for making requests
        :param suburl: The suburl to query
        :return: Decoded json object
        """
        url = "{}/{}".format(self.API_BASE_URL, suburl)
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_item(self, item_number, raw=False):
        """
        Get a dictionary or object with info about the given item number from the Hacker News API.
        Item can be a poll, story, comment or possibly other entry.
        Will raise an requests.HTTPError if we got a non-200 response back. Will raise a ValueError
        if a item_number that can not be converted to int was passed in, or the server has no
        information for that item number.

        (Possible) response parameters:
            "id"        ->  The item's unique id. Required.
            "deleted"   ->	true if the item is deleted.
            "type"      ->	The type of item. One of "job", "story", "comment", "poll", or "pollopt".
            "by"        ->	The username of the item's author.
            "time"      ->	Creation date of the item, in Unix Time.
            "text"      ->	The comment, Ask HN, or poll text. HTML.
            "dead"      ->	true if the item is dead.
            "parent"    ->	The item's parent. For comments, either another comment or the relevant story.
                            For pollopts, the relevant poll.
            "kids"      ->	The ids of the item's comments, in ranked display order.
            "url"       ->	The URL of the story.
            "score"     ->	The story's score, or the votes for a pollopt.
            "title"     ->	The title of the story or poll.
            "parts"     ->	A list of related pollopts, in display order.

        :param item_number: an integer number for the HN item requested
        :param raw: (optional): If true, return the raw decoded JSON dict, if False, return a nice object
                    with keywords as attributes. Default if False.
        :return: A dictionary with relevant info about the item, if successful.
        """
        if not isinstance(item_number, int):
            item_number = int(item_number)
        suburl = "v0/item/{}.json".format(item_number)
        try:
            item_data = self._make_request(suburl)
        except requests.HTTPError as e:
            hn_logger.exception('Faulted on item request for item {}, with status {}'.format(item_number, e.errno))
            raise e
        if not item_data:
            raise ValueError('Item id {} not found!'.format(item_number))
        return item_data if raw else HackerNewsItem(**item_data)

    def get_user(self, user_name, raw=False):
        """
        Get a dictionary or object with info about the given user from the Hacker News API.
        Will raise an requests.HTTPError if we got a non-200 response back.

        Response parameters:
            "id'        ->  The user's unique username. Case-sensitive. Required.
            "delay"     ->	Delay in minutes between a comment's creation and its visibility to other users.
            "created"   ->  Creation date of the user, in Unix Time.
            "karma"     ->	The user's karma.
            "about"     ->	The user's optional self-description. HTML.
            "submitted" ->	List of the user's stories, polls and comments.

        :param user_name: the relevant user's name
        :param raw: (optional): If true, return the raw decoded JSON dict, if False, return a nice object
                    with keywords as attributes. Default if False.
        :return: A dictionary with relevant info about the user, if successful.
        """
        suburl = "v0/user/{}.json".format(user_name)
        try:
            user_data = self._make_request(suburl)
        except requests.HTTPError as e:
            hn_logger.exception('Faulted on item request for user {}, with status {}'.format(user_name, e.errno))
            raise e
        if not user_data:
            raise ValueError('User name {} not found, or no data!'.format(user_name))
        return user_data if raw else HackerNewsUpdates(**user_data)

    def get_top_stories(self):
        """
        Get the item numbers for the current top stories.
        Will raise an requests.HTTPError if we got a non-200 response back.
        :return: A list with the top story item numbers.
        """
        suburl = "v0/topstories.json"
        try:
            top_stories = self._make_request(suburl)
        except requests.HTTPError as e:
            hn_logger.exception('Faulted on getting top stories, with status {}'.format(e.errno))
            raise e
        return top_stories

    def get_max_item(self):
        """
        Get the current maximum item number
        :return: The current maximum item number.
        """
        suburl = "v0/maxitem.json"
        try:
            max_item = self._make_request(suburl)
        except requests.HTTPError as e:
            hn_logger.exception('Faulted on get max item, with status {}'.format(e.errno))
            raise e
        return max_item

    def get_recent_updates(self, raw=True):
        """
        Get the most recent updates on Hacker News

        Response dictionary parameters:
            "items"     ->  A list of the most recently update items by item number.
            "profiles"  ->  A list of most recently updated user profiles by user name.

        :param raw: (optional): If true, return the raw dictionary, if False, return a nice object with attrs for
                    keywords. Default is True.
        :return: A dictionary with relevant info about recent updates.
        """
        suburl = "v0/updates.json"
        try:
            updates_data = self._make_request(suburl)
        except requests.HTTPError as e:
            hn_logger.exception('Faulted on get max item, with status {}'.format(e.errno))
            raise e
        return updates_data if raw else HackerNewsUpdates(**updates_data)


class HackerNewsItem(object):
    def __init__(self, **params):
        self.__dict__.update(params)


class HackerNewsUser(object):
    def __init__(self, **params):
        self.__dict__.update(params)


class HackerNewsUpdates(object):
    def __init__(self, **params):
        self.__dict__.update(params)

if __name__ == "__main__":
    api = HackerNewsAPI()
    print api.get_item(8863, raw=True)