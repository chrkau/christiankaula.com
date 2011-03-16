title: Django can be too convenient
slug: django-can-be-too-convenient
date: 2009-04-29 12:08
tags: django, python, codeconventions, security

Django is nice, I think I have made my point clear on that. As a framework it lets you some truly short code that does quite a lot. It's convenient. But you should be careful to not let yourself fall into the trap of convenience. Here's an example of what I mean:

So we wrote our super nice model like this:

	:::python
	class SomeModel(models.Model):
		foo = models.CharField(max_length=30)
		bar = models.CharField(max_length=30)

Now we need a form so data can get into our little app. We don't need much code for that:

	:::python
	class SomeModelForm(forms.ModelForm):
		class Meta:
			model = SomeModel

So after a while our project has grown to a reasonable size and suddenly there is demand for another field in SomeModel that holds extra important secret data nobody ever should be allowed to see save the user herself and our trusty admins. Our new model might look like this now:

	:::python
	class SomeModel(models.Model):
		foo = models.CharField(max_length=30)
		bar = models.CharField(max_length=30)
		secret_data = models.CharField(max_length=30)

'So what's your point?' you I hear you shout. Sure it's all valid code and everything is working and all is fine. Except your long-forgotten *SomeModelForm* now will show an input field for *secret_data* if you didn't think of changing it. You would never forget you poor little forms, would you? Well I do, chances are you do forget them too sometimes.

And because I'm pretty good at forgetting some of the important details when it would be most important to remember them, I trained myself to always write my forms like this:

	:::python
	class SomeModelForm(forms.ModelForm):
		class Meta:
			model = SomeModel
			fields = ('foo', 'bar')

I'm sure you noticed the fields attribute of the Meta class. This way when I forget about my models they will show too less info instead of too much. Sure the application might still crash in some way because it's missing data, but with an important difference: Now I will get info mails about missing data errors instead of users looking at secret data without me being noticed.

Yep I know your app will go through a staging phase before it's actually deployed on the production server and stuff like this is found by your legion of professional testers. But still - it's one point on the 'stuff I don't have to worry about' side.
