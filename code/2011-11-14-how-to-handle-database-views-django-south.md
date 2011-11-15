title: How to Handle Database Views in Django/South
slug: how-to-handle-database-views-django-south
date: 2011-11-14 19:43
tags: database, django, postgres
description: My simplistic take on database view handling in Django/South.

In a recent Django project I had to work with Postgres views quite extensively. The problem is that while [South](http://south.aeracode.org/) does a great job handling model related stuff, you’re on your own when handling views and other database level stuff. So I thought I’d share the simple/simplistic solution I came up with.


## Hand written migrations

Since South doesn’t provide much help in writing views for you, you will write your migrations by hand. So let’s add a dandy new view to our database.

	:::python
	# migration 0001
	# (…) imports and such

	class Migration(SchemaMigration):

    def forwards(self, orm):
        query = """
			CREATE VIEW fancy_view AS
			SELECT aCol, bCol
			FROM stuff
			;
		"""
		db.execute(query)
	
	def backwards(self, orm):
        query = """
			DROP VIEW fancy_view;
		"""
		db.execute(query)

	# (…) loads of frozen models

Now that wasn’t too bad, right? Oh, but now we forgot all about *cCol*. No sweat, let’s just write another migration to fix that.

	:::python
	# migration 0002
	# (…) imports and such

	class Migration(SchemaMigration):

    def forwards(self, orm):
        query = """
			DROP VIEW fancy_view;
		"""
		db.execute(query)
        query = """
			DROP VIEW fancy_view;
			CREATE VIEW fancy_view AS
			SELECT aCol, bCol, cCol
			FROM stuff
			;
		"""
		db.execute(query)
	
	def backwards(self, orm):
        query = """
			DROP VIEW fancy_view;
		"""
        query = """
			CREATE VIEW fancy_view AS
			SELECT acol, bcol
			FROM stuff
			;
		"""
		db.execute(query)

	# loads of frozen models (…)

Okay, that kinda sucks. Now we have to repeat the forward SQL part of migration 0001 in the backwards part of migration 0002.


## What about dependent views?

And the above example didn’t mention views that depend on each other. Let’s say we have two views, *fancy_view* and *depending_view*. The drill would look something like this:

1. Write migration 0001 for *fancy_view*.
2. Find out you need *depending_view* which depends on *fancy_view* because it joins in some stuff from there.
3. Write migration 0002 for *depending_view*.
4. Find out you need to change something in *fancy_view*.
5. Write migration 0003 which takes care of this:
	1. Drop *fancy_view* and all that depends on it.
	2. Recreate *fancy_view* with changes.
	3. Recreate *depending_view*.
	4. Does the same stuff migration 0002 does in *forwards* in *backwards*.

This is anything but simple anymore and as such prone to error. Sure you can do a lot with copy and paste but it’s really easy to make mistakes there. (Trust me on that one…)


## Why can’t my computer do that for me?

Here’s what I came up with: I put my views in SQL files named after the migration they occur in. So for migration *0001_add_fancy_view.py* there could be a *0001_fancy_view.sql* and a *0001_other_fancy_view.sql*.

So let’s assume the situation described above: In migration 0002 we added a view named *depending_view* that somehow depends on *fancy_view* which was introduced in migration 0001. Now in migration 0003 we want to change something in *fancy_view*. For that we have to drop *fancy_view* and everything that depends on it and build it up from the ground again.

This is what that migration could look like:

	:::python
	# 0003_change_fancy_view.py
	# (…) imports and such

	def run_file(file_name):
		import os
		f = open(os.path.join(os.path.dirname(__file__), file_name))
		query = f.read()
		db.execute(query)

	class Migration(SchemaMigration):
		def forwards(self, orm):
			# get rid of fancy_view and all depending views
			db.execute("DROP VIEW fancy_view CASCADE;")
			# update fancy_view
			run_file('0003_fancy_view.sql')
			# re-add depending_view
			run_file('0002_depending_view.sql')

		def backwards(self, orm):
			# get rid of fancy_view and all depending views
			db.execute("DROP VIEW fancy_view CASCADE;")
			# re-add the old version of fancy view
			run_file('0001_fancy_view.sql')
			# re-add depending_view
			run_file('0002_depending_view.sql')

	# (…) loads of frozen models

Much nicer, in my humble opinion. We let the computer handle most of the boring parts and concentrate only on the order that things should be handled in. Sure there’s loads of room for improvement but it gets the job done.
