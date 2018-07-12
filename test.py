import re


def main():
    pattern = re.compile(r'a/\d+_\d+\?*.+')
    match = pattern.search('http://www.sohu.com/a/239133638_267106?g=0?code=b8d9554f5d683833dad5be9ff3af908a&_f=index_cpc_1_0')
    if match:
        # 使用Match获得分组信息
        print(match.group())
    pass


if __name__ == '__main__':
    main()
