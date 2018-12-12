import random
import urllib.request
import time

nameNum = 0

def download_web_image(url , nameNum):
    flag = False
    while (flag == False):
     name = "ROB BOSS" + str(nameNum)
     full_name = str(name) + ".jpg"
     urllib.request.urlretrieve(url, full_name)
     flag = True
X = 0
while (X < 10000):
    download_web_image("http://4.bp.blogspot.com/-JN3YMkPVSno/UagO7AjIH-I/AAAAAAAAZaU/ZODabmUqp3U/s1600/rob_boss.jpg" , nameNum )
    X = X + 1
    nameNum = nameNum + 1
