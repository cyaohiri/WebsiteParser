import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

import bs4
import requests
import yaml


if 'idlelib' in sys.modules:
    sys.argv = [sys.argv[0], 'https://www.fjellsport.no/pit-viper-the-radical-polarized-polarized-unisex.html',
                '-if', 'urls.txt', '-cf', './config.yaml']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',

}


parser = argparse.ArgumentParser(description='Pulls data from a web-page in JSON format according to a specified CSS-selector to field mapping')
parser.add_argument('URL', type=str, default=None)
parser.add_argument('-if', '--input-file', type=str, default=None,
                    help='path to a text file containing a list of URLs to parse, separated by newline')

parser.add_argument('-cf', '--config-file', type=str, default='~/.websiteParserConfig.yml',
                    help='path to a YAML file containing the desired element-to-field mapping; defaults to ~/.websiteParserConfig.yml')
parser.add_argument('-v', '--version', action='version', version='PageParser 0.1',
                    help='print the current version number.')

args = parser.parse_args()
print(args)
with open(args.config_file) as f:
    config = yaml.safe_load(f)
    print(json.dumps(config, indent=2))

with open(args.input_file) as f:
    urls = f.read().strip().split('\n')

direct_url = args.URL
print(direct_url)
if False:
    r = requests.get(direct_url, headers=headers)
    with open('product.html', 'wb') as f:
        f.write(r.content)
    soup = bs4.BeautifulSoup(r.content, 'lxml')
else:
    with open('product.html', 'rb') as f:
        soup = bs4.BeautifulSoup(f.read(), 'lxml')

print(soup.title.text)
entry = {}
for site, mapping in config['Sites'].items():
    if site in direct_url:
        for k, v in mapping.items():
            try:
                entry[k] = soup.select(v)[0].text.strip()
            except Exception as e:
                entry[k] = ''
        break
entry['URL'] = direct_url
print(json.dumps(entry, indent=2))


