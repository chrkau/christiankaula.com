title: On CSS structure
slug: on-css-structure
date: 2011-06-01 01:54
tags: css


Because I have to do some collaborative work on CSS files (no [Sass](http://sass-lang.com/)/[Compass](http://compass-style.org/)) these days I'd like to take the time and write down some pointers regarding CSS structure.



## Alphabetical order

As with a lot of  other stuff that needs to be organized in some way, alphabetical order makes a lot of sense. Capital letters go before lowercase letters. Top do bottom.

There's no magic to it and it makes stuff that much easier to find. Easier to find means less chance to duplicate things that are already there.



## Specificity

[Specificity](http://www.w3.org/TR/2003/WD-CSS21-20030128/cascade.html#specificity) is one of those things you usually don't think about until it bites you. In short specificity is a value calculated by the browser for every selector and used to check which one of n overlapping selectors takes precedence.

All in all you can get away with keeping a few simple rules in mind:

* class selectors beat element selectors
* id selectors beat class selectors
* combine selectors to increase the specificity



## Use newlines

I know a few guys that like to put all attributes of one selector in one line. This is bad for two reasons. First its really hard to read. Have a look at this:

	:::css
	a { width: 74px; height: 62px; float: left; position: relative; margin-top: 520px; margin-left: 0px; }

	b {
		width: 74px;
		height: 62px;
		float: left;
		position: relative;
		margin-top: 520px;
		margin-left: 0px;
	}

It should be obvious that the layout of b is much easier on the eyes.

Second reason is version control. Let's say you need to change the width in the above examples. If you change it for *b* you will end up with a diff that encompasses exactly the one line in which *width* is set. Do the same thing for *a* and the whole definition will show up as changed in the logs. Have fun figuring out what exactly was changed on that line. Not cool.



## Putting it together

What does a well structured CSS file look like then? Start with element selectors, follow with class selectors and put the id selectors in the bottom of your file. This pretty much reflects the order in which your browser will parse the CSS.

Order selector names alphabetically. So do for attributes. That way nobody gets confused and attributes won't be duplicated - or at least they are less likely to be messed up.

In the end you might end up with something like this:

	:::css
	a {
		color: blue;
		text-deocration: none;
	}
	p {…}

	.anotherClass {…}
	.someClass {…}

	#imAnId {…}
	#soAmI {…}



## Why I don't listen to my own advice

'I saw your CSS - you don't order your attributes alphabetically!' I hear you cry. And you are right. It's one of my (perhaps not so) little quirks: I like my attributes in semantic order. First the basic stuff like *width* and *height* followed by stuff concerning position like *float* and *position* (duh). After that comes *background* and text stuff in an order similar to how typographers usually specify fonts (family, weight, size, color). the last three attributes are ordered by going out of the element. First you got *padding* followed by *border* and lastly *margin*.

It probably doesn't make sense to you and I don't blame you. Stick to alphabetical ordering as the lowest common denominator and we can all get along.

