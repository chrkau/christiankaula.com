title: Database Switcheroo
slug: database-switcheroo
date: 2009-01-06 14:56
tags: django, mysql, postgres

Switching the database is quite fun with Django. In my case I'm slowly migrating my sites from MySQL to Postgres.

1. *manage dumpdata* will produce a database independent XML or JSON dump
2. *manage syncdb* will take care of producing a almost empty database skeleton
3. the tables *auth_permission* and *django_content_type* in the database sekelton need to be cleaned completely
4. *manage loaddata* reads the data from the dump and writes it back into the your new database

Rejoice.
