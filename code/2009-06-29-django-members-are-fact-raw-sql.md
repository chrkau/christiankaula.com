title: Django Members That are in Fact Raw SQL
slug: django-members-are-fact-raw-sql
date: 2009-06-29 08:32
tags: django, sql

So the other day I wondered if it wasn't pretty cool if Django models would have something like members that are in fact raw queries. On the bus home it occurred to me that this functionality already exists. Just add a custom manager to a model which always returns querysets with extras.

Something like this (not tested so don't complain if it contains errors):

	:::python
	from django.db import models


	class SomeManager(models.Manager):
		def get_query_set(self):
			return super(SomeManager, self).get_query_set().extra(
				select={'somecount': '''
					SELECT COUNT(*)
					FROM someapp_somemodel
				''',}
			)


	class SomeModel(models.Model):
		objects = SomeManager()
		...
