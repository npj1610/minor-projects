from npj6.scraper.cache import Cache

import lxml.html
import re

# Must be executed from folder for the import to work
# Example that outputs every Ty Segall song not in 4/4
if __name__ == "__main__":
    with Cache() as c:

        #code here

        RWT = 0.1
        name = []
        signature = []

        url = r'https://www.chords.tv/bpmkey/search.php?query=Ty+Segall'

        while url is not None:
            tree = lxml.html.fromstring(c.requestURL(url, requestWaitingTime=RWT))

            #All song links
            songs = tree.xpath('/html/body/div[2]/div[2]/div/div/div[2]/span[1]/a/@href')

            #Save songs
            for song in songs:
                songtree = lxml.html.fromstring(c.requestURL(song, requestWaitingTime=RWT))
                name.append(songtree.xpath(r"/html/body/div[2]/h1/a[1]/text()")[0])
                try:
                    signature.append(re.findall(
                        "[0-9]+/[0-9]+",
                        songtree.xpath(r"//*[contains(text(), 'ime signature')]/text()")[0]
                    ))
                except IndexError:
                    signature.append([])

            #Next page
            next = tree.xpath('/html/body/div[2]/h3[2]/span/a/@href')
            try:
                url = next[0]
            except IndexError:
                url = None

        #Filter the Data
        weird_ones = [s for s in zip(name, signature) if '4/4' not in s[1]]
        for s in weird_ones:
            print("Ty Segall - " + s[0] + "\n\t" + str(s[1]))

        #code here
