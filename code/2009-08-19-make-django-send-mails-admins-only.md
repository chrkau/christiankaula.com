title: Make Django Send Mails to Admins Only
slug: make-django-send-mails-admins-only
date: 2009-08-19 08:33
tags: django, python

Image you are running a staging system for your Django project on which all the testing for the production system is done. You are using a dump of the production database to have some actual data you can play around with. And you have this one/many function/s in which you send email to some/all users. They probably will not be happy to get all those emails from your staging system while not having the slightest idea what's going on.

#### The Code
Here is a solution I came up with:

	:::python
	class EmailMessage(DjangoEmailMessage):
	    """
	    Wrapper for the original DjangoEmailMessage.
	    Responsible for sending emails only to admins instead of original
	    addressees if application is in testing mode.
	    """
	    def message(self):
	        if settings.STAGING:
	            admin_addresses = zip(*settings.ADMINS)[1]
	            self.body = 'These people:\n\n%s\n\nWould have received this:\n\n%s' % (
	                self.recipients(), self.body
	            )
	            self.subject = u'Staging: ' + unicode(self.subject)
	            self.to = admin_addresses
	            self.bcc = []
        
	        return super(EmailMessage, self).message()


	def send_mass_mail(datatuple, fail_silently=False, auth_user=None,
	    auth_password=None
	):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password, fail_silently=fail_silently
	    )
	    messages = [
	        EmailMessage(subject, message, sender, recipient)
	        for subject, message, sender, recipient in datatuple
	    ]
	    return connection.send_messages(messages)


	def send_mail(subject, message, from_email, recipient_list,
	              fail_silently=False, auth_user=None, auth_password=None):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password,
	        fail_silently=fail_silently
	    )
	    return EmailMessage(
	        subject, message, from_email, recipient_list,
	        connection=connection
	    ).send()


#### Okay what does this do?

I added a setting *STAGING* to my *settings.py* which is set to *True* on the staging system (makes sense no?). That setting controls if emails are actually send to the original receivers or if all outgoing mail is sent to the admins only.

Of course that only works for cases in which you use your own *EmailMessage*, *send_mass_mail* and *send_mail* class and functions.
title: Make Django Send Mails to Admins Only
slug: make-django-send-mails-admins-only
date: 2009-08-19 08:33
tags: django, python

Image you are running a staging system for your Django project on which all the testing for the production system is done. You are using a dump of the production database to have some actual data you can play around with. And you have this one/many function/s in which you send email to some/all users. They probably will not be happy to get all those emails from your staging system while not having the slightest idea what's going on.

#### The Code
Here is a solution I came up with:

	:::python
	class EmailMessage(DjangoEmailMessage):
	    """
	    Wrapper for the original DjangoEmailMessage.
	    Responsible for sending emails only to admins instead of original
	    addressees if application is in testing mode.
	    """
	    def message(self):
	        if settings.STAGING:
	            admin_addresses = zip(*settings.ADMINS)[1]
	            self.body = 'These people:\n\n%s\n\nWould have received this:\n\n%s' % (
	                self.recipients(), self.body
	            )
	            self.subject = u'Staging: ' + unicode(self.subject)
	            self.to = admin_addresses
	            self.bcc = []
        
	        return super(EmailMessage, self).message()


	def send_mass_mail(datatuple, fail_silently=False, auth_user=None,
	    auth_password=None
	):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password, fail_silently=fail_silently
	    )
	    messages = [
	        EmailMessage(subject, message, sender, recipient)
	        for subject, message, sender, recipient in datatuple
	    ]
	    return connection.send_messages(messages)


	def send_mail(subject, message, from_email, recipient_list,
	              fail_silently=False, auth_user=None, auth_password=None):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password,
	        fail_silently=fail_silently
	    )
	    return EmailMessage(
	        subject, message, from_email, recipient_list,
	        connection=connection
	    ).send()


#### Okay what does this do?

I added a setting *STAGING* to my *settings.py* which is set to *True* on the staging system (makes sense no?). That setting controls if emails are actually send to the original receivers or if all outgoing mail is sent to the admins only.

