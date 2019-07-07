import urllib.request
import random


def load_baidu():
    url = "http://www.baidu.com"
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
        "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"
    ]

    random_user_agent = random.choice(user_agent_list)

    request = urllib.request.Request(url)

    request.add_header("User-Agent", random_user_agent)

    #response = urllib.request.urlopen(request)

    print(request.get_header("User-agent"))

load_baidu()