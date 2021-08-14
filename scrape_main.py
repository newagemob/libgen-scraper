""" Library Genesis scraper pulling any requested author's published works hosted on the site. """

"""
USE PUPPETEER JS HEADLESS BROWSER TO DOWNNLOAD DOCUMENTS
"""

import os
from libgen_api import LibgenSearch


libSearch = LibgenSearch()

path = "/home/bluntslightyear/Developer/portfolio/lib_scrpr/library_collect/"

if not os.path.exists(path):
    os.mkdir(path)



""" write list of publications to console, download all publications to separate files in a folder titled the author's name """

def authorSearch():
    global author
    global results

    author = input("Author Name : ")
    narrow = input("Narrow Search? (Y / N)")

    if narrow == "Y" or narrow == "y" or narrow == "yes":
        authorSpec()
    else:
        pass

    results = libSearch.search_title(author)
    
    print(results)

    dlInput = input("Would you like to download " + author + "'s publications? (Y / N)")

    if dlInput == "Y" or dlInput == "y" or dlInput == "yes":
        downloadPubLinks()
    else:
        pass

    return results



def authorSpec():
    print("\n\n\n\t\tWARNING ::: this function is in beta\n\n")
    language = input("Language : ")
    year = input("Year : ")

    authorFilters = {"Language": language, "Year": year}
    filteredSearch = libSearch.search_author_filtered(i, authorFilters, exact_match=True)

    print(filteredSearch)



''' this only downloads links in key : pair values '''

def downloadPubLinks():
    authorFolder = path + author
    if not os.path.exists(authorFolder):
        os.mkdir(authorFolder)

    dlQueue = results[0]
    dlLinks = libSearch.resolve_download_links(dlQueue)

    dlPage = open(authorFolder + "/" + author + ".txt", 'w')

    print(dlLinks, file=dlPage)




authorSearch()
