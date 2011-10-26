title: Subversion: Ignore More
slug: subversion-ignore-more
date: 2009-05-06 14:08
tags: subversion

Just a little reminder for myself, since I never am able to recall how to ignore stuff in Subversion:

You ignore stuff by adding an ignore to the containing directory. Either shorthand per file:

	:::bash
	svn propset svn:ignore somefile .

Or you can edit the properties manually (which I prefer):

	:::bash
	svn propedit svn:ignore .

[Command Line svn:ignore a file](http://blog.bogojoker.com/2008/07/command-line-svnignore-a-file/)
