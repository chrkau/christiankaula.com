title: A Howto on Django Syndication
slug: howto-django-syndication
date: 2009-09-22 10:08
tags: django, syndication

Last week I had to implement a customized RSS feed in Django for the first time. Sounded like a fun project to me until I had a look at the documentation which is… well let's just say it's not as good as the core documentation.

So if anybody runs into the same problems as me here is a simple example on how to do a little customizing of the Django syndication stuff:

:::python
	from django.contrib.syndication.feeds import Feed
	from django.utils.feedgenerator import Rss201rev2Feed
	from content.models import SomeModel


	# this is our very own custom RSS feed generator class
	class FooFeed(Rss201rev2Feed):

		# add_root_elements adds xml elements to the root node of the RSS XML.
		# In this case we add a 'foo' element to our feed root with a value of
		# 'bar'.
		def add_root_elements(self, handler):
			super(FooFeed, self).add_root_elements(handler)
			handler.addQuickElement(u'foo', 'bar')

		# add_item_elements adds elements to the actual items in the RSS XML.
		# In this case we add a 'foz' element with an attribute 'baz'. The values
		# for those two keys are coming out of the passed in item dict.
		def add_item_elements(self, handler, item):
			super(FooFeed, self).add_item_elements(handler, item)
			handler.addQuickElement(u'foz', item['foz'], attrs={'baz': item['baz']})


	# this is our actual feed class that provides data for the RSS feed
	class JobPostingFeed(Feed):
		# this will use our custom RSS feed generator class from above
		feed_type = FooFeed
		title = 'FooFeed stuff'
		link = '/'
		description = 'Freaky FooFeed stuff.'

		# this definies which objects are passed into the feed generator
		def items(self):
			return SomeModel.objects.order_by('-created_at')

		# This took me the most time to figure out even though the idea is pretty
		# simple. We used the item dictionary in add_item_elements above which is
		# filled with the values we define here. Since we are accessing the keys
		# 'foz' and 'baz' above we have to make sure those kyes/values actually
		# exist in the 'item' dict.
		def item_extra_kwargs(self, obj):
			return {
				'foz': obj.some_method(),
				'baz': obj.some_attribute,
			}

_Update: Fixed add_item_elements. Thanks for pointing it out John._
