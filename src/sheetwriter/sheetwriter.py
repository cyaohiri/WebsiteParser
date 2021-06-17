import argparse
import json
import sys
from pathlib import Path

import gspread

def authenticate_client(path=Path('~/.gdrivecreds.json')):
    print('Authenticating client...')
    client = gspread.service_account(path)
    return client

def insert_missing_headers(worksheet: gspread.Worksheet, data: dict):
    """Read the data and add any missing columns to the remote worksheet

    Args:
        worksheet (gspread.Worksheet): [Worksheet to extend]
        data (dict): [Input data]
    """
    try:
        header = worksheet.row_values(1)
    except IndexError:
        worksheet.update_cell(1, 1, ' ')
        header = worksheet.row_values(1)
    print('Current remote header:', header)
    missing_columns = []
    for d in data:
        for key in d.keys():
            if key not in missing_columns and key not in header:
                missing_columns.append(key)

    worksheet.resize(cols=len(set(header).union(missing_columns)))
    for c in missing_columns:
        print('Inserting column:', c)
        worksheet.update_cell(1, len(header)+1, c)
        header = worksheet.row_values(1)

    header = worksheet.row_values(1)
    print('Current remote header:', header)

# used when testing in IDLE
if 'idlelib' in sys.modules:
    sys.argv = [sys.argv[0], 'GSheetwriter testsheet', 'data.json',
                '-ws', 'Sheet1', '-c', './gdrivecreds.json']

parser = argparse.ArgumentParser(description='Writes JSON data to a Google Sheets spreadsheet')
parser.add_argument('spreadsheet', type=str)
parser.add_argument('data', type=str)
parser.add_argument('-c', '--credentials', type=str, metavar='credentials', default='~/.gdrivecreds.json',
                    help='path to a JSON file containing credentials to Google Drive API; defaults to ~/.gdrivecreds.json')
parser.add_argument('-ws', '--worksheet', type=str, metavar='worksheet', default=None,
                    help='worksheet to use; defaults to first worksheet')
parser.add_argument('-d', '--dry-run', metavar='', default=False,
                    help='test the credentials and verify the input data; nothing will be written to Google Sheets')
parser.add_argument('-v', '--version', action='version', version='SheetWriter 0.1',
                    help='print the current version number')

args = parser.parse_args()
print(args)
with open(args.data) as f:
    data = json.load(f)

client = authenticate_client(args.credentials)
print(f"Using spreadsheet '{args.spreadsheet}'")
ss = client.open(args.spreadsheet)

worksheets = ss.worksheets()
worksheet = None
for ws in worksheets:
    if args.worksheet is None:
        worksheet = ws
        break
    if ws.title == args.worksheet:
        worksheet = ws
        break

if worksheet is None:
    print(f"Could not find worksheet '{args.worksheet}'")
    sys.exit(1)

if args.dry_run:
    sys.exit(0)

print(f"Using worksheet '{worksheet.title}'")
insert_missing_headers(worksheet, data)
header = worksheet.row_values(1)
print('Inserting rows...')
for row in data:
    new_row = [row[k] if k in row else '' for k in header]
    print(new_row)
    worksheet.append_row(new_row)
    # worksheet.insert_row(new_new, index=index)
print(f'Inserted {len(data)} rows')
