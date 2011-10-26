title: Postgres on Mac Revisted
slug: postgres-on-mac-revisted
date: 2009-02-20 21:33
tags: postgres, mac, macports

Whops seems like I missed to write down that you always have to set up a default database with Postgres before you can do anything else.

	:::bash
	sudo mkdir -p /opt/local/var/db/postgresql83/defaultdb
	sudo chown postgres:postgres /opt/local/var/db/postgresql83/defaultdb
	sudo su postgres -c '/opt/local/lib/postgresql83/bin/initdb -D /opt/local/var/db/postgresql83/defaultdb'

	sudo launchctl load -w /Library/LaunchDaemons/org.macports.postgresql83-server.plist

[Installing Ruby on Rails and PostgreSQL on OS X](http://www.robbyonrails.com/articles/2008/01/22/installing-ruby-on-rails-and-postgresql-on-os-x-third-edition)
