## Sample usage
This document provides some example of how these utilities can be used in a real-world environment.

## Standalone use
### Site searcher
*Goal: Search the site BHphotovideo.com and fetch the URL of product page for "Sony FE 24mm f/2.8 G Lens".*

Command: `siteSearcher --query-string /c/search?Ntt= --results-container [data-selenium='listingProductDetailSection'] bhphotovideo.com "Sony FE 24mm f/2.8 G Lens"`

Output: `https://www.bhphotovideo.com/c/product/1630080-REG/sony_sel24f28g_fe_24mm_f_2_8_g.html`

Explanation:  
The tool would in this case open up the search page https://www.bhphotovideo.com/c/search?Ntt=sony%2024mm%202.8, then locate the first `a href` element inside **results-container**, which is `<a data-selenium="miniProductPageProductImgLink" class="link_29FfdQHOeQOWOre_0jF7Re" href="/c/product/1630080-REG/sony_sel24f28g_fe_24mm_f_2_8_g.html"><img data-selenium="miniProductPageImg" class="image_1RwLvcJ70jHSVLOALM4UoW" src="https://static.bhphoto.com/images/images345x345/1616494845_1630080.jpg" alt="Sony FE 24mm f/2.8 G Lens"></a>` and return the full target URL, which then is output to stdout

### Page parser
*Goal: Fetch specifications (data) for the product at https://www.bhphotovideo.com/c/product/1630080-REG/sony_sel24f28g_fe_24mm_f_2_8_g.html based on the CSS-selector to datafield mappings specified in **sample-config.yaml***

Command: `pageParser --config-file config.yml https://www.bhphotovideo.com/c/product/1630080-REG/sony_sel24f28g_fe_24mm_f_2_8_g.html`

Output:  
```JSON
	{
		"ProductTitle": "Sony FE 24mm f/2.8 G Lens",
		"Price": "$598.00",
		"FocalLength": "24mm",
		"Aperture": "f/2.8",
		"Weight": "5.7 oz / 162 g",
		"URL": "https://www.bhphotovideo.com/c/product/1630080-REG/sony_sel24f28g_fe_24mm_f_2_8_g.html"
	}
```

Explanation:  
The tool will pase the DOM of the product page for the specified elements, and pull extract data of the first child element which contains text, typically using `<element>.innerText`


### GSheet writer
*Goal: Write a row to the Google sheet at https://docs.google.com/spreadsheets/d/1_4oLWc0wPmrutKIR1r75UO46PD7ZAT0voYdeIa8EYNE using input JSON object*

Command: `gSheetWriter "GSheetwriter testsheet" _data_` where _data_ is the JSON object defined above.  
Output: A row in the sheet, as defined in row 2 of https://docs.google.com/spreadsheets/d/1_4oLWc0wPmrutKIR1r75UO46PD7ZAT0voYdeIa8EYNE

Explanation: A new row is created for the object. Then the program searches the header row for cells with content matching input JSON key-names, and writes values to the corresponding row cell. If key-name is not found in the header row, it is created (appended) as the last column.

### Combined use
I envision to use these tools in combination, in a manner such as this:

`siteSearcher "Sigma Sony 24-70 2.8" bhphotovideo | pageParser | gSheetWriter "Photogear"`