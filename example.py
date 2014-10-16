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
    print "Title: {}".format(story_data.get('title'))
    print "Submitted by: {}".format(story_data.get('by'))
    print "Url: {}".format(story_data.get('url'))
    print "Id: {}".format(story_data.get('id'))

print "-"*40