Of course that only works for cases in which you use your own *EmailMessage*, *send_mass_mail* and *send_mail* class and functions.
title: Make Django Send Mails to Admins Only
slug: make-django-send-mails-admins-only
date: 2009-08-19 08:33
tags: django, python

Image you are running a staging system for your Django project on which all the testing for the production system is done. You are using a dump of the production database to have some actual data you can play around with. And you have this one/many function/s in which you send email to some/all users. They probably will not be happy to get all those emails from your staging system while not having the slightest idea what's going on.

#### The Code
Here is a solution I came up with:

	:::python
	class EmailMessage(DjangoEmailMessage):
	    """
	    Wrapper for the original DjangoEmailMessage.
	    Responsible for sending emails only to admins instead of original
	    addressees if application is in testing mode.
	    """
	    def message(self):
	        if settings.STAGING:
	            admin_addresses = zip(*settings.ADMINS)[1]
	            self.body = 'These people:\n\n%s\n\nWould have received this:\n\n%s' % (
	                self.recipients(), self.body
	            )
	            self.subject = u'Staging: ' + unicode(self.subject)
	            self.to = admin_addresses
	            self.bcc = []
        
	        return super(EmailMessage, self).message()


	def send_mass_mail(datatuple, fail_silently=False, auth_user=None,
	    auth_password=None
	):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password, fail_silently=fail_silently
	    )
	    messages = [
	        EmailMessage(subject, message, sender, recipient)
	        for subject, message, sender, recipient in datatuple
	    ]
	    return connection.send_messages(messages)


	def send_mail(subject, message, from_email, recipient_list,
	              fail_silently=False, auth_user=None, auth_password=None):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password,
	        fail_silently=fail_silently
	    )
	    return EmailMessage(
	        subject, message, from_email, recipient_list,
	        connection=connection
	    ).send()


#### Okay what does this do?

I added a setting *STAGING* to my *settings.py* which is set to *True* on the staging system (makes sense no?). That setting controls if emails are actually send to the original receivers or if all outgoing mail is sent to the admins only.

Of course that only works for cases in which you use your own *EmailMessage*, *send_mass_mail* and *send_mail* class and functions.
title: Make Django Send Mails to Admins Only
slug: make-django-send-mails-admins-only
date: 2009-08-19 08:33
tags: django, python

Image you are running a staging system for your Django project on which all the testing for the production system is done. You are using a dump of the production database to have some actual data you can play around with. And you have this one/many function/s in which you send email to some/all users. They probably will not be happy to get all those emails from your staging system while not having the slightest idea what's going on.

#### The Code
Here is a solution I came up with:

	:::python
	class EmailMessage(DjangoEmailMessage):
	    """
	    Wrapper for the original DjangoEmailMessage.
	    Responsible for sending emails only to admins instead of original
	    addressees if application is in testing mode.
	    """
	    def message(self):
	        if settings.STAGING:
	            admin_addresses = zip(*settings.ADMINS)[1]
	            self.body = 'These people:\n\n%s\n\nWould have received this:\n\n%s' % (
	                self.recipients(), self.body
	            )
	            self.subject = u'Staging: ' + unicode(self.subject)
	            self.to = admin_addresses
	            self.bcc = []
        
	        return super(EmailMessage, self).message()


	def send_mass_mail(datatuple, fail_silently=False, auth_user=None,
	    auth_password=None
	):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password, fail_silently=fail_silently
	    )
	    messages = [
	        EmailMessage(subject, message, sender, recipient)
	        for subject, message, sender, recipient in datatuple
	    ]
	    return connection.send_messages(messages)


	def send_mail(subject, message, from_email, recipient_list,
	              fail_silently=False, auth_user=None, auth_password=None):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password,
	        fail_silently=fail_silently
	    )
	    return EmailMessage(
	        subject, message, from_email, recipient_list,
	        connection=connection
	    ).send()


#### Okay what does this do?

I added a setting *STAGING* to my *settings.py* which is set to *True* on the staging system (makes sense no?). That setting controls if emails are actually send to the original receivers or if all outgoing mail is sent to the admins only.

Of course that only works for cases in which you use your own *EmailMessage*, *send_mass_mail* and *send_mail* class and functions.
title: Make Django Send Mails to Admins Only
slug: make-django-send-mails-admins-only
date: 2009-08-19 08:33
tags: django, python

