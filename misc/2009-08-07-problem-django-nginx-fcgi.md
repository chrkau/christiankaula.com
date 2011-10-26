title: The Problem With Django, Nginx and FCGI
slug: problem-django-nginx-fcgi
date: 2009-08-07 01:49
tags: django, nginx, fcgi

Alright after about a whole day of near-continuous downtime I finally found the bug that I overcame few months ago already. I'm using [nginx](http://nginx.net/) as proxy to Django per FCGI. Now after upgrading nginx the site started to misbehave. No matter which location I tried to access I always ended up on the index page.

So after loads of trial and error I came to the conclusion that the problem is in the *fastcgi_params* file. Consider this line:

	:::nginx
	fastcgi_param  SCRIPT_NAME  $fastcgi_script_name;

What Django expects is not *SCRIPT_NAME* but *PATH_INFO*:

	:::nginx
	fastcgi_param  PATH_INFO  $fastcgi_script_name;

So in case you ever wonder why your Django app only shows you the index page no matter which URL you try to access this might just have to do with the FCGI params.
title: The Problem With Django, Nginx and FCGI
slug: problem-django-nginx-fcgi
date: 2009-08-07 01:49
tags: django, nginx, fcgi

Alright after about a whole day of near-continuous downtime I finally found the bug that I overcame few months ago already. I'm using [nginx](http://nginx.net/) as proxy to Django per FCGI. Now after upgrading nginx the site started to misbehave. No matter which location I tried to access I always ended up on the index page.

So after loads of trial and error I came to the conclusion that the problem is in the *fastcgi_params* file. Consider this line:

	:::nginx
	fastcgi_param  SCRIPT_NAME  $fastcgi_script_name;

What Django expects is not *SCRIPT_NAME* but *PATH_INFO*:

	:::nginx
	fastcgi_param  PATH_INFO  $fastcgi_script_name;

So in case you ever wonder why your Django app only shows you the index page no matter which URL you try to access this might just have to do with the FCGI params.
title: The Problem With Django, Nginx and FCGI
slug: problem-django-nginx-fcgi
date: 2009-08-07 01:49
tags: django, nginx, fcgi

Alright after about a whole day of near-continuous downtime I finally found the bug that I overcame few months ago already. I'm using [nginx](http://nginx.net/) as proxy to Django per FCGI. Now after upgrading nginx the site started to misbehave. No matter which location I tried to access I always ended up on the index page.

So after loads of trial and error I came to the conclusion that the problem is in the *fastcgi_params* file. Consider this line:

	:::nginx
	fastcgi_param  SCRIPT_NAME  $fastcgi_script_name;

What Django expects is not *SCRIPT_NAME* but *PATH_INFO*:

	:::nginx
	fastcgi_param  PATH_INFO  $fastcgi_script_name;

So in case you ever wonder why your Django app only shows you the index page no matter which URL you try to access this might just have to do with the FCGI params.
title: The Problem With Django, Nginx and FCGI
slug: problem-django-nginx-fcgi
date: 2009-08-07 01:49
tags: django, nginx, fcgi

Alright after about a whole day of near-continuous downtime I finally found the bug that I overcame few months ago already. I'm using [nginx](http://nginx.net/) as proxy to Django per FCGI. Now after upgrading nginx the site started to misbehave. No matter which location I tried to access I always ended up on the index page.

So after loads of trial and error I came to the conclusion that the problem is in the *fastcgi_params* file. Consider this line:

	:::nginx
	fastcgi_param  SCRIPT_NAME  $fastcgi_script_name;

What Django expects is not *SCRIPT_NAME* but *PATH_INFO*:

	:::nginx
	fastcgi_param  PATH_INFO  $fastcgi_script_name;

So in case you ever wonder why your Django app only shows you the index page no matter which URL you try to access this might just have to do with the FCGI params.
title: The Problem With Django, Nginx and FCGI
slug: problem-django-nginx-fcgi
date: 2009-08-07 01:49
tags: django, nginx, fcgi

Alright after about a whole day of near-continuous downtime I finally found the bug that I overcame few months ago already. I'm using [nginx](http://nginx.net/) as proxy to Django per FCGI. Now after upgrading nginx the site started to misbehave. No matter which location I tried to access I always ended up on the index page.

So after loads of trial and error I came to the conclusion that the problem is in the *fastcgi_params* file. Consider this line:

	:::nginx
	fastcgi_param  SCRIPT_NAME  $fastcgi_script_name;

What Django expects is not *SCRIPT_NAME* but *PATH_INFO*:

	:::nginx
	fastcgi_param  PATH_INFO  $fastcgi_script_name;

So in case you ever wonder why your Django app only shows you the index page no matter which URL you try to access this might just have to do with the FCGI params.
title: The Problem With Django, Nginx and FCGI
slug: problem-django-nginx-fcgi
date: 2009-08-07 01:49
tags: django, nginx, fcgi

Alright after about a whole day of near-continuous downtime I finally found the bug that I overcame few months ago already. I'm using [nginx](http://nginx.net/) as proxy to Django per FCGI. Now after upgrading nginx the site started to misbehave. No matter which location I tried to access I always ended up on the index page.

So after loads of trial and error I came to the conclusion that the problem is in the *fastcgi_params* file. Consider this line:

	:::nginx
	fastcgi_param  SCRIPT_NAME  $fastcgi_script_name;

What Django expects is not *SCRIPT_NAME* but *PATH_INFO*:

	:::nginx
	fastcgi_param  PATH_INFO  $fastcgi_script_name;

So in case you ever wonder why your Django app only shows you the index page no matter which URL you try to access this might just have to do with the FCGI params.
title: The Problem With Django, Nginx and FCGI
slug: problem-django-nginx-fcgi
date: 2009-08-07 01:49
tags: django, nginx, fcgi

Alright after about a whole day of near-continuous downtime I finally found the bug that I overcame few months ago already. I'm using [nginx](http://nginx.net/) as proxy to Django per FCGI. Now after upgrading nginx the site started to misbehave. No matter which location I tried to access I always ended up on the index page.

So after loads of trial and error I came to the conclusion that the problem is in the *fastcgi_params* file. Consider this line:

	:::nginx
	fastcgi_param  SCRIPT_NAME  $fastcgi_script_name;

What Django expects is not *SCRIPT_NAME* but *PATH_INFO*:

	:::nginx
	fastcgi_param  PATH_INFO  $fastcgi_script_name;

So in case you ever wonder why your Django app only shows you the index page no matter which URL you try to access this might just have to do with the FCGI params.
title: The Problem With Django, Nginx and FCGI
slug: problem-django-nginx-fcgi
date: 2009-08-07 01:49
tags: django, nginx, fcgi

Alright after about a whole day of near-continuous downtime I finally found the bug that I overcame few months ago already. I'm using [nginx](http://nginx.net/) as proxy to Django per FCGI. Now after upgrading nginx the site started to misbehave. No matter which location I tried to access I always ended up on the index page.

So after loads of trial and error I came to the conclusion that the problem is in the *fastcgi_params* file. Consider this line:

	:::nginx
	fastcgi_param  SCRIPT_NAME  $fastcgi_script_name;

What Django expects is not *SCRIPT_NAME* but *PATH_INFO*:

	:::nginx
	fastcgi_param  PATH_INFO  $fastcgi_script_name;

So in case you ever wonder why your Django app only shows you the index page no matter which URL you try to access this might just have to do with the FCGI params.
