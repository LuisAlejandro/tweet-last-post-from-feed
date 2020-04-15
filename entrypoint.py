#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import hmac
import random
import base64
import hashlib
from datetime import datetime
from urllib.request import urlopen, Request
from urllib.parse import urlencode

from atoma import parse_rss_bytes

from utils import escape, html_unescape, u, s


TWITTER_API_VERSION = '1.0'
TWITTER_API_METHOD = 'HMAC-SHA1'
TWITTER_API_END = 'https://api.twitter.com/1.1/statuses/update.json'
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
TWITTER_OAUTH_TOKEN = os.environ.get('TWITTER_OAUTH_TOKEN')
TWITTER_OAUTH_SECRET = os.environ.get('TWITTER_OAUTH_SECRET')
FEED_URL = os.environ.get('FEED_URL')
FEED_DATA = parse_rss_bytes(urlopen(FEED_URL).read())

for post in FEED_DATA.items:

    ITEM_TIMESTAMP = int(post.pub_date.strftime('%Y%m%d%H%M%S'))
    LAST_TIMESTAMP = int(datetime.now().strftime('%Y%m%d%H%M%S')) - 10000
    ITEM_TITLE = u(html_unescape(post.title))
    ITEM_LINK = u(post.guid)
    TWITTER_STATUS = ITEM_TITLE+' '+ITEM_LINK

    if ITEM_TIMESTAMP >= LAST_TIMESTAMP:

        SIGNATURE_TIMESTAMP = datetime.now().strftime('%s')
        SIGNATURE_ONCE = base64.b64encode(s(''.join([str(random.randint(0, 9)) for i in range(24)])))
        SIGNATURE_BASE_STRING_AUTH = 'oauth_consumer_key='+escape(TWITTER_CONSUMER_KEY)
        SIGNATURE_BASE_STRING_AUTH += '&oauth_nonce='+escape(SIGNATURE_ONCE)
        SIGNATURE_BASE_STRING_AUTH += '&oauth_signature_method='+escape(TWITTER_API_METHOD)
        SIGNATURE_BASE_STRING_AUTH += '&oauth_timestamp='+escape(SIGNATURE_TIMESTAMP)
        SIGNATURE_BASE_STRING_AUTH += '&oauth_token='+escape(TWITTER_OAUTH_TOKEN)
        SIGNATURE_BASE_STRING_AUTH += '&oauth_version='+escape(TWITTER_API_VERSION)
        SIGNATURE_BASE_STRING_AUTH += '&status='+escape(TWITTER_STATUS)
        SIGNATURE_BASE_STRING = s('POST&'+escape(TWITTER_API_END)+'&'+escape(SIGNATURE_BASE_STRING_AUTH))
        SIGNATURE_KEY = s(escape(TWITTER_CONSUMER_SECRET)+'&'+escape(TWITTER_OAUTH_SECRET))

        OAUTH_HMAC_HASH = hmac.new(SIGNATURE_KEY, SIGNATURE_BASE_STRING, hashlib.sha1)
        OAUTH_SIGNATURE = base64.b64encode(OAUTH_HMAC_HASH.digest())
        OAUTH_HEADER = 'OAuth '
        OAUTH_HEADER += 'oauth_consumer_key="'+escape(TWITTER_CONSUMER_KEY)+'", '
        OAUTH_HEADER += 'oauth_nonce="'+escape(SIGNATURE_ONCE)+'", '
        OAUTH_HEADER += 'oauth_signature="'+escape(OAUTH_SIGNATURE)+'", '
        OAUTH_HEADER += 'oauth_signature_method="'+escape(TWITTER_API_METHOD)+'", '
        OAUTH_HEADER += 'oauth_timestamp="'+escape(SIGNATURE_TIMESTAMP)+'", '
        OAUTH_HEADER += 'oauth_token="'+escape(TWITTER_OAUTH_TOKEN)+'", '
        OAUTH_HEADER += 'oauth_version="'+escape(TWITTER_API_VERSION)+'"'

        HTTP_REQUEST = Request(url=TWITTER_API_END,
                                data=s(urlencode({'status': TWITTER_STATUS})),
                                headers={'Authorization': OAUTH_HEADER,
                                        'Content-Type': 'application/x-www-form-urlencoded'})
        while True:

            RESULT = json.loads(urlopen(HTTP_REQUEST).read())

            if 'errors' not in RESULT:
                break
