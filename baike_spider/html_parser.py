from bs4 import BeautifulSoup
import re
import urllib.parse   #py3+(py2--urllib2)

class HtmlParser(object):

    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r'/item/*?'))
        #https://baike.baidu.com/item/Python
        for link in links:   #逐条处理
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url,new_url)# 拼接url
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        res_data={}
        #url
        res_data['url'] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>

        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title']=title_node.get_text()

        summary_node = soup.find('div',class_='lemma-summary')
        #<div class="lemma-summary" label-module="lemmaSummary">
        res_data['summary']=summary_node.get_text()

        return res_data

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
