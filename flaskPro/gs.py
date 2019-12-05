import time
import requests
from lxml import etree

url = "https://so.gushiwen.org/gushi/cifu.aspx"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

response = requests.get(url,headers)

content = response.content.decode(response.apparent_encoding)

html = etree.HTML(content)

link_list = html.xpath('//div[@class="typecont"]/span/a')

headers["Referer"] = "https://so.gushiwen.org/shiwenv_ce802de625e5.aspx"

for link in link_list:
    url = "https://so.gushiwen.org"+link.attrib.get("href")
    sw_response = requests.get(url,headers)
    sw_html = etree.HTML(sw_response.content)
    content_list = sw_html.xpath('//div[@class="sons"]/div[@class="cont"]')
    for con in content_list:
        title = con.xpath("h1")
        author = con.xpath('p[@class="source"]/a[2]')
        p_list = con.xpath('div[@class="contson"]/p')
        article = ""
        description = ""
        if title:
            t = title[0].text
            a = author[0].text
            i = 0
            for p in p_list:
                if i == 0:
                    d = p.text
                    i += 1
                article += p.text
            print(d)
            url = "http://127.0.0.1:8000/Api/Article/"
            data = {
                "type": "add_article",
                "title": t,
                "author": a,
                'description': d,
                'content': article
            }
            api_response = requests.post(url,data=data)
            response = api_response.json()
            print(response)
            time.sleep(1)
        print("+++++++++++++++++++++++++")