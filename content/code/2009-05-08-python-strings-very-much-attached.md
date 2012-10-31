title: Python - Strings Very Much Attached
slug: python-strings-very-much-attached
date: 2009-05-08 21:04
tags: python

Now this is what you do all the time to strings in Python:

	:::python
	something = 'text'
	print 'some %s' % something

But what if you don't know what you want to insert into a string during programming time? Well then you need the [Python string module](http://docs.python.org/library/string.html). It contains all kinds of [light templating tools](http://docs.python.org/library/string.html#template-strings) which allow you to do this:

	:::python
	import string

	some_text = 'hello $something'
	template = string.Template(some_text)
	print template.substitute(something='world')
