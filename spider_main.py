# coding:utf-8
# 爬虫总调度程序

# 引入各个管理器
import url_manager,html_downloader,html_parser,html_outputer

# 简单的爬虫程序
# url_manager URL管理器
# html_downloader 根据URL下载网页内容
# html_parser 下载下来的网页内容进行解析
# html_outputer 将下载的文件输出到文件里面

# 将各个功能模块拆分，其实整合在一起也是可行的，模块化更好管理


class SpiderMain(object):
    # 在构造函数中初始化，url管理器，下载器，解析器，输出器等各个对象
    def __init__(self):
        print('进来程序')
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()


    def craw(self, root_url):
        count = 1
        # 添加初始的爬虫连接
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                
                if  count == 3:
                    break

                count += 1
            except:
                print('craw failed')

        self.outputer.output_html()



# 编写main函数
# 自动执行函数，main下面也需要添加双下划线 ++
if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

