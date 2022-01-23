import requests
import urllib
from urllib import parse
def smallchatbot(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(msg))
    html =requests.get(url)
    content = html.json()["content"]
    con = str(content)
    c = con.replace('{br}', "\n")
    return c
while True:
    msg = input("我：")
    if (msg == "quit" or msg == "bye"):
        print("菲菲：拜拜，祝你愉快！")
        break
    res =smallchatbot(msg)

    print("菲菲：", res)
