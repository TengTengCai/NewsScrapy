import json
import re


def foo1():
    pattern = re.compile(r'a/\d+_\d+\?*.+')
    match = pattern.search(
        'http://www.sohu.com/a/239133638_267106?g=0?code=b8d9554f5d683833dad5be9ff3af908a&_f=index_cpc_1_0')
    if match:
        # 使用Match获得分组信息
        print(match.group())
    pass


def foo2():
    pattern = re.compile(r'cd.qq.com/\w+/\d+/\d+\.htm.*')
    match = pattern.search('http://cd.qq.com/a/20180713/005865.htm#p=1')
    if match:
        print(match.group())


def foo3():
    pattern = re.compile(r'news.qq.com/\w+/\d+/\d+\.htm')
    match = pattern.search('https://news.qq.com/a/20180714/009818.htm')
    if match:
        print(match.group())


def foo4():
    data = 'window.DATA = {"article_id":"20180714A0CP3W","article_type":"0","title":"织牢织密打击电信诈骗的天网","tags":"腾讯,腾讯网,腾讯新闻","media":"光明日报","media_id":"5024155","pubtime":"2018-07-14 09:13:32","comment_id":"2873377475","political":0,"content":"","content_ext":""}'
    json_str = str(data).split('=')[1]
    mydict = json.loads(json_str, encoding='utf-8')
    print(type(mydict))
    print(mydict['pubtime'])


def main():
    foo4()


if __name__ == '__main__':
    main()
