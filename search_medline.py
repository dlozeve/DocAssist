import re
import urllib.request as ur
from xml.etree import ElementTree as ET

from config import config_path


class SearchMedline(config_path):
    def __init__(self, n_results):
        config_path.__init__(self)
        self.n_results = n_results

    def cleanhtml(self,raw_html):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext

    def Medline(self, n_results=1):

        query = open(self.transcript_D, 'r').read()
        requestURL = "https://wsearch.nlm.nih.gov/ws/query?db=healthTopics&term=%%22%s%%22"%(query.replace(' ','+')) + \
                     '&retmax=%s'%str(n_results)

        root = ET.parse(ur.urlopen(requestURL)).getroot()

        results = []
        for i in range(n_results):
            d = {}
            d['rank'] = i+1
            article = root.find('list').findall(".//document[@rank='%s']"%str(i))[0]
            d['title'] = self.cleanhtml(article.findall(".//content[@name='title']")[0].text)
            d['origin'] = self.cleanhtml(article.findall(".//content[@name='organizationName']")[0].text)
            d['url'] = article.attrib["url"]
            print("%s. %s, %s, %s"%(d['rank'], d['title'], d['origin'], d['url']))

            results.append(d)

        return(results)

# if __name__ == '__main__':

    # Medline(["asthma"], n_results=1)
    # _ = Medline("chronic obstructive pulmonary disease",n_results=5)