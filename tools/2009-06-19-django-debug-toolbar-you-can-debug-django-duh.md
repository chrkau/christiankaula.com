title: With Django Debug Toolbar you can debug Django... duh
slug: django-debug-toolbar-you-can-debug-django-duh
date: 2009-06-19 09:07
tags: django, performanceoptimization

So since right now I'm playing the performance optimizer again I searched for a nice profiling/debugging tool for Django. Loads of snippets I found, loads of middleware, loads of scripts and stuff. And then a colleague of mine said "you know I always used something called Django debug toolbar or something". I'm like "alright let's google for it and see if it's any good".

The next few minutes I tried to pick up my jaw from the floor again.

This thing is the hot stuff. It does all the stuff you need when hunting for performance eating stuff. Shows you queries, their speed, the templates and their rendering times and a lot more.

There is one problem though: you have to choose between the original version which just works and does the Good Stuff(tm) but looks... let's say functional and a fork that gave me slight problems with jQuery and error pages but is most stylish and has some bells and whistles that are definitely useful (show unique queries and their respective counts especially).

But no matter which you use it will definitely a big boon in your development process.

* [Django Debug Toolbar (original)](http://github.com/robhudson/django-debug-toolbar/tree/master)
* [Django Debug Toolbar (fork)](http://github.com/dcramer/django-debug-toolbar/tree/master)
