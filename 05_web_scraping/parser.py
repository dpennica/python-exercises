from lxml import html
import requests

page = requests.get(
    'https://www.gutenberg.org/files/52484/52484-h/52484-h.htm')
tree = html.fromstring(page.content)
