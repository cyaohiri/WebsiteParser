% PAGEPARSER(1) Version 1.0 | Basic documentation/requirements

NAME
====

**pageParser** — Pulls data from a web-page in JSON format according to a specified CSS-selector to field mapping


SYNOPSIS
========

**pageParser** _URL_  
**pageParser** \[**-cf**|**--config-file** config.yml] _URL_  
**pageParser** \[**-if**|**--input-file** urls.txt]  
**pageParser** \[**-h**|**--help**|**-v**|**--version**]  

DESCRIPTION
===========

This tool searches the DOM of the webpage at _URL_ using CSS selectors in the element-to-field mapping specific to the domain of _URL_ as specified in the configuration (_config_) file. If found, the text content of the matching DOM element, or that of the first of its children which contains any text, is extracted and returned as a JSON object, where the key matches the corresponding field name from the config file.

The configuration is in YAML format, and the mapping is specified as follows:


```YAML
Sites:
  domain.com:
    ItemName:   .itemInfo .name
    Price:      .itemInfo .price
    UpdatedAt:  span.datestamp
```

The input URL is always added to the output as the last key. The resulting data is output as JSON data in the following format:

```JSON
	{
		"ItemName": "A classic name",
		"Price": "$1000",
		"UpdatedAt": "2021-05-04",
		"URL": "<_URL_>"
	}
```

If a _inputFile_ containing a list of URLs is provided, the corresponding webpages will be parsed one by one, and the resulting data will be output as a JSON array.

Sample input file:

```
https://somesite.com/products/a-product
https://somesite.com/products/another-product
```

Example output:
```JSON
[
	{
		"URL": "https://somesite.com/products/a-product",
		"ItemName": "A product",
		"Price": "$10",
		"UpdatedAt": "2021-06-22"
	},
	{
		"URL": "https://somesite.com/products/another-product",
		"ItemName": "Another product",
		"Price": "$19",
		"UpdatedAt": "2021-08-18"
	}
]
```


Options
-------

-h, --help

:   Prints brief usage information.

-cf, --config-file

:   Path to a YAML file containing the desired element-to-field mapping  
		Defaults to *~/.websiteParserConfig.yml*  
    The file must be readable  

-if, --input-file

:   Path to a text file containing a list of URLs to parse, separated by newline  
    The file must be readable

-v, --version

:   Prints the current version number.

FILES
=====

*~/.websiteParserConfig.yml*

:   YAML file containing the desired element-to-field mapping

BUGS
====

See GitHub Issues: <https://github.com/[owner]/[repo]/issues>

AUTHOR
======

Foobar Goodprogrammer <foo@example.org>

SEE ALSO
========

**gSheetWriter(1)**, **siteSearcher(1)**