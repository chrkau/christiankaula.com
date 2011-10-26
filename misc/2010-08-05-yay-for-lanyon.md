title: Yay for Lanyon
slug: yay-for-lanyon
date: 2010-08-05 16:38
tags: update

Migrated the site to a [Lanyon](http://bitbucket.org/arthurk/lanyon/) based setup today. Really nice little HTML generator - probably because one can sense it was made by a [djangonaut](http://www.arthurkoziel.com/).

Yet there are three things I'm missing:

* A settings file. Why can't I save settings permanently?
* Better tag handling. What's the point of having tags if there isn't a site-wide list of tags I can work with?
* Better datetime parsing. That one I actually took care of already. Might publish that in my own fork soon.

And if one wanted to make Lanyon even more kick-ass here's the thing: Mix it with some [growl](http://github.com/xfire/growl/tree) ideas. I'm thinking per-site hooks and subclasses of the default *Article* class and free-form page metadata. To me that would be the HTML generator to end all HTML generators.