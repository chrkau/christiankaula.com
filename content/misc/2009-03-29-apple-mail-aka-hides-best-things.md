title: Apple Mail AKA Hides-Best-Things
slug: apple-mail-aka-hides-best-things
date: 2009-03-29 14:01
tags: mac, mail

After almost getting used to Mail not supporting identities, today I finally found a way to use them too. Mail supports an infinite number of alias-sets consisting of E-mail and full name. To make Mail actually provide this feature you have to create them manually though. Here's and example entry in *~Library/Preferences/com.apple.mail.plist*:


	:::xml
	<key>MailAccounts</key>
	<array>
	  <dict>
	    <key>AccountName</key>
	    <string>User@example.com</string>
	    <key>AccountPath</key>
	    <string>~/Library/Mail/IMAP-user@example.com</string>
	    <key>AccountType</key>
	    <string>IMAPAccount</string>
	    <key>EmailAddresses</key>
	    <array>
	      <string>user@example.com</string>
	    </array>
	    <key>EmailAliases</key>
	    <array>
	      <dict>
	        <key>alias</key>
	        <string>alias1@example.com</string>
	        <key>name</key>
	        <string>Name 1</string>
	      </dict>
	      <dict>
	        <key>alias</key>
	        <string>alias2@example.com</string>
	        <key>name</key>
	        <string>Name 2</string>
	      </dict>
	    </array>
	    <key>FullUserName</key>
	    <string>Official Name</string>
	  </dict>
	</array>

By the way if you only need alias email addresses you can do that directly per user interface. Just put all the email addresses you need into the *Email Address" field separated by commas.

[Original comment by xSmurf](http://www.macosxhints.com/article.php?story=20051213200935504)
