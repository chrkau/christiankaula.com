title: More Fun With Tracebacks
slug: more-fun-tracebacks
date: 2009-04-30 15:59
tags: python

Okay if you - unlike me - did actually read the [documentation of the Python traceback module](http://docs.python.org/library/traceback.html) you probably know that what I wrote [here](http://christiankaula.com/categories/hints/fun-python-stracktraces/) can be archived much easier if you just do this:

	:::python
	try:
		1 / 0
	except:
		import traceback
		traceback.print_exc()

And if you want to do something with your traceback like send it per mail you can do like so:

	:::python
	try:
		1 / 0
	except:
		import traceback
		import StringIO

		fp = StringIO()
		traceback.print_exc(file=fp)
		print fp.getvalue()
