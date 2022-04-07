from multiprocessing.reduction import sendfds
import re
from sys import getdlopenflags
from markupsafe import HasHTML
import requests
import fake_useragent

User_agent = fake_useragent.UserAgent()

headers = {
    "Accept": "*/*",
    "User-Agent": User_agent.random
}

url_base= "https://health-diet.ru"

req = requests.get(url=url_base, headers=headers)

# with open("index_repit.html", "w", encoding="utf8") as file_object:
#     file_object.write(req.text)

print("hello world")

lkhdf;lhdfg\HasHTMLhfgdh

getdlopenflagsdfgdf

sendfds




