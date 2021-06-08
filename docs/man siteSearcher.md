% SITESEARCHER(1) Version 1.0 | Basic documentation/requirements

NAME
====

**siteSearcher** — Perform a search query on a website, and return the URL of a matching search result.


SYNOPSIS
========
 
**siteSearcher** \[**-qs**|**--query-string** "search?keyword="] \[**-rc**|**--results-container** "#searchResults"] _DOMAIN_ _KEYWORD_  
**siteSearcher** \[**-cf|--config-file** "config.yml"] _DOMAIN_ _KEYWORD_  
**siteSearcher** \[**-rn|--result-number** 3] _DOMAIN_ _KEYWORD_  
**siteSearcher** \[**-h**|**--help**|**-v**|**--version**]  

DESCRIPTION
===========
This tool performs a search query for _KEYWORD_ on the website at _DOMAIN_ based on _query-string_, then traverses the search result container DOM element matching _results-container_ and returns the URL of the first `href` found for result number _result-number_ inside the container.

_DOMAIN_ is in the format "website.extension"

A configuration file specifying _query-string_ and _results-container_ for _DOMAIN_ may be supplied. The configuration is in YAML format, and the mapping is specified as follows:


```YAML
Sites:
  domain.com:
    QueryString:	search?keyword=
    ResultsContainer:	#searchResults
```

The resulting URL is output as a string:

`https://somewebsite.com/items/your-item`

Options
-------

-h, --help

:   Prints brief usage information.

-qs, --query-string

:   Query-string to be used in combination with _KEYWORD_ in order to trigger a search query on _DOMAIN_. String.
		Example: search?keyword=  
		Required.  
		If **config-file** is specified, this option will be attempted found at `QueryString` key for _DOMAIN_ in `Sites` dict.  

-rs, --results-container

:   CSS-selector specifying the DOM element containing search results. String.  
		Example: #searchResults  
		Required.  
		If **config-file** is specified, this option will be attempted found at `ResultsContainer` key for _DOMAIN_ in `Sites` dict.  

-cf, --config-file

:   Path to a YAML file containing option configuration parameters.
		Defaults to *~/.websiteParserConfig.yml*  
    The file must be readable  

-rn, --result-number

:   Integer indecating which search result for which to return the URL. Integer.  
		Defaults to 0.

-v, --version

:   Prints the current version number.

FILES
=====

*~/.websiteParserConfig.yml*

:   YAML file containing option configuration info

BUGS
====

See GitHub Issues: <https://github.com/[owner]/[repo]/issues>

AUTHOR
======

Foobar Goodprogrammer <foo@example.org>

SEE ALSO
========

**gSheetWriter(1)**, **pageParser(1)**