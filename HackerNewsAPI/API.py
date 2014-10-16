__author__ = 'Robert P. Cope'
import requests
import logging

hn_logger = logging.getLogger(__name__)
if not hn_logger.handlers:
    ch = logging.StreamHandler()
    hn_logger.addHandler(ch)
    hn_logger.setLevel(logging.INFO)


#TODO: Probably best to have everything get data under one call, to reduce duplicate code.
class HackerNewsAPI(object):
    """
        A simple API for interfacing with the official Hacker News API,
        at https://hacker-news.firebaseio.com, and https://github.com/HackerNews/API
    """

    API_BASE_URL = "https://hacker-news.firebaseio.com"

    def __init__(self):
        hn_logger.info('HackerNewsAPI module instantiated.')
        self.session = requests.Session()

    #TODO: Put an assert on item number being an int.
    def get_item(self, item_number):
        """
        Get a dictionary with info about the given item number from the Hacker News API.
        Item can be a poll, story, comment or possibly other entry.
        Will raise an requests.HTTPError if we got a non-200 response back.

        (Possible) response dictionary parameters:
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
        :return: A dictionary with relevant info about the item, if successful.
        """
        url = "{}/v0/item/{}.json".format(self.API_BASE_URL, item_number)
        response = self.session.get(url)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            hn_logger.exception('Faulted on item request for item {}, with status {}'.format(item_number, e.errno))
            raise e
        return response.json()

    def get_user(self, user_name):
        """
        Get a dictionary with info about the given user from the Hacker News API.
        Will raise an requests.HTTPError if we got a non-200 response back.

        Response dictionary parameters:
            "id'        ->  The user's unique username. Case-sensitive. Required.
            "delay"     ->	Delay in minutes between a comment's creation and its visibility to other users.
            "created"   ->  Creation date of the user, in Unix Time.
            "karma"     ->	The user's karma.
            "about"     ->	The user's optional self-description. HTML.
            "submitted" ->	List of the user's stories, polls and comments.

        :param user_name: the relevant user's name
        :return: A dictionary with relevant info about the user, if successful.
        """
        url = "{}/v0/user/{}.json".format(self.API_BASE_URL, user_name)
        response = self.session.get(url)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            hn_logger.exception('Faulted on item request for user {}, with status {}'.format(user_name, e.errno))
            raise e
        return response.json()

    def get_top_stories(self):
        """
        Get the item numbers for the current top stories.
        Will raise an requests.HTTPError if we got a non-200 response back.
        :return: A list with the top story item numbers.
        """
        url = "{}/v0/user/topstories.json".format(self.API_BASE_URL)
        response = self.session.get(url)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            hn_logger.exception('Faulted on getting top stories, with status {}'.format(e.errno))
            raise e
        return response.json()

    def get_max_item(self):
        """
        Get the current maximum item number
        :return: The current maximum item number.
        """
        url = "{}/v0/user/maxitem.json".format(self.API_BASE_URL)
        response = self.session.get(url)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            hn_logger.exception('Faulted on get max item, with status {}'.format(e.errno))
            raise e
        return response.json()

    def get_recent_updates(self):
        """
        Get the most recent updates on Hacker News

        Response dictionary parameters:
            "items"     ->  A list of the most recently update items by item number.
            "profiles"  ->  A list of most recently updated user profiles by user name.

        :return: A dictionary with relevant info about recent updates.
        """
        url = "{}/v0/user/updates.json".format(self.API_BASE_URL)
        response = self.session.get(url)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            hn_logger.exception('Faulted on get max item, with status {}'.format(e.errno))
            raise e
        return response.json()