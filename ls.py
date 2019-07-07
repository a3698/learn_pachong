import urllib.request
import urllib.parse
import string

def load_data():
    url = "http://www.baidu.com/s?wd="

    name = "领克"

    final_url = url + name
    print(final_url)

    #转义中文
    encode_new_url = urllib.parse.quote(final_url, safe=string.printable)

    print(encode_new_url)

    response = urllib.request.urlopen(encode_new_url)
    print(response)

    data = response.read()
    print(data)

    str_data = data.decode("utf-8")
    print(str_data)

    with open("baidu_lingke.html", "w", encoding="utf-8") as f:
        f.write(str_data)



load_data()