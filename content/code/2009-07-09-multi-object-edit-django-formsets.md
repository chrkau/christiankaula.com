title: Multi-Object-Edit With Django FormSets
slug: multi-object-edit-django-formsets
date: 2009-07-09 08:39
tags: django

I had to write a multi-object edit table the other day for a Django project and as such I dove into the [FormSet Documentation](http://docs.djangoproject.com/en/dev/topics/forms/formsets/). Django's documentation is really good usually but the part abut the FormSets was a bit of a letdown.

So in case anybody else is in the same situation here is some code of how I did it (written from memory - should still be okay I hope).


	:::python
	# forms.py
	from django.forms.models import modelformset_factory

	# creating a FormSet for a specific Model is easy
	FooFormSetBase = modelformset_factory(
		Foo, extra=0, fields=('somefield', 'someotherfield'))

	# now we want to add a checkbox so we can do stuff to only selected items
	class FooFormSet(FooFormSetBase):
		# this is where you can add additional fields to a ModelFormSet
		# this is also where you can change stuff about the auto generated form
		def add_fields(self, form, index):
			super(FooFormSet, self).add_fields(form, index)
			form.fields['is_checked'] = forms.BooleanField(required=False)
			form.fields['somefield'].widget.attrs['class'] = 'somefieldclass'

After writing the FormSet itself here is the view:

	:::python
	# views.py
	from django.shortcuts import redirect
	from django.template import RequestContext
	from fooproject.fooapp.forms import FooFormSet
	from fooproject.models import Foo


	def fooview(request):
		if request.method == 'POST':
			# we have multiple actions - save and delete in this case
			action = request.POST.get('action')
			formset = FooFormSet(
				request.POST, queryset=Foo.objects.all())

			if formset.is_valid():
				# iterate over all forms in the formset
				for form in formset.forms:
					# only do stuff for forms in which is_checked is checked
					if form.cleaned_data.get('is_checked'):
						if action == u'delete':
							# we need to call save to get an actual model but
							# there is no need to hit the database hence the
							# commit=False
							model_instance = form.save(commit=False)
							# now that we got a model we can delete it
							model_instance.delete()
						if action == u'save':
							form.save()

				redirect('someview')

		else:
			formset = FooFormSet(
				queryset=Foo.objects.all()
			)

		return render_to_response('sometemplate.html', {
			'formset': formset,
		}, context_instance=RequestContext(request))

Now all that's missing is the template:

	:::html+django
	<form action="." method="post" accept-charset="utf-8">
		<table>
			<thead>
				<tr>
					<th>is_checked</th>
					<th>somefield</th>
					<th>someotherfield</th>
				</tr>
			</thead>
			<tbody>
			{% for form in formset.forms %}
				<tr>
					<td>
						{# don't forget about the id field #}
						{{ form.id }}
						{{ form.is_checked }}
					</td>
					<td>{{ form.somefield }}</td>
					<td>{{ form.someotherfield }}</td>
				</tr>
			{% endfor %}
			</tbody>
		</table>
		<p>
			{# and don't forget about the management form #}
			{{ formset.management_form }}
			{% csrf_token %}
			<button type="submit" name="action" value="save">save</button>
			<button type="submit" name="action" value="delete">delete</button>
		</p>
	</form>

Of course there is stuff still missing – you won't see errors in your form for example. But you get the general idea.


**Edit 31.10.2012:**

Thanks to [Trinh Nguyen](https://twitter.com/dangtrinhnt) for bringing my attention to some stupid errors in the code and the inspiration do do some more commenting.

