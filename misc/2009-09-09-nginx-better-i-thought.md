title: Nginx is Even Better Than I Thought
slug: nginx-better-i-thought
date: 2009-09-09 08:27
tags: nginx

So for quite a few months I was pretty sure having HTTPS on multiple domains with the same IP was a no-go on nginx. [I was wrong](http://www.ruby-forum.com/topic/156637#690017).

If you have a OpenSSL version >= 0.9.8f with [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) support compiled in and a half-way recent nginx version you are good to go. Just set up as many virtual domains as needed.

Quick example from memory (I'm quite positive it is correct though):

	:::nginx
	server {
	  server_name somedomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/file.pem;
	  ssl_certificate_key /some/file.key;
	}
	server {
	  server_name someotherdomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/other/file.pem;
	  ssl_certificate_key /some/other/file.key;
	}
	server {
	  server_name evenotherdomain.example.com;
	}

Keep in mind though, that enabling SSL in any way leads to a kind of catch-all situation. Meaning if you access *https://evenotherdomain.exmaple.com* you will most likely end up on one of your SSL-enabled domains (*domedomain.example.com* or *someotherdomain.example.com*).

Here is what I did to prevent that:

	:::nginx
	server {
	  listen 443;
	  server_name evenotherdomain.example.com;
	  rewrite ^(.*) http://example.com$1 permanent;
	}
title: Nginx is Even Better Than I Thought
slug: nginx-better-i-thought
date: 2009-09-09 08:27
tags: nginx

So for quite a few months I was pretty sure having HTTPS on multiple domains with the same IP was a no-go on nginx. [I was wrong](http://www.ruby-forum.com/topic/156637#690017).

If you have a OpenSSL version >= 0.9.8f with [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) support compiled in and a half-way recent nginx version you are good to go. Just set up as many virtual domains as needed.

Quick example from memory (I'm quite positive it is correct though):

	:::nginx
	server {
	  server_name somedomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/file.pem;
	  ssl_certificate_key /some/file.key;
	}
	server {
	  server_name someotherdomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/other/file.pem;
	  ssl_certificate_key /some/other/file.key;
	}
	server {
	  server_name evenotherdomain.example.com;
	}

Keep in mind though, that enabling SSL in any way leads to a kind of catch-all situation. Meaning if you access *https://evenotherdomain.exmaple.com* you will most likely end up on one of your SSL-enabled domains (*domedomain.example.com* or *someotherdomain.example.com*).

Here is what I did to prevent that:

	:::nginx
	server {
	  listen 443;
	  server_name evenotherdomain.example.com;
	  rewrite ^(.*) http://example.com$1 permanent;
	}
title: Nginx is Even Better Than I Thought
slug: nginx-better-i-thought
date: 2009-09-09 08:27
tags: nginx

So for quite a few months I was pretty sure having HTTPS on multiple domains with the same IP was a no-go on nginx. [I was wrong](http://www.ruby-forum.com/topic/156637#690017).

If you have a OpenSSL version >= 0.9.8f with [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) support compiled in and a half-way recent nginx version you are good to go. Just set up as many virtual domains as needed.

Quick example from memory (I'm quite positive it is correct though):

	:::nginx
	server {
	  server_name somedomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/file.pem;
	  ssl_certificate_key /some/file.key;
	}
	server {
	  server_name someotherdomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/other/file.pem;
	  ssl_certificate_key /some/other/file.key;
	}
	server {
	  server_name evenotherdomain.example.com;
	}

Keep in mind though, that enabling SSL in any way leads to a kind of catch-all situation. Meaning if you access *https://evenotherdomain.exmaple.com* you will most likely end up on one of your SSL-enabled domains (*domedomain.example.com* or *someotherdomain.example.com*).

Here is what I did to prevent that:

	:::nginx
	server {
	  listen 443;
	  server_name evenotherdomain.example.com;
	  rewrite ^(.*) http://example.com$1 permanent;
	}
title: Nginx is Even Better Than I Thought
slug: nginx-better-i-thought
date: 2009-09-09 08:27
tags: nginx

So for quite a few months I was pretty sure having HTTPS on multiple domains with the same IP was a no-go on nginx. [I was wrong](http://www.ruby-forum.com/topic/156637#690017).

If you have a OpenSSL version >= 0.9.8f with [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) support compiled in and a half-way recent nginx version you are good to go. Just set up as many virtual domains as needed.

Quick example from memory (I'm quite positive it is correct though):

	:::nginx
	server {
	  server_name somedomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/file.pem;
	  ssl_certificate_key /some/file.key;
	}
	server {
	  server_name someotherdomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/other/file.pem;
	  ssl_certificate_key /some/other/file.key;
	}
	server {
	  server_name evenotherdomain.example.com;
	}

Keep in mind though, that enabling SSL in any way leads to a kind of catch-all situation. Meaning if you access *https://evenotherdomain.exmaple.com* you will most likely end up on one of your SSL-enabled domains (*domedomain.example.com* or *someotherdomain.example.com*).

Here is what I did to prevent that:

	:::nginx
	server {
	  listen 443;
	  server_name evenotherdomain.example.com;
	  rewrite ^(.*) http://example.com$1 permanent;
	}
title: Nginx is Even Better Than I Thought
slug: nginx-better-i-thought
date: 2009-09-09 08:27
tags: nginx

So for quite a few months I was pretty sure having HTTPS on multiple domains with the same IP was a no-go on nginx. [I was wrong](http://www.ruby-forum.com/topic/156637#690017).

If you have a OpenSSL version >= 0.9.8f with [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) support compiled in and a half-way recent nginx version you are good to go. Just set up as many virtual domains as needed.

Quick example from memory (I'm quite positive it is correct though):

	:::nginx
	server {
	  server_name somedomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/file.pem;
	  ssl_certificate_key /some/file.key;
	}
	server {
	  server_name someotherdomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/other/file.pem;
	  ssl_certificate_key /some/other/file.key;
	}
	server {
	  server_name evenotherdomain.example.com;
	}

Keep in mind though, that enabling SSL in any way leads to a kind of catch-all situation. Meaning if you access *https://evenotherdomain.exmaple.com* you will most likely end up on one of your SSL-enabled domains (*domedomain.example.com* or *someotherdomain.example.com*).

Here is what I did to prevent that:

	:::nginx
	server {
	  listen 443;
	  server_name evenotherdomain.example.com;
	  rewrite ^(.*) http://example.com$1 permanent;
	}
title: Nginx is Even Better Than I Thought
slug: nginx-better-i-thought
date: 2009-09-09 08:27
tags: nginx

So for quite a few months I was pretty sure having HTTPS on multiple domains with the same IP was a no-go on nginx. [I was wrong](http://www.ruby-forum.com/topic/156637#690017).

If you have a OpenSSL version >= 0.9.8f with [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) support compiled in and a half-way recent nginx version you are good to go. Just set up as many virtual domains as needed.

Quick example from memory (I'm quite positive it is correct though):

	:::nginx
	server {
	  server_name somedomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/file.pem;
	  ssl_certificate_key /some/file.key;
	}
	server {
	  server_name someotherdomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/other/file.pem;
	  ssl_certificate_key /some/other/file.key;
	}
	server {
	  server_name evenotherdomain.example.com;
	}

Keep in mind though, that enabling SSL in any way leads to a kind of catch-all situation. Meaning if you access *https://evenotherdomain.exmaple.com* you will most likely end up on one of your SSL-enabled domains (*domedomain.example.com* or *someotherdomain.example.com*).

Here is what I did to prevent that:

	:::nginx
	server {
	  listen 443;
	  server_name evenotherdomain.example.com;
	  rewrite ^(.*) http://example.com$1 permanent;
	}
title: Nginx is Even Better Than I Thought
slug: nginx-better-i-thought
date: 2009-09-09 08:27
tags: nginx

So for quite a few months I was pretty sure having HTTPS on multiple domains with the same IP was a no-go on nginx. [I was wrong](http://www.ruby-forum.com/topic/156637#690017).

If you have a OpenSSL version >= 0.9.8f with [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) support compiled in and a half-way recent nginx version you are good to go. Just set up as many virtual domains as needed.

Quick example from memory (I'm quite positive it is correct though):

	:::nginx
	server {
	  server_name somedomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/file.pem;
	  ssl_certificate_key /some/file.key;
	}
	server {
	  server_name someotherdomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/other/file.pem;
	  ssl_certificate_key /some/other/file.key;
	}
	server {
	  server_name evenotherdomain.example.com;
	}

Keep in mind though, that enabling SSL in any way leads to a kind of catch-all situation. Meaning if you access *https://evenotherdomain.exmaple.com* you will most likely end up on one of your SSL-enabled domains (*domedomain.example.com* or *someotherdomain.example.com*).

Here is what I did to prevent that:

	:::nginx
	server {
	  listen 443;
	  server_name evenotherdomain.example.com;
	  rewrite ^(.*) http://example.com$1 permanent;
	}
title: Nginx is Even Better Than I Thought
slug: nginx-better-i-thought
date: 2009-09-09 08:27
tags: nginx

So for quite a few months I was pretty sure having HTTPS on multiple domains with the same IP was a no-go on nginx. [I was wrong](http://www.ruby-forum.com/topic/156637#690017).

If you have a OpenSSL version >= 0.9.8f with [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) support compiled in and a half-way recent nginx version you are good to go. Just set up as many virtual domains as needed.

Quick example from memory (I'm quite positive it is correct though):

	:::nginx
	server {
	  server_name somedomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/file.pem;
	  ssl_certificate_key /some/file.key;
	}
	server {
	  server_name someotherdomain.example.com;
	  listen 443;

	  keepalive_timeout 70;
	  ssl on;
	  ssl_protocols SSLv3;
	  ssl_certificate /some/other/file.pem;
	  ssl_certificate_key /some/other/file.key;
	}
	server {
	  server_name evenotherdomain.example.com;
	}

Keep in mind though, that enabling SSL in any way leads to a kind of catch-all situation. Meaning if you access *https://evenotherdomain.exmaple.com* you will most likely end up on one of your SSL-enabled domains (*domedomain.example.com* or *someotherdomain.example.com*).

Here is what I did to prevent that:

	:::nginx
	server {
	  listen 443;
	  server_name evenotherdomain.example.com;
	  rewrite ^(.*) http://example.com$1 permanent;
	}
