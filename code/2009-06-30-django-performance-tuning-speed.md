title: Django Performance Tuning - Speed Up!
slug: django-performance-tuning-speed
date: 2009-06-30 08:53
tags: django, performance

So these days I spend a lot of my workday trying to get a Django app up to speed that... wasn't exactly written with performance in mind. Here are a few things that helped me speed up that thing (all without going down to SQL level):

* If you need to check if a foreign key points to an existing model or simply need the id of a related object instead of using *foo.user* you can use *foo.user_id*. That way you won't hit the database without really needing the related object.
* Same as above but for assignments. Instead of *foo.user = bar.user* you can do *foo.user_id = bar.user_id*.
* Same as above but for filters. No need to do *Foo.objects.filter(somefk=bar.user)* if you can do *Foo.objects.filter(somefk=bar.user_id)* and save a trip to the database in the best case.
* The [select_related](http://docs.djangoproject.com/en/dev/ref/models/querysets/#id4) queryset method is your friend. But only if you treat it right and don't throw it at any queryset that comes into view. Take some time and consider what related objects you will need and include only those.
* If you don't need objects but only some values in those objects don't let the ORM build a pile of objects just to grab some integers. Read up on [values_list](http://docs.djangoproject.com/en/1.0/ref/models/querysets/#values-list-fields).
* Read up on the [with template tag](http://docs.djangoproject.com/en/dev/ref/templates/builtins/#with). Use it, love it - it will make you a better person.
title: Django Performance Tuning - Speed Up!
slug: django-performance-tuning-speed
date: 2009-06-30 08:53
tags: django, performance

So these days I spend a lot of my workday trying to get a Django app up to speed that... wasn't exactly written with performance in mind. Here are a few things that helped me speed up that thing (all without going down to SQL level):

* If you need to check if a foreign key points to an existing model or simply need the id of a related object instead of using *foo.user* you can use *foo.user_id*. That way you won't hit the database without really needing the related object.
* Same as above but for assignments. Instead of *foo.user = bar.user* you can do *foo.user_id = bar.user_id*.
* Same as above but for filters. No need to do *Foo.objects.filter(somefk=bar.user)* if you can do *Foo.objects.filter(somefk=bar.user_id)* and save a trip to the database in the best case.
* The [select_related](http://docs.djangoproject.com/en/dev/ref/models/querysets/#id4) queryset method is your friend. But only if you treat it right and don't throw it at any queryset that comes into view. Take some time and consider what related objects you will need and include only those.
* If you don't need objects but only some values in those objects don't let the ORM build a pile of objects just to grab some integers. Read up on [values_list](http://docs.djangoproject.com/en/1.0/ref/models/querysets/#values-list-fields).
* Read up on the [with template tag](http://docs.djangoproject.com/en/dev/ref/templates/builtins/#with). Use it, love it - it will make you a better person.
title: Django Performance Tuning - Speed Up!
slug: django-performance-tuning-speed
date: 2009-06-30 08:53
tags: django, performance

So these days I spend a lot of my workday trying to get a Django app up to speed that... wasn't exactly written with performance in mind. Here are a few things that helped me speed up that thing (all without going down to SQL level):

* If you need to check if a foreign key points to an existing model or simply need the id of a related object instead of using *foo.user* you can use *foo.user_id*. That way you won't hit the database without really needing the related object.
* Same as above but for assignments. Instead of *foo.user = bar.user* you can do *foo.user_id = bar.user_id*.
* Same as above but for filters. No need to do *Foo.objects.filter(somefk=bar.user)* if you can do *Foo.objects.filter(somefk=bar.user_id)* and save a trip to the database in the best case.
* The [select_related](http://docs.djangoproject.com/en/dev/ref/models/querysets/#id4) queryset method is your friend. But only if you treat it right and don't throw it at any queryset that comes into view. Take some time and consider what related objects you will need and include only those.
* If you don't need objects but only some values in those objects don't let the ORM build a pile of objects just to grab some integers. Read up on [values_list](http://docs.djangoproject.com/en/1.0/ref/models/querysets/#values-list-fields).
* Read up on the [with template tag](http://docs.djangoproject.com/en/dev/ref/templates/builtins/#with). Use it, love it - it will make you a better person.
title: Django Performance Tuning - Speed Up!
slug: django-performance-tuning-speed
date: 2009-06-30 08:53
tags: django, performance

So these days I spend a lot of my workday trying to get a Django app up to speed that... wasn't exactly written with performance in mind. Here are a few things that helped me speed up that thing (all without going down to SQL level):

* If you need to check if a foreign key points to an existing model or simply need the id of a related object instead of using *foo.user* you can use *foo.user_id*. That way you won't hit the database without really needing the related object.
* Same as above but for assignments. Instead of *foo.user = bar.user* you can do *foo.user_id = bar.user_id*.
* Same as above but for filters. No need to do *Foo.objects.filter(somefk=bar.user)* if you can do *Foo.objects.filter(somefk=bar.user_id)* and save a trip to the database in the best case.
* The [select_related](http://docs.djangoproject.com/en/dev/ref/models/querysets/#id4) queryset method is your friend. But only if you treat it right and don't throw it at any queryset that comes into view. Take some time and consider what related objects you will need and include only those.
* If you don't need objects but only some values in those objects don't let the ORM build a pile of objects just to grab some integers. Read up on [values_list](http://docs.djangoproject.com/en/1.0/ref/models/querysets/#values-list-fields).
* Read up on the [with template tag](http://docs.djangoproject.com/en/dev/ref/templates/builtins/#with). Use it, love it - it will make you a better person.
title: Django Performance Tuning - Speed Up!
slug: django-performance-tuning-speed
date: 2009-06-30 08:53
tags: django, performance

So these days I spend a lot of my workday trying to get a Django app up to speed that... wasn't exactly written with performance in mind. Here are a few things that helped me speed up that thing (all without going down to SQL level):

* If you need to check if a foreign key points to an existing model or simply need the id of a related object instead of using *foo.user* you can use *foo.user_id*. That way you won't hit the database without really needing the related object.
* Same as above but for assignments. Instead of *foo.user = bar.user* you can do *foo.user_id = bar.user_id*.
* Same as above but for filters. No need to do *Foo.objects.filter(somefk=bar.user)* if you can do *Foo.objects.filter(somefk=bar.user_id)* and save a trip to the database in the best case.
* The [select_related](http://docs.djangoproject.com/en/dev/ref/models/querysets/#id4) queryset method is your friend. But only if you treat it right and don't throw it at any queryset that comes into view. Take some time and consider what related objects you will need and include only those.
* If you don't need objects but only some values in those objects don't let the ORM build a pile of objects just to grab some integers. Read up on [values_list](http://docs.djangoproject.com/en/1.0/ref/models/querysets/#values-list-fields).
* Read up on the [with template tag](http://docs.djangoproject.com/en/dev/ref/templates/builtins/#with). Use it, love it - it will make you a better person.
title: Django Performance Tuning - Speed Up!
slug: django-performance-tuning-speed
date: 2009-06-30 08:53
tags: django, performance

So these days I spend a lot of my workday trying to get a Django app up to speed that... wasn't exactly written with performance in mind. Here are a few things that helped me speed up that thing (all without going down to SQL level):

* If you need to check if a foreign key points to an existing model or simply need the id of a related object instead of using *foo.user* you can use *foo.user_id*. That way you won't hit the database without really needing the related object.
* Same as above but for assignments. Instead of *foo.user = bar.user* you can do *foo.user_id = bar.user_id*.
* Same as above but for filters. No need to do *Foo.objects.filter(somefk=bar.user)* if you can do *Foo.objects.filter(somefk=bar.user_id)* and save a trip to the database in the best case.
* The [select_related](http://docs.djangoproject.com/en/dev/ref/models/querysets/#id4) queryset method is your friend. But only if you treat it right and don't throw it at any queryset that comes into view. Take some time and consider what related objects you will need and include only those.
* If you don't need objects but only some values in those objects don't let the ORM build a pile of objects just to grab some integers. Read up on [values_list](http://docs.djangoproject.com/en/1.0/ref/models/querysets/#values-list-fields).
* Read up on the [with template tag](http://docs.djangoproject.com/en/dev/ref/templates/builtins/#with). Use it, love it - it will make you a better person.
title: Django Performance Tuning - Speed Up!
slug: django-performance-tuning-speed
date: 2009-06-30 08:53
tags: django, performance

So these days I spend a lot of my workday trying to get a Django app up to speed that... wasn't exactly written with performance in mind. Here are a few things that helped me speed up that thing (all without going down to SQL level):

* If you need to check if a foreign key points to an existing model or simply need the id of a related object instead of using *foo.user* you can use *foo.user_id*. That way you won't hit the database without really needing the related object.
* Same as above but for assignments. Instead of *foo.user = bar.user* you can do *foo.user_id = bar.user_id*.
* Same as above but for filters. No need to do *Foo.objects.filter(somefk=bar.user)* if you can do *Foo.objects.filter(somefk=bar.user_id)* and save a trip to the database in the best case.
* The [select_related](http://docs.djangoproject.com/en/dev/ref/models/querysets/#id4) queryset method is your friend. But only if you treat it right and don't throw it at any queryset that comes into view. Take some time and consider what related objects you will need and include only those.
* If you don't need objects but only some values in those objects don't let the ORM build a pile of objects just to grab some integers. Read up on [values_list](http://docs.djangoproject.com/en/1.0/ref/models/querysets/#values-list-fields).
* Read up on the [with template tag](http://docs.djangoproject.com/en/dev/ref/templates/builtins/#with). Use it, love it - it will make you a better person.
title: Django Performance Tuning - Speed Up!
slug: django-performance-tuning-speed
date: 2009-06-30 08:53
tags: django, performance

So these days I spend a lot of my workday trying to get a Django app up to speed that... wasn't exactly written with performance in mind. Here are a few things that helped me speed up that thing (all without going down to SQL level):

* If you need to check if a foreign key points to an existing model or simply need the id of a related object instead of using *foo.user* you can use *foo.user_id*. That way you won't hit the database without really needing the related object.
* Same as above but for assignments. Instead of *foo.user = bar.user* you can do *foo.user_id = bar.user_id*.
* Same as above but for filters. No need to do *Foo.objects.filter(somefk=bar.user)* if you can do *Foo.objects.filter(somefk=bar.user_id)* and save a trip to the database in the best case.
* The [select_related](http://docs.djangoproject.com/en/dev/ref/models/querysets/#id4) queryset method is your friend. But only if you treat it right and don't throw it at any queryset that comes into view. Take some time and consider what related objects you will need and include only those.
* If you don't need objects but only some values in those objects don't let the ORM build a pile of objects just to grab some integers. Read up on [values_list](http://docs.djangoproject.com/en/1.0/ref/models/querysets/#values-list-fields).
* Read up on the [with template tag](http://docs.djangoproject.com/en/dev/ref/templates/builtins/#with). Use it, love it - it will make you a better person.
