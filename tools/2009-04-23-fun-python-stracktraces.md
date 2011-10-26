title: Fun with Python Stracktraces
slug: fun-python-stracktraces
date: 2009-04-23 15:58
tags: python

Today while happily hacking away at my Python code I found myself in the following situation: I needed the traceback of an exception while not wanting the whole app to exit because of the exception being raised.

Turns out there is a [traceback module](http://docs.python.org/library/traceback.html) which in conjunction with the [sys module](http://docs.python.org/library/sys.html) allows to do some neat things with exceptions.

Have a look at this quick and dirty example:

	:::python
	try:
		foo
	
	except NameError:
		import sys, traceback
		print traceback.print_tb(sys.exc_info()[2])

This code actually works and doesn't crash (meaning it doesn't do anything but not crash :P), but still prints a nice little traceback so you know on which line the exception occurred.

All this is very hacky of course - but for debugging purposes its mighty convenient.
