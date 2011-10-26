title: CSS is the new C - Sass is the Future
slug: css-new-c-sass-future
date: 2009-07-08 09:03
tags: css, 960gs, sass, compass

So the other day I started to look for tools that let me use variables in CSS. This mainly was because it really gets old to copy paste the same colors over and over again. Thanks to Twitter soon I was pointed in the direction of [LESS](http://lesscss.org/).

After playing around with LESS a bit I came to the conclusion that it was nice and allowed for variables and a shortened syntax but overall didn't offer enough flexibility.

Played with some more tools and finally tried [Sass](http://sass-lang.com/). And to spoil the surprise: In my humble opinion that thing is the future of CSS. It allows to use variables, mixins (which can work a bit like functions), imports and uses a syntax that reminds me of Python (which always is a major factor) and saves heaps of unnecessary typing work.

The only gripe I had with it was that it didn't allow for a *--watch* parameter that takes care of always recompiling my CSS files when the SASS source changes. But that was quickly taken care of by using [Compass](http://compass-style.org/) which sees itself as a kind of meta-framework.

Really liking the idea I dumped my [960gs](http://960.gs/) CSS files and replaced them with the 960gs Compass plugin. This really impacted my site big time - but not in a positive way. After kicking out the 960gs plugin again and reinstalling my old official CSS files all was back to normal.

Closing thoughts: We have frameworks for everything in web development today, so why not have a real one for CSS, too? I mean just think about how much CSS we write all the time - all the same stuff over and over again. And thanks to the syntax of CSS most of what we write could be put into a library and reused. That's where Sass and Compass come into play. Though Compass might not Just Work™ its approach is definitely right and should be watched closely.
