title: Where to Not Put Django Templates
date: 2011-10-01
slug: where-to-not-put-django-templates
tags: django


Here's a hint for you: You are probably putting your Django template files in the wrong place.

	:::bash
	vim yourdjangoproject/someapp/templates/someapp/sometemplate.html

Looks familiar? Uh oh — seems I got you.



## So what's wrong with that line?

The most obvious giveaway is the double occurrence of your app's name. Ever wondered why you should have to put your templates in a directory named after the app that the current templates directory belongs to? No? Aww, you disappoint me. Aren't we developer types supposed to be lazy and such?

Anyway, if you never asked yourself that question, changes are this hasn't occurred to your either: Why would anyone ever want to put a template for one app in the templates directory of another app. Most likely that is because pretty much nobody ever would want to do that.



## But that's the Django way!

No, sorry to disappoint you. And no that does not help with a structured project layout. Remember that it's good style to design Django apps as reusable? You probably do and you are probably thinking: *"Haha! Right! Now what do you say to that?!"* I answer: My point exactly.

Let's assume you strife to design your apps in a reusable manner. Good for you. Now think of how often you have multiple projects with equaling HTML layouts. My guess is you don't have those very often. So that means the templates that came with your neat reusable app have to be customized to the project. And suddenly your app isn't that reusable anymore just because you bundled templates with it.



## But my web designer…

Apart from that you aren't doing your designer a favor either. If you put your templates inside of your app structure the poor guy/girl will have to dig through all those funny *.py* and *.pyc* files. I hear those contain some of the strange stuff those weird corder guys mess around with.

Now if you put all your templates in one directory — possibly even outside of your Django project structure — there will be minimum contact of Python code and HTML. That's a nice thing to do for your layout guy/girl. Just point them at the directory and all they will ever see is homely *.html*. Once you see the happy smile on their face you will know it was the right thing to do.

Besides that you might remember that us weird coder people also like to fight the constant battle of parting layout from logic. A battle we lose often enough, so why not cease victory where it comes easy?



## But you didn't cover my use case at all!

Of course I'm speaking generally here. There are loads of use cases in which it absolutely makes sense to bundle templates with your app. Perhaps in your case your templates simply never change because your app provides some add-on functionality like a WYSIWYG editor. Or you want to provide default templates that are at least unlikely to change much — perhaps some email templates.

The lesson here is that you probably should put your template files in an extra template directory because it makes stuff simpler. And simpler most of times equals better. If you can name a good reason why you still want to bundle your templates with your app, forget I ever said anything and carry on.

