import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

import bs4
import requests
import yaml


if 'idlelib' in sys.modules:
    sys.argv = [sys.argv[0], '-qs', '/c/search?Ntt=', '-rc', '.product_19pae40ejOyj6V7StHfjYz',
                '-cf', './config.yaml', 'bhphotovideo.com', 'aqueous']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',

}

parser = argparse.ArgumentParser(description='Perform a search query on a website, and return the URL of a matching search result.')
#parser = argparse.ArgumentParser(add_help=False)

parser.add_argument('DOMAIN', type=str, default=None)
parser.add_argument('KEYWORD', type=str, default=None)
parser.add_argument('-rc', '--results-container', type=str,
                    help='CSS-selector specifying the DOM element containing search results. Example: #searchResults')
parser.add_argument('-rn', '--result-number', type=int, default=0,
                    help='integer indicating for which search result to return the URL; defaults to 0')
parser.add_argument('-qs', '--query-string', type=str,
                    help='query string to be used in combination with KEYWORD in order to trigger a search query on DOMAIN. Example: search?keyword=')

parser.add_argument('-cf', '--config-file', type=str, default='~/.websiteParserConfig.yml',
                    help='path to a YAML file containing the desired element-to-field mapping; defaults to ~/.websiteParserConfig.yml')
parser.add_argument('-v', '--version', action='version', version='PageParser 0.1',
                    help='print the current version number.')

args = parser.parse_args()
print(args)
with open(args.config_file) as f:
    config = yaml.safe_load(f)
    print(json.dumps(config, indent=2))

# TEMP
listing_url = 'https://' + args.DOMAIN + args.query_string + args.KEYWORD
print(listing_url)
if False:
    r = requests.get(listing_url, headers=headers)
    with open('listing.html', 'wb') as f:
        f.write(r.content)
    soup = bs4.BeautifulSoup(r.content, 'lxml')
else:
    with open('listing.html', 'rb') as f:
        soup = bs4.BeautifulSoup(f.read(), 'lxml')

print(soup.title.text)
product_url = ''
for site, mapping in config['Sites'].items():
    if site in listing_url:
        listings = soup.select(mapping['ResultsContainer'])
        if len(listings) > args.result_number:
            product_url = 'https://' + site + listings[args.result_number].a['href']
        break
print(product_url)