Image you are running a staging system for your Django project on which all the testing for the production system is done. You are using a dump of the production database to have some actual data you can play around with. And you have this one/many function/s in which you send email to some/all users. They probably will not be happy to get all those emails from your staging system while not having the slightest idea what's going on.

#### The Code
Here is a solution I came up with:

	:::python
	class EmailMessage(DjangoEmailMessage):
	    """
	    Wrapper for the original DjangoEmailMessage.
	    Responsible for sending emails only to admins instead of original
	    addressees if application is in testing mode.
	    """
	    def message(self):
	        if settings.STAGING:
	            admin_addresses = zip(*settings.ADMINS)[1]
	            self.body = 'These people:\n\n%s\n\nWould have received this:\n\n%s' % (
	                self.recipients(), self.body
	            )
	            self.subject = u'Staging: ' + unicode(self.subject)
	            self.to = admin_addresses
	            self.bcc = []
        
	        return super(EmailMessage, self).message()


	def send_mass_mail(datatuple, fail_silently=False, auth_user=None,
	    auth_password=None
	):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password, fail_silently=fail_silently
	    )
	    messages = [
	        EmailMessage(subject, message, sender, recipient)
	        for subject, message, sender, recipient in datatuple
	    ]
	    return connection.send_messages(messages)


	def send_mail(subject, message, from_email, recipient_list,
	              fail_silently=False, auth_user=None, auth_password=None):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password,
	        fail_silently=fail_silently
	    )
	    return EmailMessage(
	        subject, message, from_email, recipient_list,
	        connection=connection
	    ).send()


#### Okay what does this do?

I added a setting *STAGING* to my *settings.py* which is set to *True* on the staging system (makes sense no?). That setting controls if emails are actually send to the original receivers or if all outgoing mail is sent to the admins only.

Of course that only works for cases in which you use your own *EmailMessage*, *send_mass_mail* and *send_mail* class and functions.
title: Make Django Send Mails to Admins Only
slug: make-django-send-mails-admins-only
date: 2009-08-19 08:33
tags: django, python

Image you are running a staging system for your Django project on which all the testing for the production system is done. You are using a dump of the production database to have some actual data you can play around with. And you have this one/many function/s in which you send email to some/all users. They probably will not be happy to get all those emails from your staging system while not having the slightest idea what's going on.

#### The Code
Here is a solution I came up with:

	:::python
	class EmailMessage(DjangoEmailMessage):
	    """
	    Wrapper for the original DjangoEmailMessage.
	    Responsible for sending emails only to admins instead of original
	    addressees if application is in testing mode.
	    """
	    def message(self):
	        if settings.STAGING:
	            admin_addresses = zip(*settings.ADMINS)[1]
	            self.body = 'These people:\n\n%s\n\nWould have received this:\n\n%s' % (
	                self.recipients(), self.body
	            )
	            self.subject = u'Staging: ' + unicode(self.subject)
	            self.to = admin_addresses
	            self.bcc = []
        
	        return super(EmailMessage, self).message()


	def send_mass_mail(datatuple, fail_silently=False, auth_user=None,
	    auth_password=None
	):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password, fail_silently=fail_silently
	    )
	    messages = [
	        EmailMessage(subject, message, sender, recipient)
	        for subject, message, sender, recipient in datatuple
	    ]
	    return connection.send_messages(messages)


	def send_mail(subject, message, from_email, recipient_list,
	              fail_silently=False, auth_user=None, auth_password=None):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password,
	        fail_silently=fail_silently
	    )
	    return EmailMessage(
	        subject, message, from_email, recipient_list,
	        connection=connection
	    ).send()


#### Okay what does this do?

I added a setting *STAGING* to my *settings.py* which is set to *True* on the staging system (makes sense no?). That setting controls if emails are actually send to the original receivers or if all outgoing mail is sent to the admins only.

Of course that only works for cases in which you use your own *EmailMessage*, *send_mass_mail* and *send_mail* class and functions.
title: Make Django Send Mails to Admins Only
slug: make-django-send-mails-admins-only
date: 2009-08-19 08:33
tags: django, python

