title: Fun with Forms in Django
slug: fun-forms-django
date: 2009-05-07 16:00
tags: django, python

Now here I got another pearl. It bugged me to no end that one cannot have a *ModelForm* and override only certain attributes of a certain field without having to overwrite the whole field with all of its default attributes. Well, seems that is actually possible, like so:

	:::python
	class SomeForm(forms.ModelForm):
		class Meta:
			model = SomeModel

	def __init__(self, *args, **kwargs):
			super(SomeForm, self).__init__(*args, **kwargs)
			self.fields['some_field'].min_length = 2
			self.fields['some_field'].max_length = 15
			self.fields['some_other_field'].widget = forms.PasswordInput()

[Useful form tricks in Django](http://collingrady.wordpress.com/2008/07/24/useful-form-tricks-in-django/)
