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


logging.basicConfig(level=logging.DEBUG)


### fetching

last_id = None
tweet_files = filter(lambda x: x.endswith('json'), os.listdir('tweets'))
if tweet_files:
	logging.info('Seems we have some data already.')
	last_id = sorted(tweet_files)[-1].split('-')[-1][:-5]

params_raw = {
	'include_entities': 'true',
	'include_rts': 'false',
	'trim_user': 'true',
	'screen_name': 'chrkau',
	'count': '200'
}
if last_id:
	params_raw['since_id'] = last_id
	logging.info('Get stuff with id > %s' % last_id)

params = urlencode(params_raw)
fetch_url = 'https://api.twitter.com/1/statuses/user_timeline.json?%s' % params
logging.info('accessing %s' % fetch_url)
urlhandle = urlopen(fetch_url)
data = json.loads(unicode(urlhandle.read()))

if not data:
	logging.info('No new data.')
	sys.exit()


### processing

tweet_ids = []

for tweet in data:
	tweet_ids.append(tweet['id'])

	timestamp = datetime.fromtimestamp(mktime(parsedate(tweet['created_at'])))
	slug = 'tweet-%s' % tweet['id']
	fname = '%s-%s.md' % (
		timestamp.strftime('%Y-%m-%d'),
		tweet['id']
	)
	path = os.path.join('tweets', fname)
	f_out = open(path, 'wa', encoding='utf-8')
	header = 'title: Tweet %s\nslug: %s\ndate: %s' % (
		tweet['id'],
		slug,
		timestamp.strftime('%Y-%m-%d %H:%M')
	)

	#replace shortened urls with expanded ones
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
			u'[%s](%s)' % (url['url'], url_long)
		)

	f_out.write(header)
	f_out.write('\n\n\n%s\n' % text)
	f_out.close()

tweet_file = open('tweets/tweets-%s.json' % max(tweet_ids), 'wa', encoding='utf-8')
tweet_file.write(json.dumps(data))
tweet_file.close()

