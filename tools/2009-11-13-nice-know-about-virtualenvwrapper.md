title: Nice to Know About Virtualenvwrapper
slug: nice-know-about-virtualenvwrapper
date: 2009-11-13 12:32
tags: django, python, virtualenv, virtualenvwrapper

Since I'm mostly working on various [Django](http://www.djangoproject.com/) projects I am working with [virtualenv](http://pypi.python.org/pypi/virtualenv)/[virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/) a lot. It allows to encapsulate environments and keep them identical across all servers your app will run on.


#### The Problem

All this means setting up pretty much the same Python environment over and over again:

* create an environment
* enter environment
* install [pip](http://pip.openplans.org/)
* install [IPython](http://ipython.scipy.org/moin/)
* install Django
* install [psycopg2](http://pypi.python.org/pypi/psycopg2/2.0.4)
* install [PIL](http://www.pythonware.com/products/pil/)
* install [south](http://south.aeracode.org/)
* install [sorl-thumbnail](http://code.google.com/p/sorl-thumbnail/)
* install [django-compress](http://code.google.com/p/django-compress/)
* install all project specific packages and django apps

Quite tedious after your nth project really.


#### The Solution

After reading [how virtualenv allows bootstrapping environments](http://arthurkoziel.com/2008/10/22/working-virtualenv/) and as such reducing tedious work I wondered if that can be done with virtualenvwrapper, too. Turns its absolutely possible.

There actually are quite a few [hooks in virtualenvwrapper](http://www.doughellmann.com/docs/virtualenvwrapper/hooks.html) that allow for stuff being run pre- and post- creating/deleting/activating environments. Now my *postmkvirtualenv* script looks like this:

	:::bash
	#!/bin/bash

	easy_install pip
	pip install ipython
	pip install yolk
	pip install psycopg2
	pip install django
	pip install -e hg+http://bitbucket.org/andrewgodwin/south/@stableish#egg=south
	pip install pil
	pip install -e svn+http://sorl-thumbnail.googlecode.com/svn/trunk/#egg=solr
	pip install -e svn+http://django-compress.googlecode.com/svn/trunk/#egg=compress

Now whenever I create an environment with *mkvirtualenv someproject* all my standard Python packages and Django apps get installed automagically. And then I'm able to put something like this in my *postactiveate* script:

	:::bash
	#!/bin/bash

	cd /Users/me/Projects/someproject/

So whenever I activate my environment with *workon someproject* I get beamed right into my project dir and can start hacking right away. Nice and easy.
