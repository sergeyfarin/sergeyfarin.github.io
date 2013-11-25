#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sergey Farin'
CONTACT = u'Sergey.Farin@gmail.com'
AUTHOR_EMAIL = u'Sergey.Farin@gmail.com'
SITENAME = u'Sergey Farin'
ABOUT = u'Reservoir Engineer'
SITE_DESCRIPTION = u'My notes on Petroleum and Reservoir Engineering, using python in my job'
SITEURL = ''

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'

PATH = 'content'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
}
}

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '/users/Sergey/anaconda/pelican-themes/pure'
PLUGIN_PATH = '/users/Sergey/anaconda/pelican-plugins'
PLUGINS = ['assets', 'sitemap', 'gravatar']
GOOGLE_PLUSONE = False

GPLUS_INTEGRATION_ENABLED = True
GPLUS_USERNAME = 'SergeyFarin'
GPLUS_API_ACCESS = '776749055184'
