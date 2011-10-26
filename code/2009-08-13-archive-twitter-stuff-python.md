title: Archive Twitter Stuff With Python
slug: archive-twitter-stuff-python
date: 2009-08-13 08:49
tags: twitter, python

Just read [this article](http://morethanseven.net/2007/11/23/archiving-twitter-data-with-python/) which gives a description on how to archive Twitter stuff with Python. I saw the code and thought 'heck why so complicated?'.

Get [python-twitter](http://code.google.com/p/python-twitter/) and do like so: 

	:::python
	import twitter

	api = twitter.Api()

	statuses = api.GetUserTimeline('twitter', count=1000000)
	f = open('twitter.txt', 'w')

	for s in statuses:
	    f.write(s.created_at + '\n' + s.text.encode('utf8') + '\n\n')

This code will get the last million posts of the user *twitter* and write it to the file *twitter.txt* in the same directory as the script itself lies in. If your username should not be *twitter* or if you have more than a million posts you might want to change those values (and in the latter case consider getting professional help).
title: Archive Twitter Stuff With Python
slug: archive-twitter-stuff-python
date: 2009-08-13 08:49
tags: twitter, python

Just read [this article](http://morethanseven.net/2007/11/23/archiving-twitter-data-with-python/) which gives a description on how to archive Twitter stuff with Python. I saw the code and thought 'heck why so complicated?'.

Get [python-twitter](http://code.google.com/p/python-twitter/) and do like so: 

	:::python
	import twitter

	api = twitter.Api()

	statuses = api.GetUserTimeline('twitter', count=1000000)
	f = open('twitter.txt', 'w')

	for s in statuses:
	    f.write(s.created_at + '\n' + s.text.encode('utf8') + '\n\n')

This code will get the last million posts of the user *twitter* and write it to the file *twitter.txt* in the same directory as the script itself lies in. If your username should not be *twitter* or if you have more than a million posts you might want to change those values (and in the latter case consider getting professional help).
title: Archive Twitter Stuff With Python
slug: archive-twitter-stuff-python
date: 2009-08-13 08:49
tags: twitter, python

Just read [this article](http://morethanseven.net/2007/11/23/archiving-twitter-data-with-python/) which gives a description on how to archive Twitter stuff with Python. I saw the code and thought 'heck why so complicated?'.

Get [python-twitter](http://code.google.com/p/python-twitter/) and do like so: 

	:::python
	import twitter

	api = twitter.Api()

	statuses = api.GetUserTimeline('twitter', count=1000000)
	f = open('twitter.txt', 'w')

	for s in statuses:
	    f.write(s.created_at + '\n' + s.text.encode('utf8') + '\n\n')

This code will get the last million posts of the user *twitter* and write it to the file *twitter.txt* in the same directory as the script itself lies in. If your username should not be *twitter* or if you have more than a million posts you might want to change those values (and in the latter case consider getting professional help).
title: Archive Twitter Stuff With Python
slug: archive-twitter-stuff-python
date: 2009-08-13 08:49
tags: twitter, python

Just read [this article](http://morethanseven.net/2007/11/23/archiving-twitter-data-with-python/) which gives a description on how to archive Twitter stuff with Python. I saw the code and thought 'heck why so complicated?'.

Get [python-twitter](http://code.google.com/p/python-twitter/) and do like so: 

	:::python
	import twitter

	api = twitter.Api()

	statuses = api.GetUserTimeline('twitter', count=1000000)
	f = open('twitter.txt', 'w')

	for s in statuses:
	    f.write(s.created_at + '\n' + s.text.encode('utf8') + '\n\n')

This code will get the last million posts of the user *twitter* and write it to the file *twitter.txt* in the same directory as the script itself lies in. If your username should not be *twitter* or if you have more than a million posts you might want to change those values (and in the latter case consider getting professional help).
title: Archive Twitter Stuff With Python
slug: archive-twitter-stuff-python
date: 2009-08-13 08:49
tags: twitter, python

Just read [this article](http://morethanseven.net/2007/11/23/archiving-twitter-data-with-python/) which gives a description on how to archive Twitter stuff with Python. I saw the code and thought 'heck why so complicated?'.

Get [python-twitter](http://code.google.com/p/python-twitter/) and do like so: 

	:::python
	import twitter

	api = twitter.Api()

	statuses = api.GetUserTimeline('twitter', count=1000000)
	f = open('twitter.txt', 'w')

	for s in statuses:
	    f.write(s.created_at + '\n' + s.text.encode('utf8') + '\n\n')

This code will get the last million posts of the user *twitter* and write it to the file *twitter.txt* in the same directory as the script itself lies in. If your username should not be *twitter* or if you have more than a million posts you might want to change those values (and in the latter case consider getting professional help).
title: Archive Twitter Stuff With Python
slug: archive-twitter-stuff-python
date: 2009-08-13 08:49
tags: twitter, python

Just read [this article](http://morethanseven.net/2007/11/23/archiving-twitter-data-with-python/) which gives a description on how to archive Twitter stuff with Python. I saw the code and thought 'heck why so complicated?'.

Get [python-twitter](http://code.google.com/p/python-twitter/) and do like so: 

	:::python
	import twitter

	api = twitter.Api()

	statuses = api.GetUserTimeline('twitter', count=1000000)
	f = open('twitter.txt', 'w')

	for s in statuses:
	    f.write(s.created_at + '\n' + s.text.encode('utf8') + '\n\n')

This code will get the last million posts of the user *twitter* and write it to the file *twitter.txt* in the same directory as the script itself lies in. If your username should not be *twitter* or if you have more than a million posts you might want to change those values (and in the latter case consider getting professional help).
title: Archive Twitter Stuff With Python
slug: archive-twitter-stuff-python
date: 2009-08-13 08:49
tags: twitter, python

Just read [this article](http://morethanseven.net/2007/11/23/archiving-twitter-data-with-python/) which gives a description on how to archive Twitter stuff with Python. I saw the code and thought 'heck why so complicated?'.

Get [python-twitter](http://code.google.com/p/python-twitter/) and do like so: 

	:::python
	import twitter

	api = twitter.Api()

	statuses = api.GetUserTimeline('twitter', count=1000000)
	f = open('twitter.txt', 'w')

	for s in statuses:
	    f.write(s.created_at + '\n' + s.text.encode('utf8') + '\n\n')

This code will get the last million posts of the user *twitter* and write it to the file *twitter.txt* in the same directory as the script itself lies in. If your username should not be *twitter* or if you have more than a million posts you might want to change those values (and in the latter case consider getting professional help).
title: Archive Twitter Stuff With Python
slug: archive-twitter-stuff-python
date: 2009-08-13 08:49
tags: twitter, python

Just read [this article](http://morethanseven.net/2007/11/23/archiving-twitter-data-with-python/) which gives a description on how to archive Twitter stuff with Python. I saw the code and thought 'heck why so complicated?'.

Get [python-twitter](http://code.google.com/p/python-twitter/) and do like so: 

	:::python
	import twitter

	api = twitter.Api()

	statuses = api.GetUserTimeline('twitter', count=1000000)
	f = open('twitter.txt', 'w')

	for s in statuses:
	    f.write(s.created_at + '\n' + s.text.encode('utf8') + '\n\n')

This code will get the last million posts of the user *twitter* and write it to the file *twitter.txt* in the same directory as the script itself lies in. If your username should not be *twitter* or if you have more than a million posts you might want to change those values (and in the latter case consider getting professional help).
