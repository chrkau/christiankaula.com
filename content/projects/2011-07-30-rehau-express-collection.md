title: REHAU Express Collection
slug: rehau-express-collection
date: 2011-07-30 16:21
tags: app, iphone, zepto, javascript, python, ux
image: rehau-ec-01.png

During my master's we had the chance to develop an app prototype for [REHAU AG + Co](http://www.rehau.com). Goal was to create a working prototype for an app that allows to browse the catalog of little plastic thingies you can put on raw borders of materials like wood ("Kantenbänder" in German – something like "edge bands" perhaps?). My group consisted of four people. My job was to do most of the coding.

The whole thing did not sound too hard until we were given the data REHAU is working with: a bunch of rather funky Excel files. While I was hacking together a Python export script I learned more than I care to know about how those *edge bands* (I'll just roll with it) are categorized.

Next we thought long and hard about how an app like this would be used and by whom and such. UX stuff you could call it. We concluded that most people using the app probably would know what they are searching for in most cases. So we built the app around the idea find-as-you-type principle.

<img src="/images/rehau-ec-02.png" alt="REHAU Express Collection screenshots 1" />


Technology wise we decided to go the [Web app](http://developer.apple.com/library/ios/#documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html) route. To keep the app as lightweight as possible I chose [Zepto.js](http://zeptojs.com/) over jQuery and came up with a minimal app/animation framework.

<img src="/images/rehau-ec-03.png" alt="REHAU Express Collection screenshots 2" />

When we presented it we suggested some caching functions – possibly involving [localStorage](http://en.wikipedia.org/wiki/Web_storage#localStorage) and the [HTML5 cache manifest](http://en.wikipedia.org/wiki/Cache_manifest_in_HTML5) – to make the app usable when offline. We also had some ideas concerning a update mechanism that only downloads deltas instead of the whole *edge band* data set. Sadly it turned out that REHAU only wanted to get some ideas and never was really interested in letting students do any real work on the app.

