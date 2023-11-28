import logging

from bs4 import BeautifulSoup
from pelican import signals

def add_rel_me(path, context):

    mast_user = context.setdefault('MASTODON_USER')

    if not mast_user:
        return

    with open(path, 'r') as f:
        html_data = f.read()

    bs = BeautifulSoup(html_data, 'html.parser')

    a_tags = bs.find_all('a')

    for tag in a_tags:
        if mast_user in tag['href']:
            tag['rel'] = 'me'
            logging.info('A TAG: %s', tag)

            with open(path, 'w') as f:
                f.write(str(bs))


def register():
    signals.content_written.connect(add_rel_me)
