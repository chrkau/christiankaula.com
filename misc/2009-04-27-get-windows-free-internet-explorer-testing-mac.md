title: Get Windows for Free (For Internet Explorer Testing on Mac)
slug: get-windows-free-internet-explorer-testing-mac
date: 2009-04-27 14:18
tags: mac, windows, virtualbox, theunarchiver

Alright so you're one of those web developer/web designer guys, too? And you're on a Mac and still need to test those websites on the loathed abomination known as Internet Explorer? If you don't want to shell out any money to be able to do what you probably hate here's a quick guide:

Microsoft has those neat [virtual images for most versions of Internet Explorer](http://www.microsoft.com/downloads/details.aspx?FamilyId=21EABB90-958F-4B64-B5F1-73D0A413C8EF&displaylang=en
). Get one. The exe file can be unpacked with [The Unarchiver](http://wakaba.c3.cx/s/apps/unarchiver.html), which is free and GPL and all kinds of nice. You can use whatever you like instead of course.

While you're at it grab a copy of [VirtualBox](http://www.virtualbox.org/). Don't worry its free, too.

Once you got all the basic stuff you can add the now unpacked virtual image file to VirtualBox. You can do that in the *Image Manger* or something. In any case you open the dialog with command-d. After you added it you create a new virtual machine and it will probably offer you your just added image as primary partition. Just say yes and click through the process.

If you start your shiny new Windows image you will most likely get a bluescreen telling you something about some <em>processr.sys</em> error that just crashed your system to bits. But don't give up just yet.

Instead fire up regedit and search for <em>HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Processor</em>. Change the value of *Start* to 4.

Now you should be able to start your virtual Windows. But you still won't be able to access any network stuff since the Microsoft image is missing network drivers. And this is the hardest part. You need to get a hold of a file called <em>pcntpci5.sys</em>. I had no luck finding it online so I had to grab it from an existing Windows installation. You will probably find it somewhere in <em>C:\\windows\\system32\\drivers</em> or something. Sorry I can't remember the exact location right now.

And once you jumped through all these loops its time to lean back and enjoy your brand new free windows installation (for web testing purposes). Now wasn't that easy?

Original links:

* [Running IE6, IE7 and IE8 on your Mac](http://blog.mozmonkey.com/2008/vpc-ie6-ie7-ie8-on-mac-os-x/)
* [Problems with Intelppm.sys and processr.sys under Virtual PC / Virtual Server](http://blogs.msdn.com/virtual_pc_guy/archive/2005/10/24/484461.aspx)  

title: Get Windows for Free (For Internet Explorer Testing on Mac)
slug: get-windows-free-internet-explorer-testing-mac
date: 2009-04-27 14:18
tags: mac, windows, virtualbox, theunarchiver

Alright so you're one of those web developer/web designer guys, too? And you're on a Mac and still need to test those websites on the loathed abomination known as Internet Explorer? If you don't want to shell out any money to be able to do what you probably hate here's a quick guide:

Microsoft has those neat [virtual images for most versions of Internet Explorer](http://www.microsoft.com/downloads/details.aspx?FamilyId=21EABB90-958F-4B64-B5F1-73D0A413C8EF&displaylang=en
). Get one. The exe file can be unpacked with [The Unarchiver](http://wakaba.c3.cx/s/apps/unarchiver.html), which is free and GPL and all kinds of nice. You can use whatever you like instead of course.

While you're at it grab a copy of [VirtualBox](http://www.virtualbox.org/). Don't worry its free, too.

Once you got all the basic stuff you can add the now unpacked virtual image file to VirtualBox. You can do that in the *Image Manger* or something. In any case you open the dialog with command-d. After you added it you create a new virtual machine and it will probably offer you your just added image as primary partition. Just say yes and click through the process.

If you start your shiny new Windows image you will most likely get a bluescreen telling you something about some <em>processr.sys</em> error that just crashed your system to bits. But don't give up just yet.

Instead fire up regedit and search for <em>HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Processor</em>. Change the value of *Start* to 4.

Now you should be able to start your virtual Windows. But you still won't be able to access any network stuff since the Microsoft image is missing network drivers. And this is the hardest part. You need to get a hold of a file called <em>pcntpci5.sys</em>. I had no luck finding it online so I had to grab it from an existing Windows installation. You will probably find it somewhere in <em>C:\\windows\\system32\\drivers</em> or something. Sorry I can't remember the exact location right now.

And once you jumped through all these loops its time to lean back and enjoy your brand new free windows installation (for web testing purposes). Now wasn't that easy?

Original links:

* [Running IE6, IE7 and IE8 on your Mac](http://blog.mozmonkey.com/2008/vpc-ie6-ie7-ie8-on-mac-os-x/)
* [Problems with Intelppm.sys and processr.sys under Virtual PC / Virtual Server](http://blogs.msdn.com/virtual_pc_guy/archive/2005/10/24/484461.aspx)  

title: Get Windows for Free (For Internet Explorer Testing on Mac)
slug: get-windows-free-internet-explorer-testing-mac
date: 2009-04-27 14:18
tags: mac, windows, virtualbox, theunarchiver

Alright so you're one of those web developer/web designer guys, too? And you're on a Mac and still need to test those websites on the loathed abomination known as Internet Explorer? If you don't want to shell out any money to be able to do what you probably hate here's a quick guide:

Microsoft has those neat [virtual images for most versions of Internet Explorer](http://www.microsoft.com/downloads/details.aspx?FamilyId=21EABB90-958F-4B64-B5F1-73D0A413C8EF&displaylang=en
). Get one. The exe file can be unpacked with [The Unarchiver](http://wakaba.c3.cx/s/apps/unarchiver.html), which is free and GPL and all kinds of nice. You can use whatever you like instead of course.

While you're at it grab a copy of [VirtualBox](http://www.virtualbox.org/). Don't worry its free, too.

Once you got all the basic stuff you can add the now unpacked virtual image file to VirtualBox. You can do that in the *Image Manger* or something. In any case you open the dialog with command-d. After you added it you create a new virtual machine and it will probably offer you your just added image as primary partition. Just say yes and click through the process.

If you start your shiny new Windows image you will most likely get a bluescreen telling you something about some <em>processr.sys</em> error that just crashed your system to bits. But don't give up just yet.

Instead fire up regedit and search for <em>HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Processor</em>. Change the value of *Start* to 4.

Now you should be able to start your virtual Windows. But you still won't be able to access any network stuff since the Microsoft image is missing network drivers. And this is the hardest part. You need to get a hold of a file called <em>pcntpci5.sys</em>. I had no luck finding it online so I had to grab it from an existing Windows installation. You will probably find it somewhere in <em>C:\\windows\\system32\\drivers</em> or something. Sorry I can't remember the exact location right now.

And once you jumped through all these loops its time to lean back and enjoy your brand new free windows installation (for web testing purposes). Now wasn't that easy?

Original links:

* [Running IE6, IE7 and IE8 on your Mac](http://blog.mozmonkey.com/2008/vpc-ie6-ie7-ie8-on-mac-os-x/)
* [Problems with Intelppm.sys and processr.sys under Virtual PC / Virtual Server](http://blogs.msdn.com/virtual_pc_guy/archive/2005/10/24/484461.aspx)  

title: Get Windows for Free (For Internet Explorer Testing on Mac)
slug: get-windows-free-internet-explorer-testing-mac
date: 2009-04-27 14:18
tags: mac, windows, virtualbox, theunarchiver

Alright so you're one of those web developer/web designer guys, too? And you're on a Mac and still need to test those websites on the loathed abomination known as Internet Explorer? If you don't want to shell out any money to be able to do what you probably hate here's a quick guide:

Microsoft has those neat [virtual images for most versions of Internet Explorer](http://www.microsoft.com/downloads/details.aspx?FamilyId=21EABB90-958F-4B64-B5F1-73D0A413C8EF&displaylang=en
). Get one. The exe file can be unpacked with [The Unarchiver](http://wakaba.c3.cx/s/apps/unarchiver.html), which is free and GPL and all kinds of nice. You can use whatever you like instead of course.

While you're at it grab a copy of [VirtualBox](http://www.virtualbox.org/). Don't worry its free, too.

Once you got all the basic stuff you can add the now unpacked virtual image file to VirtualBox. You can do that in the *Image Manger* or something. In any case you open the dialog with command-d. After you added it you create a new virtual machine and it will probably offer you your just added image as primary partition. Just say yes and click through the process.

If you start your shiny new Windows image you will most likely get a bluescreen telling you something about some <em>processr.sys</em> error that just crashed your system to bits. But don't give up just yet.

Instead fire up regedit and search for <em>HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Processor</em>. Change the value of *Start* to 4.

Now you should be able to start your virtual Windows. But you still won't be able to access any network stuff since the Microsoft image is missing network drivers. And this is the hardest part. You need to get a hold of a file called <em>pcntpci5.sys</em>. I had no luck finding it online so I had to grab it from an existing Windows installation. You will probably find it somewhere in <em>C:\\windows\\system32\\drivers</em> or something. Sorry I can't remember the exact location right now.

And once you jumped through all these loops its time to lean back and enjoy your brand new free windows installation (for web testing purposes). Now wasn't that easy?

Original links:

* [Running IE6, IE7 and IE8 on your Mac](http://blog.mozmonkey.com/2008/vpc-ie6-ie7-ie8-on-mac-os-x/)
* [Problems with Intelppm.sys and processr.sys under Virtual PC / Virtual Server](http://blogs.msdn.com/virtual_pc_guy/archive/2005/10/24/484461.aspx)  

title: Get Windows for Free (For Internet Explorer Testing on Mac)
slug: get-windows-free-internet-explorer-testing-mac
date: 2009-04-27 14:18
tags: mac, windows, virtualbox, theunarchiver

Alright so you're one of those web developer/web designer guys, too? And you're on a Mac and still need to test those websites on the loathed abomination known as Internet Explorer? If you don't want to shell out any money to be able to do what you probably hate here's a quick guide:

Microsoft has those neat [virtual images for most versions of Internet Explorer](http://www.microsoft.com/downloads/details.aspx?FamilyId=21EABB90-958F-4B64-B5F1-73D0A413C8EF&displaylang=en
). Get one. The exe file can be unpacked with [The Unarchiver](http://wakaba.c3.cx/s/apps/unarchiver.html), which is free and GPL and all kinds of nice. You can use whatever you like instead of course.

While you're at it grab a copy of [VirtualBox](http://www.virtualbox.org/). Don't worry its free, too.

Once you got all the basic stuff you can add the now unpacked virtual image file to VirtualBox. You can do that in the *Image Manger* or something. In any case you open the dialog with command-d. After you added it you create a new virtual machine and it will probably offer you your just added image as primary partition. Just say yes and click through the process.

If you start your shiny new Windows image you will most likely get a bluescreen telling you something about some <em>processr.sys</em> error that just crashed your system to bits. But don't give up just yet.

Instead fire up regedit and search for <em>HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Processor</em>. Change the value of *Start* to 4.

Now you should be able to start your virtual Windows. But you still won't be able to access any network stuff since the Microsoft image is missing network drivers. And this is the hardest part. You need to get a hold of a file called <em>pcntpci5.sys</em>. I had no luck finding it online so I had to grab it from an existing Windows installation. You will probably find it somewhere in <em>C:\\windows\\system32\\drivers</em> or something. Sorry I can't remember the exact location right now.

And once you jumped through all these loops its time to lean back and enjoy your brand new free windows installation (for web testing purposes). Now wasn't that easy?

Original links:

* [Running IE6, IE7 and IE8 on your Mac](http://blog.mozmonkey.com/2008/vpc-ie6-ie7-ie8-on-mac-os-x/)
* [Problems with Intelppm.sys and processr.sys under Virtual PC / Virtual Server](http://blogs.msdn.com/virtual_pc_guy/archive/2005/10/24/484461.aspx)  

title: Get Windows for Free (For Internet Explorer Testing on Mac)
slug: get-windows-free-internet-explorer-testing-mac
date: 2009-04-27 14:18
tags: mac, windows, virtualbox, theunarchiver

Alright so you're one of those web developer/web designer guys, too? And you're on a Mac and still need to test those websites on the loathed abomination known as Internet Explorer? If you don't want to shell out any money to be able to do what you probably hate here's a quick guide:

Microsoft has those neat [virtual images for most versions of Internet Explorer](http://www.microsoft.com/downloads/details.aspx?FamilyId=21EABB90-958F-4B64-B5F1-73D0A413C8EF&displaylang=en
). Get one. The exe file can be unpacked with [The Unarchiver](http://wakaba.c3.cx/s/apps/unarchiver.html), which is free and GPL and all kinds of nice. You can use whatever you like instead of course.

While you're at it grab a copy of [VirtualBox](http://www.virtualbox.org/). Don't worry its free, too.

Once you got all the basic stuff you can add the now unpacked virtual image file to VirtualBox. You can do that in the *Image Manger* or something. In any case you open the dialog with command-d. After you added it you create a new virtual machine and it will probably offer you your just added image as primary partition. Just say yes and click through the process.

If you start your shiny new Windows image you will most likely get a bluescreen telling you something about some <em>processr.sys</em> error that just crashed your system to bits. But don't give up just yet.

Instead fire up regedit and search for <em>HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Processor</em>. Change the value of *Start* to 4.

Now you should be able to start your virtual Windows. But you still won't be able to access any network stuff since the Microsoft image is missing network drivers. And this is the hardest part. You need to get a hold of a file called <em>pcntpci5.sys</em>. I had no luck finding it online so I had to grab it from an existing Windows installation. You will probably find it somewhere in <em>C:\\windows\\system32\\drivers</em> or something. Sorry I can't remember the exact location right now.

And once you jumped through all these loops its time to lean back and enjoy your brand new free windows installation (for web testing purposes). Now wasn't that easy?

Original links:

* [Running IE6, IE7 and IE8 on your Mac](http://blog.mozmonkey.com/2008/vpc-ie6-ie7-ie8-on-mac-os-x/)
* [Problems with Intelppm.sys and processr.sys under Virtual PC / Virtual Server](http://blogs.msdn.com/virtual_pc_guy/archive/2005/10/24/484461.aspx)  

title: Get Windows for Free (For Internet Explorer Testing on Mac)
slug: get-windows-free-internet-explorer-testing-mac
date: 2009-04-27 14:18
tags: mac, windows, virtualbox, theunarchiver

Alright so you're one of those web developer/web designer guys, too? And you're on a Mac and still need to test those websites on the loathed abomination known as Internet Explorer? If you don't want to shell out any money to be able to do what you probably hate here's a quick guide:

Microsoft has those neat [virtual images for most versions of Internet Explorer](http://www.microsoft.com/downloads/details.aspx?FamilyId=21EABB90-958F-4B64-B5F1-73D0A413C8EF&displaylang=en
). Get one. The exe file can be unpacked with [The Unarchiver](http://wakaba.c3.cx/s/apps/unarchiver.html), which is free and GPL and all kinds of nice. You can use whatever you like instead of course.

While you're at it grab a copy of [VirtualBox](http://www.virtualbox.org/). Don't worry its free, too.

Once you got all the basic stuff you can add the now unpacked virtual image file to VirtualBox. You can do that in the *Image Manger* or something. In any case you open the dialog with command-d. After you added it you create a new virtual machine and it will probably offer you your just added image as primary partition. Just say yes and click through the process.

If you start your shiny new Windows image you will most likely get a bluescreen telling you something about some <em>processr.sys</em> error that just crashed your system to bits. But don't give up just yet.

Instead fire up regedit and search for <em>HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Processor</em>. Change the value of *Start* to 4.

Now you should be able to start your virtual Windows. But you still won't be able to access any network stuff since the Microsoft image is missing network drivers. And this is the hardest part. You need to get a hold of a file called <em>pcntpci5.sys</em>. I had no luck finding it online so I had to grab it from an existing Windows installation. You will probably find it somewhere in <em>C:\\windows\\system32\\drivers</em> or something. Sorry I can't remember the exact location right now.

And once you jumped through all these loops its time to lean back and enjoy your brand new free windows installation (for web testing purposes). Now wasn't that easy?

Original links:

* [Running IE6, IE7 and IE8 on your Mac](http://blog.mozmonkey.com/2008/vpc-ie6-ie7-ie8-on-mac-os-x/)
* [Problems with Intelppm.sys and processr.sys under Virtual PC / Virtual Server](http://blogs.msdn.com/virtual_pc_guy/archive/2005/10/24/484461.aspx)  

title: Get Windows for Free (For Internet Explorer Testing on Mac)
slug: get-windows-free-internet-explorer-testing-mac
date: 2009-04-27 14:18
tags: mac, windows, virtualbox, theunarchiver

Alright so you're one of those web developer/web designer guys, too? And you're on a Mac and still need to test those websites on the loathed abomination known as Internet Explorer? If you don't want to shell out any money to be able to do what you probably hate here's a quick guide:

Microsoft has those neat [virtual images for most versions of Internet Explorer](http://www.microsoft.com/downloads/details.aspx?FamilyId=21EABB90-958F-4B64-B5F1-73D0A413C8EF&displaylang=en
). Get one. The exe file can be unpacked with [The Unarchiver](http://wakaba.c3.cx/s/apps/unarchiver.html), which is free and GPL and all kinds of nice. You can use whatever you like instead of course.

While you're at it grab a copy of [VirtualBox](http://www.virtualbox.org/). Don't worry its free, too.

Once you got all the basic stuff you can add the now unpacked virtual image file to VirtualBox. You can do that in the *Image Manger* or something. In any case you open the dialog with command-d. After you added it you create a new virtual machine and it will probably offer you your just added image as primary partition. Just say yes and click through the process.

If you start your shiny new Windows image you will most likely get a bluescreen telling you something about some <em>processr.sys</em> error that just crashed your system to bits. But don't give up just yet.

Instead fire up regedit and search for <em>HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Processor</em>. Change the value of *Start* to 4.

Now you should be able to start your virtual Windows. But you still won't be able to access any network stuff since the Microsoft image is missing network drivers. And this is the hardest part. You need to get a hold of a file called <em>pcntpci5.sys</em>. I had no luck finding it online so I had to grab it from an existing Windows installation. You will probably find it somewhere in <em>C:\\windows\\system32\\drivers</em> or something. Sorry I can't remember the exact location right now.

And once you jumped through all these loops its time to lean back and enjoy your brand new free windows installation (for web testing purposes). Now wasn't that easy?

Original links:

* [Running IE6, IE7 and IE8 on your Mac](http://blog.mozmonkey.com/2008/vpc-ie6-ie7-ie8-on-mac-os-x/)
* [Problems with Intelppm.sys and processr.sys under Virtual PC / Virtual Server](http://blogs.msdn.com/virtual_pc_guy/archive/2005/10/24/484461.aspx)  

