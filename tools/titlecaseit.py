#!/usr/bin/env python
# coding: utf-8

import os
import re
import titlecase
from codecs import open
from titlecase import PUNCT,SMALL, titlecase as tc


SMALL += '|be|am|is|are|being|was|were|been'
titlecase.SMALL_WORDS = re.compile(r'^(%s)$' % SMALL, re.I)
titlecase.SMALL_FIRST = re.compile(r'^([%s]*)(%s)\b' % (PUNCT, SMALL), re.I)
titlecase.SMALL_LAST = re.compile(r'\b(%s)[%s]?$' % (SMALL, PUNCT), re.I)
titlecase.SUBPHRASE = re.compile(r'([:.;?!][ ])(%s)' % SMALL)
DIRS = ('code', 'interface', 'misc', 'projects', 'tools')
BE_WORDS = (u'be', u'am', u'is', u'are', u'being', u'was', u'were', u'been')

TITLELINE_RE = re.compile(r'^title: (.*)$', re.MULTILINE)

def replace(match):
	title = tc(match.group(1))
	title = title.replace(u'...', u'…')
	return u'title: ' + title

for directory in DIRS:
	for dirname, dirnames, filenames in os.walk(directory):
		for filename in filenames:
			if filename.endswith('.md'):
				fl = open(os.path.join(dirname, filename), 'r+', encoding='utf-8')
				content = fl.read()
				content = TITLELINE_RE.sub(replace, content)
				fl.flush()
				fl.seek(0)
				fl.write(content)
				fl.close()

