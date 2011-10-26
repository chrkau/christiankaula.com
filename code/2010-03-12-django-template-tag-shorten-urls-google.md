title: Django Template Tag to Shorten URLs Like Google
slug: django-template-tag-shorten-urls-google
date: 2010-03-12 22:22
tags: django, python

Need to shorten your URLs like Google does? Something like http://example.com/some/really/long/path/ to http://example.com/.../path/? Here's my simplistic approach:

	:::python
	# -*- encoding: utf-8 -*-

	from django import template
	from django.utils.html import conditional_escape
	from django.utils.safestring import mark_safe
	import re


	register = template.Library()


	@register.filter
	def fancyurlize(value, arg):
		length = int(arg)

		text = value
		for char in (u'%', u'?'):
			arr = value.split(char)
			if len(arr) > 1:
				text = arr[0]

		if len(text) > length:
			arr = re.split(r'(?<!/)/(?!/)', text)
			if len(arr) > 2:
				text = u'/'.join((arr[0], u'...', arr[-1]))

		if len(text) > 0 and text[-1] != u'/':
			text = u''.join((text, u'/'))

		return_value = u'<a href="%s" target="_blank">%s</a>' % (
			conditional_escape(value),
			conditional_escape(text),
		)
		return mark_safe(return_value)

	fancyurlize.is_safe = True
title: Django Template Tag to Shorten URLs Like Google
slug: django-template-tag-shorten-urls-google
date: 2010-03-12 22:22
tags: django, python

Need to shorten your URLs like Google does? Something like http://example.com/some/really/long/path/ to http://example.com/.../path/? Here's my simplistic approach:

	:::python
	# -*- encoding: utf-8 -*-

	from django import template
	from django.utils.html import conditional_escape
	from django.utils.safestring import mark_safe
	import re


	register = template.Library()


	@register.filter
	def fancyurlize(value, arg):
		length = int(arg)

		text = value
		for char in (u'%', u'?'):
			arr = value.split(char)
			if len(arr) > 1:
				text = arr[0]

		if len(text) > length:
			arr = re.split(r'(?<!/)/(?!/)', text)
			if len(arr) > 2:
				text = u'/'.join((arr[0], u'...', arr[-1]))

		if len(text) > 0 and text[-1] != u'/':
			text = u''.join((text, u'/'))

		return_value = u'<a href="%s" target="_blank">%s</a>' % (
			conditional_escape(value),
			conditional_escape(text),
		)
		return mark_safe(return_value)

	fancyurlize.is_safe = True
title: Django Template Tag to Shorten URLs Like Google
slug: django-template-tag-shorten-urls-google
date: 2010-03-12 22:22
tags: django, python

Need to shorten your URLs like Google does? Something like http://example.com/some/really/long/path/ to http://example.com/.../path/? Here's my simplistic approach:

	:::python
	# -*- encoding: utf-8 -*-

	from django import template
	from django.utils.html import conditional_escape
	from django.utils.safestring import mark_safe
	import re


	register = template.Library()


	@register.filter
	def fancyurlize(value, arg):
		length = int(arg)

		text = value
		for char in (u'%', u'?'):
			arr = value.split(char)
			if len(arr) > 1:
				text = arr[0]

		if len(text) > length:
			arr = re.split(r'(?<!/)/(?!/)', text)
			if len(arr) > 2:
				text = u'/'.join((arr[0], u'...', arr[-1]))

		if len(text) > 0 and text[-1] != u'/':
			text = u''.join((text, u'/'))

		return_value = u'<a href="%s" target="_blank">%s</a>' % (
			conditional_escape(value),
			conditional_escape(text),
		)
		return mark_safe(return_value)

	fancyurlize.is_safe = True
title: Django Template Tag to Shorten URLs Like Google
slug: django-template-tag-shorten-urls-google
date: 2010-03-12 22:22
tags: django, python

Need to shorten your URLs like Google does? Something like http://example.com/some/really/long/path/ to http://example.com/.../path/? Here's my simplistic approach:

	:::python
	# -*- encoding: utf-8 -*-

	from django import template
	from django.utils.html import conditional_escape
	from django.utils.safestring import mark_safe
	import re


	register = template.Library()


	@register.filter
	def fancyurlize(value, arg):
		length = int(arg)

		text = value
		for char in (u'%', u'?'):
			arr = value.split(char)
			if len(arr) > 1:
				text = arr[0]

		if len(text) > length:
			arr = re.split(r'(?<!/)/(?!/)', text)
			if len(arr) > 2:
				text = u'/'.join((arr[0], u'...', arr[-1]))

		if len(text) > 0 and text[-1] != u'/':
			text = u''.join((text, u'/'))

		return_value = u'<a href="%s" target="_blank">%s</a>' % (
			conditional_escape(value),
			conditional_escape(text),
		)
		return mark_safe(return_value)

	fancyurlize.is_safe = True
