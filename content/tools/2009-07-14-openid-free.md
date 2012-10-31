title: OpenID for Free
slug: openid-free
date: 2009-07-14 08:55
tags: openid, php

After I see more and more sites offering [OpenID](http://openid.net/) authentication and more and more people using it I finally got interested enough to see for myself what it all is about. I didn't do so earlier because I just am getting a little paranoid and OpenID just seemed to me like giving some big, faceless company access to virtually anything I do on the web. Turns out that is not the case.

All you really have to do it set up your own ID provider which is nothing more than a smallish script (depend on which you choose/what features you need) and creating a profile for yourself/whoever you want to be able to identify.

I don't have need for much features so I chose [SimpleID](http://simpleid.sourceforge.net/), a really lightweight PHP script - hence the name. It didn't give me any problems but I still couldn't use it to auth me on bitbucket until I realized I didn't allow cookies from bitbucket (yes I really do have a paranoid streak).
