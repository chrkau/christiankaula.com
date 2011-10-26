title: Die Cache, Die
slug: die-cache-die
date: 2009-07-02 08:44
tags: django

If you ever need to remove a cache fragment that has been created by the cache template tag do like so:

	:::python
	from django.core.cache import cache
	from django.utils.hashcompat import md5_constructor
	from django.utils.http import urlquote

	def invalidate_cache_fragment(fragment_name, *args):
		cargs = md5_constructor(u':'.join([urlquote(arg) for arg in args]))
		cache_key = 'template.cache.%s.%s' % (fragment_name, cargs.hexdigest())
		cache.delete(cache_key)
title: Die Cache, Die
slug: die-cache-die
date: 2009-07-02 08:44
tags: django

If you ever need to remove a cache fragment that has been created by the cache template tag do like so:

	:::python
	from django.core.cache import cache
	from django.utils.hashcompat import md5_constructor
	from django.utils.http import urlquote

	def invalidate_cache_fragment(fragment_name, *args):
		cargs = md5_constructor(u':'.join([urlquote(arg) for arg in args]))
		cache_key = 'template.cache.%s.%s' % (fragment_name, cargs.hexdigest())
		cache.delete(cache_key)
title: Die Cache, Die
slug: die-cache-die
date: 2009-07-02 08:44
tags: django

If you ever need to remove a cache fragment that has been created by the cache template tag do like so:

	:::python
	from django.core.cache import cache
	from django.utils.hashcompat import md5_constructor
	from django.utils.http import urlquote

	def invalidate_cache_fragment(fragment_name, *args):
		cargs = md5_constructor(u':'.join([urlquote(arg) for arg in args]))
		cache_key = 'template.cache.%s.%s' % (fragment_name, cargs.hexdigest())
		cache.delete(cache_key)
title: Die Cache, Die
slug: die-cache-die
date: 2009-07-02 08:44
tags: django

If you ever need to remove a cache fragment that has been created by the cache template tag do like so:

	:::python
	from django.core.cache import cache
	from django.utils.hashcompat import md5_constructor
	from django.utils.http import urlquote

	def invalidate_cache_fragment(fragment_name, *args):
		cargs = md5_constructor(u':'.join([urlquote(arg) for arg in args]))
		cache_key = 'template.cache.%s.%s' % (fragment_name, cargs.hexdigest())
		cache.delete(cache_key)
title: Die Cache, Die
slug: die-cache-die
date: 2009-07-02 08:44
tags: django

If you ever need to remove a cache fragment that has been created by the cache template tag do like so:

	:::python
	from django.core.cache import cache
	from django.utils.hashcompat import md5_constructor
	from django.utils.http import urlquote

	def invalidate_cache_fragment(fragment_name, *args):
		cargs = md5_constructor(u':'.join([urlquote(arg) for arg in args]))
		cache_key = 'template.cache.%s.%s' % (fragment_name, cargs.hexdigest())
		cache.delete(cache_key)
title: Die Cache, Die
slug: die-cache-die
date: 2009-07-02 08:44
tags: django

If you ever need to remove a cache fragment that has been created by the cache template tag do like so:

	:::python
	from django.core.cache import cache
	from django.utils.hashcompat import md5_constructor
	from django.utils.http import urlquote

	def invalidate_cache_fragment(fragment_name, *args):
		cargs = md5_constructor(u':'.join([urlquote(arg) for arg in args]))
		cache_key = 'template.cache.%s.%s' % (fragment_name, cargs.hexdigest())
		cache.delete(cache_key)
title: Die Cache, Die
slug: die-cache-die
date: 2009-07-02 08:44
tags: django

If you ever need to remove a cache fragment that has been created by the cache template tag do like so:

	:::python
	from django.core.cache import cache
	from django.utils.hashcompat import md5_constructor
	from django.utils.http import urlquote

	def invalidate_cache_fragment(fragment_name, *args):
		cargs = md5_constructor(u':'.join([urlquote(arg) for arg in args]))
		cache_key = 'template.cache.%s.%s' % (fragment_name, cargs.hexdigest())
		cache.delete(cache_key)
title: Die Cache, Die
slug: die-cache-die
date: 2009-07-02 08:44
tags: django

If you ever need to remove a cache fragment that has been created by the cache template tag do like so:

	:::python
	from django.core.cache import cache
	from django.utils.hashcompat import md5_constructor
	from django.utils.http import urlquote

	def invalidate_cache_fragment(fragment_name, *args):
		cargs = md5_constructor(u':'.join([urlquote(arg) for arg in args]))
		cache_key = 'template.cache.%s.%s' % (fragment_name, cargs.hexdigest())
		cache.delete(cache_key)
