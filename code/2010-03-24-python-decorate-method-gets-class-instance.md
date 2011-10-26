title: Python: Decorate a Method That Gets Passed the Class Instance
slug: python-decorate-method-gets-class-instance
date: 2010-03-24 01:57
tags: python

The other day I needed to decorate a method with a decorator class that knows about the owner of the method meaning the instance. This works as expected with function decorators:

	:::python
	def some_decorator(func):
		def decorator(self, *args, **kwargs):
			print 'instance %s of class %s is now decorated whee!' % (
				self, self.__class__
			)
			return func(*args, **kwargs)

		return decorator


	class SomeClass(object):
		@some_decorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

If you need/want to use a class based decorator you have to do this:

	:::python
	class SomeDecorator(object):
		def __init__(self, func):
			self.func = func

		def __call__(self, *args, **kwargs):
			print 'instance %s of class %s this is now decorated whee!' % (
				self.obj, self.cls
			)
			return self.func.__call__(*args, **kwargs)
	
		def __get__(self, instance, owner):
			self.cls = owner
			self.obj = instance

			return self.__call__


	class SomeClass(object):
		@SomeDecorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

Thanks to [Ozgur](http://eoyilmaz.blogspot.com/) who's [post about the topic](http://eoyilmaz.blogspot.com/2009/09/python-function-decorators-2-decorating.html) pointed me in the right direction.
title: Python: Decorate a Method That Gets Passed the Class Instance
slug: python-decorate-method-gets-class-instance
date: 2010-03-24 01:57
tags: python

The other day I needed to decorate a method with a decorator class that knows about the owner of the method meaning the instance. This works as expected with function decorators:

	:::python
	def some_decorator(func):
		def decorator(self, *args, **kwargs):
			print 'instance %s of class %s is now decorated whee!' % (
				self, self.__class__
			)
			return func(*args, **kwargs)

		return decorator


	class SomeClass(object):
		@some_decorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

If you need/want to use a class based decorator you have to do this:

	:::python
	class SomeDecorator(object):
		def __init__(self, func):
			self.func = func

		def __call__(self, *args, **kwargs):
			print 'instance %s of class %s this is now decorated whee!' % (
				self.obj, self.cls
			)
			return self.func.__call__(*args, **kwargs)
	
		def __get__(self, instance, owner):
			self.cls = owner
			self.obj = instance

			return self.__call__


	class SomeClass(object):
		@SomeDecorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

Thanks to [Ozgur](http://eoyilmaz.blogspot.com/) who's [post about the topic](http://eoyilmaz.blogspot.com/2009/09/python-function-decorators-2-decorating.html) pointed me in the right direction.
title: Python: Decorate a Method That Gets Passed the Class Instance
slug: python-decorate-method-gets-class-instance
date: 2010-03-24 01:57
tags: python

The other day I needed to decorate a method with a decorator class that knows about the owner of the method meaning the instance. This works as expected with function decorators:

	:::python
	def some_decorator(func):
		def decorator(self, *args, **kwargs):
			print 'instance %s of class %s is now decorated whee!' % (
				self, self.__class__
			)
			return func(*args, **kwargs)

		return decorator


	class SomeClass(object):
		@some_decorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

If you need/want to use a class based decorator you have to do this:

	:::python
	class SomeDecorator(object):
		def __init__(self, func):
			self.func = func

		def __call__(self, *args, **kwargs):
			print 'instance %s of class %s this is now decorated whee!' % (
				self.obj, self.cls
			)
			return self.func.__call__(*args, **kwargs)
	
		def __get__(self, instance, owner):
			self.cls = owner
			self.obj = instance

			return self.__call__


	class SomeClass(object):
		@SomeDecorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

Thanks to [Ozgur](http://eoyilmaz.blogspot.com/) who's [post about the topic](http://eoyilmaz.blogspot.com/2009/09/python-function-decorators-2-decorating.html) pointed me in the right direction.
title: Python: Decorate a Method That Gets Passed the Class Instance
slug: python-decorate-method-gets-class-instance
date: 2010-03-24 01:57
tags: python

The other day I needed to decorate a method with a decorator class that knows about the owner of the method meaning the instance. This works as expected with function decorators:

	:::python
	def some_decorator(func):
		def decorator(self, *args, **kwargs):
			print 'instance %s of class %s is now decorated whee!' % (
				self, self.__class__
			)
			return func(*args, **kwargs)

		return decorator


	class SomeClass(object):
		@some_decorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

If you need/want to use a class based decorator you have to do this:

	:::python
	class SomeDecorator(object):
		def __init__(self, func):
			self.func = func

		def __call__(self, *args, **kwargs):
			print 'instance %s of class %s this is now decorated whee!' % (
				self.obj, self.cls
			)
			return self.func.__call__(*args, **kwargs)
	
		def __get__(self, instance, owner):
			self.cls = owner
			self.obj = instance

			return self.__call__


	class SomeClass(object):
		@SomeDecorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

Thanks to [Ozgur](http://eoyilmaz.blogspot.com/) who's [post about the topic](http://eoyilmaz.blogspot.com/2009/09/python-function-decorators-2-decorating.html) pointed me in the right direction.
title: Python: Decorate a Method That Gets Passed the Class Instance
slug: python-decorate-method-gets-class-instance
date: 2010-03-24 01:57
tags: python

The other day I needed to decorate a method with a decorator class that knows about the owner of the method meaning the instance. This works as expected with function decorators:

	:::python
	def some_decorator(func):
		def decorator(self, *args, **kwargs):
			print 'instance %s of class %s is now decorated whee!' % (
				self, self.__class__
			)
			return func(*args, **kwargs)

		return decorator


	class SomeClass(object):
		@some_decorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

If you need/want to use a class based decorator you have to do this:

	:::python
	class SomeDecorator(object):
		def __init__(self, func):
			self.func = func

		def __call__(self, *args, **kwargs):
			print 'instance %s of class %s this is now decorated whee!' % (
				self.obj, self.cls
			)
			return self.func.__call__(*args, **kwargs)
	
		def __get__(self, instance, owner):
			self.cls = owner
			self.obj = instance

			return self.__call__


	class SomeClass(object):
		@SomeDecorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

Thanks to [Ozgur](http://eoyilmaz.blogspot.com/) who's [post about the topic](http://eoyilmaz.blogspot.com/2009/09/python-function-decorators-2-decorating.html) pointed me in the right direction.
title: Python: Decorate a Method That Gets Passed the Class Instance
slug: python-decorate-method-gets-class-instance
date: 2010-03-24 01:57
tags: python

The other day I needed to decorate a method with a decorator class that knows about the owner of the method meaning the instance. This works as expected with function decorators:

	:::python
	def some_decorator(func):
		def decorator(self, *args, **kwargs):
			print 'instance %s of class %s is now decorated whee!' % (
				self, self.__class__
			)
			return func(*args, **kwargs)

		return decorator


	class SomeClass(object):
		@some_decorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

If you need/want to use a class based decorator you have to do this:

	:::python
	class SomeDecorator(object):
		def __init__(self, func):
			self.func = func

		def __call__(self, *args, **kwargs):
			print 'instance %s of class %s this is now decorated whee!' % (
				self.obj, self.cls
			)
			return self.func.__call__(*args, **kwargs)
	
		def __get__(self, instance, owner):
			self.cls = owner
			self.obj = instance

			return self.__call__


	class SomeClass(object):
		@SomeDecorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

Thanks to [Ozgur](http://eoyilmaz.blogspot.com/) who's [post about the topic](http://eoyilmaz.blogspot.com/2009/09/python-function-decorators-2-decorating.html) pointed me in the right direction.
title: Python: Decorate a Method That Gets Passed the Class Instance
slug: python-decorate-method-gets-class-instance
date: 2010-03-24 01:57
tags: python

The other day I needed to decorate a method with a decorator class that knows about the owner of the method meaning the instance. This works as expected with function decorators:

	:::python
	def some_decorator(func):
		def decorator(self, *args, **kwargs):
			print 'instance %s of class %s is now decorated whee!' % (
				self, self.__class__
			)
			return func(*args, **kwargs)

		return decorator


	class SomeClass(object):
		@some_decorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

If you need/want to use a class based decorator you have to do this:

	:::python
	class SomeDecorator(object):
		def __init__(self, func):
			self.func = func

		def __call__(self, *args, **kwargs):
			print 'instance %s of class %s this is now decorated whee!' % (
				self.obj, self.cls
			)
			return self.func.__call__(*args, **kwargs)
	
		def __get__(self, instance, owner):
			self.cls = owner
			self.obj = instance

			return self.__call__


	class SomeClass(object):
		@SomeDecorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

Thanks to [Ozgur](http://eoyilmaz.blogspot.com/) who's [post about the topic](http://eoyilmaz.blogspot.com/2009/09/python-function-decorators-2-decorating.html) pointed me in the right direction.
title: Python: Decorate a Method That Gets Passed the Class Instance
slug: python-decorate-method-gets-class-instance
date: 2010-03-24 01:57
tags: python

The other day I needed to decorate a method with a decorator class that knows about the owner of the method meaning the instance. This works as expected with function decorators:

	:::python
	def some_decorator(func):
		def decorator(self, *args, **kwargs):
			print 'instance %s of class %s is now decorated whee!' % (
				self, self.__class__
			)
			return func(*args, **kwargs)

		return decorator


	class SomeClass(object):
		@some_decorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

If you need/want to use a class based decorator you have to do this:

	:::python
	class SomeDecorator(object):
		def __init__(self, func):
			self.func = func

		def __call__(self, *args, **kwargs):
			print 'instance %s of class %s this is now decorated whee!' % (
				self.obj, self.cls
			)
			return self.func.__call__(*args, **kwargs)
	
		def __get__(self, instance, owner):
			self.cls = owner
			self.obj = instance

			return self.__call__


	class SomeClass(object):
		@SomeDecorator
		def dostuff(self, foo, bar):
			print 'do %s, %s' % (foo, bar)

Thanks to [Ozgur](http://eoyilmaz.blogspot.com/) who's [post about the topic](http://eoyilmaz.blogspot.com/2009/09/python-function-decorators-2-decorating.html) pointed me in the right direction.
