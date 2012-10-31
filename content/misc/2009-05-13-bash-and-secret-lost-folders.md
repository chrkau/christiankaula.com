title: Bash and the Secret of the Lost Folders
slug: bash-and-secret-lost-folders
date: 2009-05-13 09:17
tags: bash

This bit me majorly yesterday. Nobody tells Bash when the current folder is renamed.

Consider this in a first shell:

	:::bash
	mkdir foo
	cd foo

Now fire up a second shell and do this:

	:::bash
	mv foo foo.old
	mkdir foo
	cd foo
	touch hellothere.txt

Try this in your first shell:

	:::bash
	pwd
	ls

So what do you see? Missing something? Perhaps the *hellothere.txt* file? Well sorry nobody told Bash the folder was renamed. You actually aren't in the new folder but still in the old one which now is called *foo.old*.

If you really want to make sure you actually are in the folder pwd says you are, do this:

	:::bash
	cd `pwd`
