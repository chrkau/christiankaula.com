title: Clear Up Gelato CMS' Gibberish
slug: clear-gelato-cms-gibberish
date: 2009-09-05 12:14
tags: gelato, php

My search for a nice and easy tumble blog I can host myself lead me in a pretty straight line to [Gelato CMS](http://gelatocms.com/). But when I looked into the database after I had been playing around with it a bit I saw that all umlauts (äöü for you non-umlaut knowing ignoramus people) turned to garbage.

After I had tried to change the database collation a few times (gotta love MySQL for having like a bangzillion of encodings) I struck me that Gelato probably just didn't talk UTF8 to the database. A few minutes of code review later (heck who writes code in Spanish or Italian or whatever that is? and encodes it in latin?!) I came up with a minimal patch that makes Gelato speak proper UTF8.

In the file *gelato/classes/mysql_conenction.class.php* search for the function *conectar* and change the return lines (around line 64) to this:

	:::php
	<?php
	mysql_query("SET NAMES utf8;", $this->mid_conexion);		
	return $this->mid_conexion;
	?>
title: Clear Up Gelato CMS' Gibberish
slug: clear-gelato-cms-gibberish
date: 2009-09-05 12:14
tags: gelato, php

My search for a nice and easy tumble blog I can host myself lead me in a pretty straight line to [Gelato CMS](http://gelatocms.com/). But when I looked into the database after I had been playing around with it a bit I saw that all umlauts (äöü for you non-umlaut knowing ignoramus people) turned to garbage.

After I had tried to change the database collation a few times (gotta love MySQL for having like a bangzillion of encodings) I struck me that Gelato probably just didn't talk UTF8 to the database. A few minutes of code review later (heck who writes code in Spanish or Italian or whatever that is? and encodes it in latin?!) I came up with a minimal patch that makes Gelato speak proper UTF8.

In the file *gelato/classes/mysql_conenction.class.php* search for the function *conectar* and change the return lines (around line 64) to this:

	:::php
	<?php
	mysql_query("SET NAMES utf8;", $this->mid_conexion);		
	return $this->mid_conexion;
	?>
title: Clear Up Gelato CMS' Gibberish
slug: clear-gelato-cms-gibberish
date: 2009-09-05 12:14
tags: gelato, php

My search for a nice and easy tumble blog I can host myself lead me in a pretty straight line to [Gelato CMS](http://gelatocms.com/). But when I looked into the database after I had been playing around with it a bit I saw that all umlauts (äöü for you non-umlaut knowing ignoramus people) turned to garbage.

After I had tried to change the database collation a few times (gotta love MySQL for having like a bangzillion of encodings) I struck me that Gelato probably just didn't talk UTF8 to the database. A few minutes of code review later (heck who writes code in Spanish or Italian or whatever that is? and encodes it in latin?!) I came up with a minimal patch that makes Gelato speak proper UTF8.

In the file *gelato/classes/mysql_conenction.class.php* search for the function *conectar* and change the return lines (around line 64) to this:

	:::php
	<?php
	mysql_query("SET NAMES utf8;", $this->mid_conexion);		
	return $this->mid_conexion;
	?>
title: Clear Up Gelato CMS' Gibberish
slug: clear-gelato-cms-gibberish
date: 2009-09-05 12:14
tags: gelato, php

My search for a nice and easy tumble blog I can host myself lead me in a pretty straight line to [Gelato CMS](http://gelatocms.com/). But when I looked into the database after I had been playing around with it a bit I saw that all umlauts (äöü for you non-umlaut knowing ignoramus people) turned to garbage.

After I had tried to change the database collation a few times (gotta love MySQL for having like a bangzillion of encodings) I struck me that Gelato probably just didn't talk UTF8 to the database. A few minutes of code review later (heck who writes code in Spanish or Italian or whatever that is? and encodes it in latin?!) I came up with a minimal patch that makes Gelato speak proper UTF8.

In the file *gelato/classes/mysql_conenction.class.php* search for the function *conectar* and change the return lines (around line 64) to this:

	:::php
	<?php
	mysql_query("SET NAMES utf8;", $this->mid_conexion);		
	return $this->mid_conexion;
	?>
title: Clear Up Gelato CMS' Gibberish
slug: clear-gelato-cms-gibberish
date: 2009-09-05 12:14
tags: gelato, php

My search for a nice and easy tumble blog I can host myself lead me in a pretty straight line to [Gelato CMS](http://gelatocms.com/). But when I looked into the database after I had been playing around with it a bit I saw that all umlauts (äöü for you non-umlaut knowing ignoramus people) turned to garbage.

After I had tried to change the database collation a few times (gotta love MySQL for having like a bangzillion of encodings) I struck me that Gelato probably just didn't talk UTF8 to the database. A few minutes of code review later (heck who writes code in Spanish or Italian or whatever that is? and encodes it in latin?!) I came up with a minimal patch that makes Gelato speak proper UTF8.

In the file *gelato/classes/mysql_conenction.class.php* search for the function *conectar* and change the return lines (around line 64) to this:

	:::php
	<?php
	mysql_query("SET NAMES utf8;", $this->mid_conexion);		
	return $this->mid_conexion;
	?>
title: Clear Up Gelato CMS' Gibberish
slug: clear-gelato-cms-gibberish
date: 2009-09-05 12:14
tags: gelato, php

My search for a nice and easy tumble blog I can host myself lead me in a pretty straight line to [Gelato CMS](http://gelatocms.com/). But when I looked into the database after I had been playing around with it a bit I saw that all umlauts (äöü for you non-umlaut knowing ignoramus people) turned to garbage.

After I had tried to change the database collation a few times (gotta love MySQL for having like a bangzillion of encodings) I struck me that Gelato probably just didn't talk UTF8 to the database. A few minutes of code review later (heck who writes code in Spanish or Italian or whatever that is? and encodes it in latin?!) I came up with a minimal patch that makes Gelato speak proper UTF8.

In the file *gelato/classes/mysql_conenction.class.php* search for the function *conectar* and change the return lines (around line 64) to this:

	:::php
	<?php
	mysql_query("SET NAMES utf8;", $this->mid_conexion);		
	return $this->mid_conexion;
	?>
title: Clear Up Gelato CMS' Gibberish
slug: clear-gelato-cms-gibberish
date: 2009-09-05 12:14
tags: gelato, php

My search for a nice and easy tumble blog I can host myself lead me in a pretty straight line to [Gelato CMS](http://gelatocms.com/). But when I looked into the database after I had been playing around with it a bit I saw that all umlauts (äöü for you non-umlaut knowing ignoramus people) turned to garbage.

After I had tried to change the database collation a few times (gotta love MySQL for having like a bangzillion of encodings) I struck me that Gelato probably just didn't talk UTF8 to the database. A few minutes of code review later (heck who writes code in Spanish or Italian or whatever that is? and encodes it in latin?!) I came up with a minimal patch that makes Gelato speak proper UTF8.

In the file *gelato/classes/mysql_conenction.class.php* search for the function *conectar* and change the return lines (around line 64) to this:

	:::php
	<?php
	mysql_query("SET NAMES utf8;", $this->mid_conexion);		
	return $this->mid_conexion;
	?>
title: Clear Up Gelato CMS' Gibberish
slug: clear-gelato-cms-gibberish
date: 2009-09-05 12:14
tags: gelato, php

My search for a nice and easy tumble blog I can host myself lead me in a pretty straight line to [Gelato CMS](http://gelatocms.com/). But when I looked into the database after I had been playing around with it a bit I saw that all umlauts (äöü for you non-umlaut knowing ignoramus people) turned to garbage.

After I had tried to change the database collation a few times (gotta love MySQL for having like a bangzillion of encodings) I struck me that Gelato probably just didn't talk UTF8 to the database. A few minutes of code review later (heck who writes code in Spanish or Italian or whatever that is? and encodes it in latin?!) I came up with a minimal patch that makes Gelato speak proper UTF8.

In the file *gelato/classes/mysql_conenction.class.php* search for the function *conectar* and change the return lines (around line 64) to this:

	:::php
	<?php
	mysql_query("SET NAMES utf8;", $this->mid_conexion);		
	return $this->mid_conexion;
	?>
