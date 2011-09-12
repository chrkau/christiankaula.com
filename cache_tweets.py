#!/usr/bin/env python

import json
import logging
import os
import sys
from codecs import open
from datetime import datetime
from rfc822 import parsedate
from time import mktime
from urllib import urlencode, urlopen


#logging.basicConfig(level=logging.DEBUG)


### fetching

params_raw = {
	'include_entities': 'true',
	'include_rts': 'false',
	'trim_user': 'true',
	'screen_name': 'chrkau',
	'count': '100'
}
params = urlencode(params_raw)

fetch_url = 'https://api.twitter.com/1/statuses/user_timeline.json?%s' % params
logging.info('accessing %s' % fetch_url)
urlhandle = urlopen(fetch_url)
data = json.loads(unicode(urlhandle.read()))
print(len(data))

tweets = []
for tweet in data[:4]:
	timestamp = datetime.fromtimestamp(mktime(parsedate(tweet['created_at'])))
	text = tweet['text']

	for url in tweet['entities']['urls']:
		if url['expanded_url']:
			url_long = url['expanded_url']
		else:
			url_long = url['url']
		logging.info('Replacing %s with %s.' % (
			url['url'], url_long))
		text = text.replace(
			url['url'],
			u'<a href="%s">%s</a>' % (url_long, url['url'])
		)

	tweets.append({
		# 'date': timestamp.strftime('%Y-%m-%d %H:%M'),
		'date': timestamp.strftime('%c'),
		'text': text,
	})

f = open('tweets.json', 'w', encoding='utf-8')
f.write(json.dumps({'tweets': tweets}))
f.close()

