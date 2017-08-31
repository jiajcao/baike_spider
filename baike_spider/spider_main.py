import url_manager,html_downloader,html_parser,html_outputer #教程基础上去掉from baike-spider

class SpiderMain(object):

    def __init__(self):   #构造函数中初始化各个对象
        self.urls = url_manager.UrlManager()   #url管理器
        self.downloader = html_downloader.HtmlDownloader()   #下载器
        self.parser = html_parser.HtmlParser()   #解析器
        self.outputer = html_outputer.HtmlOutputer()   #输出器


    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():#如果有待爬取的url,加进url管理器
            try:
                new_url = self.urls.get_new_url()#获取一个新的url
                print('craw %d : %s' % (count,new_url))  #打印次数和url
                html_cont = self.downloader.download(new_url)#下载好的页面储存url在html-cont中
                new_url,new_data = self.parser.parse(new_url,html_cont)#下载好的页面进行解析得到新的url和数据
                self.urls.add_new_urls(new_url)#新的url补充进新的url管理器
                self.outputer.collect_data(new_data)#同时进行数据的收集
                count+=1
                if count==300:
                    break



            except Exception as e:
                print('craw failed',e)  #错误返回
        self.outputer.output_html()

if __name__=='__main__':

    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'#入口url
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)#启动爬虫
