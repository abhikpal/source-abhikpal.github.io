#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Abhik Pal'
SITENAME = AUTHOR + '\'s Weblog'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['code', 'figs', 'images', 'favicon.ico']

DEFAULT_DATE_FORMAT = '%A %B %d, %Y'
TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

THEME = 'theme/'

PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = ['code_include', 'rst-kbd']

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = ARTICLE_URL + '.html'

PAGE_URL = '{category}/{slug}'
PAGE_SAVE_AS = PAGE_URL + '.html'

TAG_URL = 'blog/tags/{slug}'
TAG_SAVE_AS = TAG_URL + '.html'

CATEGORIES_URL = 'blog/categories/{slug}'
CATEGORIES_SAVE_AS = CATEGORIES_URL + '.html'

ARCHIVES_URL = 'blog/archives'
ARCHIVES_SAVE_AS = ARCHIVES_URL + '.html'

TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 100

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('Blog Home', SITEURL + "/"),
         ('Github', 'https://www.github.com/abhikpal'),
         ('Archives', SITEURL + "/" + ARCHIVES_URL),)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
