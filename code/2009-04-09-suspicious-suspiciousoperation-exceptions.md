title: Suspicious SuspiciousOperation Exceptions
slug: suspicious-suspiciousoperation-exceptions
date: 2009-04-09 08:38
tags: django, apache

Using Apache and Django is throwing SuspiciousOperation Exception in your face and you have no idea why? Chances are you are using absolute paths. Django doesn't like that. It expects you to be a good boy/girl and put all your stuff under MEDIA_ROOT with relative paths. Everything else is perceived as suspicious behavior it seems.


**update 2011-03-16:**

Thanks to Oto for giving me a heads up:

> You can fix this by linking to the folder you need to put your images in
> using
>
> ln -s /my/uploads/ /my/project/static/media
>
> Django will write to the media folder and it will really write to the uploads
> folder.
>
> Just wanted to let you know in case you wanted to update your blog post to
> give an alternative. I ran into this issue when working on a multi-front
> store with a backend master app controlling all the data/assets.

