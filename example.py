__author__ = 'Robert P. Cope'

#
#   Hacker News API Example Script
#   - Displays most recent stories with info.
#

from HackerNewsAPI import HackerNewsAPI
import logging

root_logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
root_logger.addHandler(console_handler)

hn_api = HackerNewsAPI()
print "-"*40
print "\tHacker News Top Stories"
print "-"*40
print
for item_num in hn_api.get_top_stories():
    story_data = hn_api.get_item(item_num)
    print u"Title: {}".format(story_data.title)
    print u"Submitted by: {}".format(story_data.by)
    print u"Url: {}".format(story_data.url)
    print u"Id: {}".format(story_data.id)

print "-"*40