title: Going South
slug: going-south
date: 2009-02-10 08:23
tags: django, south

Okay so after taking a few hours to find out how to get a *unique SlugField* into the database per [South](http://south.aeracode.org/) here's what I found out:

Adding the unique index is the last thing South does in a forward migration. That means all you need is a few lines of code after the call to add_field that take care of the empty entries getting unique data that would otherwise violate the unique constraint.


	:::python
	import string
	from random import choice

	def do_stuff():
		chars = string.letters + string.digits
		newpasswd = ''
		for i in range(50):
			newpasswd = newpasswd + choice(chars)
		return newpasswd
	

	class Migration:
    
		def forwards(self):
			# Adding field 'Category.slug'
			db.add_column('forum_category', 'slug', models.SlugField(default='sdf', unique=True), keep_default=False)
			for c in Category.objects.all():
				c.slug = do_stuff()
				c.save()

South is really neat - once you figured out how it works.