title: Django Template Tag to Shorten URLs Like Google
slug: django-template-tag-shorten-urls-google
date: 2010-03-12 22:22
tags: django, python

Need to shorten your URLs like Google does? Something like http://example.com/some/really/long/path/ to http://example.com/.../path/? Here's my simplistic approach:

	:::python
	# -*- encoding: utf-8 -*-

	from django import template
	from django.utils.html import conditional_escape
	from django.utils.safestring import mark_safe
	import re


	register = template.Library()


	@register.filter
	def fancyurlize(value, arg):
		length = int(arg)

		text = value
		for char in (u'%', u'?'):
			arr = value.split(char)
			if len(arr) > 1:
				text = arr[0]

		if len(text) > length:
			arr = re.split(r'(?<!/)/(?!/)', text)
			if len(arr) > 2:
				text = u'/'.join((arr[0], u'...', arr[-1]))

		if len(text) > 0 and text[-1] != u'/':
			text = u''.join((text, u'/'))

		return_value = u'<a href="%s" target="_blank">%s</a>' % (
			conditional_escape(value),
			conditional_escape(text),
		)
		return mark_safe(return_value)

	fancyurlize.is_safe = True
title: Django Template Tag to Shorten URLs Like Google
slug: django-template-tag-shorten-urls-google
date: 2010-03-12 22:22
tags: django, python

Need to shorten your URLs like Google does? Something like http://example.com/some/really/long/path/ to http://example.com/.../path/? Here's my simplistic approach:

	:::python
	# -*- encoding: utf-8 -*-

	from django import template
	from django.utils.html import conditional_escape
	from django.utils.safestring import mark_safe
	import re


	register = template.Library()


	@register.filter
	def fancyurlize(value, arg):
		length = int(arg)

		text = value
		for char in (u'%', u'?'):
			arr = value.split(char)
			if len(arr) > 1:
				text = arr[0]

		if len(text) > length:
			arr = re.split(r'(?<!/)/(?!/)', text)
			if len(arr) > 2:
				text = u'/'.join((arr[0], u'...', arr[-1]))

		if len(text) > 0 and text[-1] != u'/':
			text = u''.join((text, u'/'))

		return_value = u'<a href="%s" target="_blank">%s</a>' % (
			conditional_escape(value),
			conditional_escape(text),
		)
		return mark_safe(return_value)

	fancyurlize.is_safe = True
title: Django Template Tag to Shorten URLs Like Google
slug: django-template-tag-shorten-urls-google
date: 2010-03-12 22:22
tags: django, python

Need to shorten your URLs like Google does? Something like http://example.com/some/really/long/path/ to http://example.com/.../path/? Here's my simplistic approach:

	:::python
	# -*- encoding: utf-8 -*-

	from django import template
	from django.utils.html import conditional_escape
	from django.utils.safestring import mark_safe
	import re


	register = template.Library()


	@register.filter
	def fancyurlize(value, arg):
		length = int(arg)

		text = value
		for char in (u'%', u'?'):
			arr = value.split(char)
			if len(arr) > 1:
				text = arr[0]

		if len(text) > length:
			arr = re.split(r'(?<!/)/(?!/)', text)
			if len(arr) > 2:
				text = u'/'.join((arr[0], u'...', arr[-1]))

		if len(text) > 0 and text[-1] != u'/':
			text = u''.join((text, u'/'))

		return_value = u'<a href="%s" target="_blank">%s</a>' % (
			conditional_escape(value),
			conditional_escape(text),
		)
		return mark_safe(return_value)

	fancyurlize.is_safe = True
title: Django Template Tag to Shorten URLs Like Google
slug: django-template-tag-shorten-urls-google
date: 2010-03-12 22:22
tags: django, python

Need to shorten your URLs like Google does? Something like http://example.com/some/really/long/path/ to http://example.com/.../path/? Here's my simplistic approach:

	:::python
	# -*- encoding: utf-8 -*-

	from django import template
	from django.utils.html import conditional_escape
	from django.utils.safestring import mark_safe
	import re


	register = template.Library()


	@register.filter
	def fancyurlize(value, arg):
		length = int(arg)

		text = value
		for char in (u'%', u'?'):
			arr = value.split(char)
			if len(arr) > 1:
				text = arr[0]

		if len(text) > length:
			arr = re.split(r'(?<!/)/(?!/)', text)
			if len(arr) > 2:
				text = u'/'.join((arr[0], u'...', arr[-1]))

		if len(text) > 0 and text[-1] != u'/':
			text = u''.join((text, u'/'))

		return_value = u'<a href="%s" target="_blank">%s</a>' % (
			conditional_escape(value),
			conditional_escape(text),
		)
		return mark_safe(return_value)

	fancyurlize.is_safe = True