Image you are running a staging system for your Django project on which all the testing for the production system is done. You are using a dump of the production database to have some actual data you can play around with. And you have this one/many function/s in which you send email to some/all users. They probably will not be happy to get all those emails from your staging system while not having the slightest idea what's going on.

#### The Code
Here is a solution I came up with:

	:::python
	class EmailMessage(DjangoEmailMessage):
	    """
	    Wrapper for the original DjangoEmailMessage.
	    Responsible for sending emails only to admins instead of original
	    addressees if application is in testing mode.
	    """
	    def message(self):
	        if settings.STAGING:
	            admin_addresses = zip(*settings.ADMINS)[1]
	            self.body = 'These people:\n\n%s\n\nWould have received this:\n\n%s' % (
	                self.recipients(), self.body
	            )
	            self.subject = u'Staging: ' + unicode(self.subject)
	            self.to = admin_addresses
	            self.bcc = []
        
	        return super(EmailMessage, self).message()


	def send_mass_mail(datatuple, fail_silently=False, auth_user=None,
	    auth_password=None
	):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password, fail_silently=fail_silently
	    )
	    messages = [
	        EmailMessage(subject, message, sender, recipient)
	        for subject, message, sender, recipient in datatuple
	    ]
	    return connection.send_messages(messages)


	def send_mail(subject, message, from_email, recipient_list,
	              fail_silently=False, auth_user=None, auth_password=None):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password,
	        fail_silently=fail_silently
	    )
	    return EmailMessage(
	        subject, message, from_email, recipient_list,
	        connection=connection
	    ).send()


#### Okay what does this do?

I added a setting *STAGING* to my *settings.py* which is set to *True* on the staging system (makes sense no?). That setting controls if emails are actually send to the original receivers or if all outgoing mail is sent to the admins only.

Of course that only works for cases in which you use your own *EmailMessage*, *send_mass_mail* and *send_mail* class and functions.
title: Make Django Send Mails to Admins Only
slug: make-django-send-mails-admins-only
date: 2009-08-19 08:33
tags: django, python

Image you are running a staging system for your Django project on which all the testing for the production system is done. You are using a dump of the production database to have some actual data you can play around with. And you have this one/many function/s in which you send email to some/all users. They probably will not be happy to get all those emails from your staging system while not having the slightest idea what's going on.

#### The Code
Here is a solution I came up with:

	:::python
	class EmailMessage(DjangoEmailMessage):
	    """
	    Wrapper for the original DjangoEmailMessage.
	    Responsible for sending emails only to admins instead of original
	    addressees if application is in testing mode.
	    """
	    def message(self):
	        if settings.STAGING:
	            admin_addresses = zip(*settings.ADMINS)[1]
	            self.body = 'These people:\n\n%s\n\nWould have received this:\n\n%s' % (
	                self.recipients(), self.body
	            )
	            self.subject = u'Staging: ' + unicode(self.subject)
	            self.to = admin_addresses
	            self.bcc = []
        
	        return super(EmailMessage, self).message()


	def send_mass_mail(datatuple, fail_silently=False, auth_user=None,
	    auth_password=None
	):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password, fail_silently=fail_silently
	    )
	    messages = [
	        EmailMessage(subject, message, sender, recipient)
	        for subject, message, sender, recipient in datatuple
	    ]
	    return connection.send_messages(messages)


	def send_mail(subject, message, from_email, recipient_list,
	              fail_silently=False, auth_user=None, auth_password=None):
	    """
	    Overridden to use own wrapper EmailMessage class.
	    """
	    connection = SMTPConnection(
	        username=auth_user, password=auth_password,
	        fail_silently=fail_silently
	    )
	    return EmailMessage(
	        subject, message, from_email, recipient_list,
	        connection=connection
	    ).send()


#### Okay what does this do?

I added a setting *STAGING* to my *settings.py* which is set to *True* on the staging system (makes sense no?). That setting controls if emails are actually send to the original receivers or if all outgoing mail is sent to the admins only.

Of course that only works for cases in which you use your own *EmailMessage*, *send_mass_mail* and *send_mail* class and functions.
