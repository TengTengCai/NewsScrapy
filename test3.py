import time

from selenium import webdriver


def crawler_browser(url):
    browser = webdriver.PhantomJS()
    browser.get(url)
    time.sleep(5)
    page_str = browser.page_source
    print(page_str)


def main():
    # crawler_browser('https://www.sohu.com/a/242044382_585752?g=0?code=b72fd57c3c97b5fec0809e1b18418ad9&_f=index_cpc_0')
    crawler_browser('https://new.qq.com/omn/20180718/20180718A1MA6V.html')
    pass


if __name__ == '__main__':
    main()
