title: By the Power of CSS… I Revisit You
slug: power-css-i-revisit-you
date: 2009-06-15 09:49
tags: css, codeconventions

Thinking about my last entry about CSS I'm thinking I probably didn't really get the structure across the right way. So let me try again.

I do not first define all tags and after that all tags with IDs, classes etc. but rather I do define tags in alphabetical order from the bare tag, over the same tags that have IDs and classes to tags that are children of the current tag.

Like so:

	:::css
	div.something
	{
		/* some code */
	}

	p
	{
		/* some code */
	}

	p#singleton
	{
		/* some code */
	}

	p.special
	{
		/* some code */
	}

	p.special a
	{
		/* some code */
	}

	q
	{
		/* some code */
	}
