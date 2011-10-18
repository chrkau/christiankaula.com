#!/usr/bin/env python

# Copyright (c) 2011, Christian Kaula
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import json
import logging
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


### handling

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
		'date': timestamp.strftime('%c'),
		'text': text,
	})

f = open('tweets.json', 'w', encoding='utf-8')
f.write(json.dumps({'tweets': tweets}))
f.close()

