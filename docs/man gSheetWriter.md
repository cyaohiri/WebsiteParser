% GSHEETWRITER(1) Version 1.0 | Basic documentation/requirements

NAME
====

**gSheetWriter** — Writes JSON data to a Google Sheets spreadsheet


SYNOPSIS
========

**gSheetWriter** \[**-ws**|**--work-sheet** "Inventory"] _sheetname_ _data_  
**gSheetWriter** \[**-h**|**--help**|**-v**|**--version**]

DESCRIPTION
===========

Writes _data_ to the Google Sheet _sheetname_, where _data_ is JSON data and _sheetname_ is a the name of the sheet as a String.
 
Expected data format is a single object, or array of objects, where the keys match the column header names.

Example JSON data: 
```
	[
		{
			"FirstColumn": "Data to put in first column, first row",
			"SecondColumn": "Data to put in second column, first row"
		},
		{
			"FirstColumn": "Data to put in first column, second row",
			"SecondColumn": "Data to put in second column, second row"
		}
	]
```

Options
-------

**-h, --help**

:   Prints brief usage information.

**-c, --credentials**

:   Path to a JSON file containing credentials to Google Drive API - String  
		Defaults to *~/.gdrivecreds.json*  
    The file must be readable

**-ws, --work-sheet**

:		Worksheet to use, inside of `sheetname` - String.  
		Defults to first the worksheet (index 0)

**-d, --dry-run**

:   Writes nothing to the Gsheet - just tests the connection and verifies input data


**-v, --version**

:   Prints the current version number.

FILES
=====

*~/.gdrivecreds.json*

:   JSON file containing Google Drive API credentials


ENVIRONMENT
===========

BUGS
====

See GitHub Issues: <https://github.com/[owner]/[repo]/issues>

AUTHOR
======

Foobar Goodprogrammer <foo@example.org>

SEE ALSO
========

**pageParser(1)**, **siteSearcher(1)**