# coding:utf-8
# url 管理器

class UrlManager(object):

    # 管理器中需要维护两个列表，一个待爬取的url列表，爬取过的url列表
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 向管理器中添加新url
    def add_new_url(self, url):
        print('添加新的url进来')
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 向管理器中批量添加url
    def add_new_urls(self, urls):
        print('批量添加新的url进来')
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.new_urls.add(url)


    # 判断管理器是否有新的待爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # url管理器中获取一个新的待爬取url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


