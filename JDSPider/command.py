"""终端命令行 操作py文件"""
import os
START_SHELL = 'scrapy shell {}'
START_GOOD_SPIDER = 'scrapy crawl JSearch -a keyword={} -a max_page={} -o {}'
START_COMMENT_SPIDER = 'scrapy crawl JComment -a csv_path={} -o {}'


class Command:
    @classmethod
    def start_shell(cls, url: str):
        return os.system(START_SHELL.format(url))

    @classmethod
    def start_good_spider(cls, keyword, max_page, save):
        return os.system(START_GOOD_SPIDER.format(keyword, max_page, save))

    @classmethod
    def start_comment_spider(cls, csv_path, save):
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)

        return os.system(START_COMMENT_SPIDER.format(csv_path, save))


command = Command()
