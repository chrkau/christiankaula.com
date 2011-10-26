title: News from the South
slug: news-south
date: 2009-04-21 15:49
tags: south

Okay this is exciting news. My favorite Django migration tool [South](http://south.aeracode.org/) has received a major update. I just stumbled over some changes to the documentation when I browsing the site the other day. And what did I see? South now does [automatic migrations](http://south.aeracode.org/wiki/Autodetection) now. What does that mean? You don't have to specify what has changed about your models (most of the time) - south is clever enough to find out for itself (again: most of the time).

Furthermore the tool now supports ORM freezing. 'What the heck is that?' I hear you ask. Well imagine the following situation: You have one model and need to change some fields. Now that the fields change you also have to jumble around some data in your migration. Let's say you want to split your name column into first_name and last_name. That means adding two columns, splitting the names and deleting your old column. When you add another column to you model now the migration will fail on another computer because during the name splitting your actual database layout doesn't fit to the models Django is trying to read from the database.

It's actually a bit complicated so I was pleasantly surprised when I found out there is [new documentation](http://south.aeracode.org/wiki/Tutorial3) that describes exactly this case: Changing database layout and manipulating data.

And since there is a [petition on the official django-developers mailing list](http://groups.google.com/group/django-developers/browse_thread/thread/c95dfa1f480c3772) to include South in the core distribution I'm more happy than ever with my choice of migration tool.
