title: How to Fix Portage
slug: how-fix-portage
date: 2009-08-14 19:31
tags: gentoo, linux

And all of a sudden I got this on my Gentoo server no matter what I tried to emerge:

	:::console
	# emerge portage
	Calculating dependencies... done!

	>>> Verifying ebuild manifests

	>>> Emerging (1 of 1) sys-apps/portage-2.1.6.13
	[Errno 8] Exec format error:
	   /usr/lib/portage/bin/ebuild /usr/portage/sys-apps/portage/portage-2.1.6.13.ebuild fetch
	 * Fetch failed for 'sys-apps/portage-2.1.6.13', Log file:
	 *  '/var/tmp/portage/sys-apps/portage-2.1.6.13/temp/build.log'

After some fiddling around and searching through Gentoo's Bugzilla I found out that all that was actually needed was this:

	:::console
	# rm /usr/bin/python
	# ln -s /usr/bin/python2.5 /usr/bin/python

(If your portage was built with python 2.4 you should link that of course.)
