#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'J\xe9r\xe9mie Jost'
SITENAME = u'Jérémie Jost'
SITEURL = ''

THEME = 'crowsfoot'

# Theme-specific config
EMAIL_ADDRESS = 'jeremiejost@gmail.com'
GITHUB_ADDRESS = 'https://github.com/jjst/'
SO_ADDRESS = 'http://stackoverflow.com/users/887422/jjst'
TWITTER_ADDRESS = 'https://twitter.com/j_jost'

PATH = 'content'

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = u'en'

DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True