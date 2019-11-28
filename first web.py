import requests
import re


def getImageList():

    html = requests.get("http://www.doutula.com/photo/list").text
    reg = r'data-original="(.*?)".*?alt = "(.*?)"'
    reg = re.compile(reg,re.S)
    images_list = re.findall(reg,html)
    print(images_list)


getImageList()
