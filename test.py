# -*- coding: utf-8 -*-
#
# Please refer to AUTHORS.md for a complete list of Copyright holders.
# Copyright (C) 2020-2022 Luis Alejandro Martínez Faneyth.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import time
import datetime
from urllib.request import urlopen
from html import unescape

from atoma import parse_rss_bytes
from tweepy import OAuth1UserHandler, API


count = 0
consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
oauth_token = os.environ.get('TWITTER_OAUTH_TOKEN')
oauth_secret = os.environ.get('TWITTER_OAUTH_SECRET')
feed_url = os.environ.get('FEED_URL')
max_count = int(os.environ.get('MAX_COUNT', 1))
post_lookback = int(os.environ.get('POST_LOOKBACK', 1 * 60 * 60))

if not feed_url:
    raise Exception('No FEED_URL provided.')

auth = OAuth1UserHandler(consumer_key, consumer_secret,
                         oauth_token, oauth_secret)
api = API(auth, wait_on_rate_limit=True)

feed_data = parse_rss_bytes(urlopen(feed_url).read())
today = datetime.datetime.now()
last_run = today - datetime.timedelta(seconds=post_lookback)
last_timestamp = int(last_run.strftime('%Y%m%d%H%M%S'))

for post in feed_data.items:

    item_timestamp = int(post.pub_date.strftime('%Y%m%d%H%M%S'))
    status_text = '{0} {1}'.format(unescape(post.title), post.guid)

    if item_timestamp >= last_timestamp and count <= max_count:
        count += 1
        tweet = api.update_status(status_text)
        time.sleep(10)
        api.destroy_status(tweet.id)
