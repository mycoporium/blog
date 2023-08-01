AUTHOR = 'Aaron Eyer'
SITENAME = 'Mycoporium Lab Notes'
SITEURL = 'https://blog.mycoporium.com'

PATH = 'content'
STATIC_PATHS = ['images']
TIMEZONE = 'America/New_York'

DEFAULT_METADATA = {
    'status': 'draft',
}

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ('North Spore', 'https://northspore.com'),
        ('FreshCap', 'https://freshcap.com'),
        ('AdaFruit', 'https://www.adafruit.com/'),
        ('McMaster-Carr', 'https://www.mcmaster.com'),
        ('Grainer', 'https://www.grainger.com/'),
        )

# Social widget
SOCIAL = (
        ('YouTube', 'https://www.youtube.com/@Mycoporium'),
        )

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
