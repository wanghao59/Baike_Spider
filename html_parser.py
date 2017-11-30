# html解析器

from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin,unquote


class HtmlParser(object):
    # 获取下载下来文件的的待爬取链接
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/\S+"))
        # print(unquote(links))
        print(links)
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    # 根据链接获取爬取下来文本里面有用的资料
    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url
        
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1></dd>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary"></div>
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data

    # 解析连接地址和文本内容
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data
    