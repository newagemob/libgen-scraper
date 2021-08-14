
libgen_scraper:
search any author or scholar on LibGen.be + download their publications

currently able to access libgen through `libgen-api` (`pip install libgen-api` | https://pypi.org/project/libgen-api/)

open with `python3 scrape_main.py`, i wrote a small input loop only asking for author's name at the moment, but the api has plenty of calls to utilize. the search results save to a txt file in /library_collect, but they should be csv probably. i thought it was json at first, but the keys are in quotations. i haven't really messed with data scraping too much.

the main problem right now is delimiting the strings in the author's text files and calling + downloading the URL / assigning the URL's local file destination

i need to separate the functionality between py files to use them as modules for future projects


tried to implement a headless browser (pyppeteer or puppeteerjs) but i deleted them and just stuck with the terminal interface.
