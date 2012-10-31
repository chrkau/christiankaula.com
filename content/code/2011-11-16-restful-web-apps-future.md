title: RESTful Web Applications: Code Less, Do More
slug: restful-web-applications-code-less-do-more
tags: rest, webapps, architecture
description: "A few thoughts on why a client-side assembled web architecture saves a lot of work.”


What does web development mean? Usually you build some software that gets data out of some database converts it to HTML and sends it to a browser. Usually that software has to handle the other case, too: Receive input from a browser, make sense of it and write the data into the database. There’s your average web project. 

But, since this is the age of responsive web design, AJAX and web apps, you aren’t done yet. Now you code a bunch of JavaScript, that does the same stuff client-side. Chances are good, you will have to write quite some server-side code for this, too.

Doesn’t sound very [DRY](http://en.wikipedia.org/wiki/Don%27t_repeat_yourself), you say? Some other people had the same thought. They created [frameworks](http://django-tastypie.readthedocs.org/en/latest/index.html), [environments ](http://nodejs.org/) and whole [programming languages](http://opalang.org/) to counter the problem. But why go for solutions, that are that complicated?


## REST to the rescue

Why not try this:

* Write a REST API that translates your data to JSON.
* Write a (semi-)static HTML page.
* Write JavaScript that talks to the API and translates the data for the user.
* Be done.

Some people call this client-side assembled web applications. I call it good design. It separates business logic (server-side) from the presentation layer (client-side). A bunch of benefits comes with it, for free. Want a native client for mobile devices? Just put a new interface on top of the API. Need an API for third party developers? You already got one. How about performance? Pure JSON data most likely is smaller than complete server-side rendered HTML pages.

And don’t tell me this isn’t feasible because it requires JavaScript. Even [Googlebot is JavaScript enabled](http://googlewebmastercentral.blogspot.com/2011/11/get-post-and-safely-surfacing-more-of.html) these days. [Big players](http://esn.me/showcase/battlelog/) are [doing client-side web applications](http://lucumr.pocoo.org/2011/11/15/modern-web-applications-are-here/) already. And if you say *but this is hard!*, I recommend reading up on [Backbone.js](http://documentcloud.github.com/backbone/).