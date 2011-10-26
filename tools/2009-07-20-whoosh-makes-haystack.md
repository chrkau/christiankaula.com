title: Whoosh makes the Haystack
slug: whoosh-makes-haystack
date: 2009-07-20 13:33
tags: django, whoosh, haystack

In search of a workable search pluggable for Django I played a bit with [Django Sphinx](http://code.google.com/p/django-sphinx/) some time ago. Its potentially nice but involves a lot of work to configure [Sphinx](http://sphinxsearch.com/) itself. So it was difficult enough to configure for me to drop it.

But now with [Haystack](http://haystacksearch.org/) there seems to be a new project that tries to be for search what [South](http://south.aeracode.org/) is for migrations: awesome. 

So since I am working on a major update for this site anyway I thought I'd give it a shot and finally implement a search function. To make a short story even shorter: I was done in about 30 minutes. (That includes almost going crazy because I got no search results and realizing I made a typo...)

What makes the whole thing nice is the fact, that its able to use [Whoosh](http://whoosh.ca/) (which itself is a quite an awesome name already). 'And what the heck is a Woosh?' I hear you ask. Well its a pure Python search engine and should do for most sites that don't have hundreds of megabytes of searchable data. No fiddling with external configs, no extra dependencies.

So if you are still searching for an easy way to integrate search features into your project this might be well worth checking out.
