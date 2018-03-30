import multiprocessing as mp
import threading as td
from bs4 import BeautifulSoup as bs
import urllib,re
from multiprocessing import Queue
#!/usr/bin/python
#-*- coding:utf8 -*-
# def job(a,b):
#     print(a**b)
#queue
def job(q):
    res = 0
    for i in range(1000):
        res+=i+i**2+i**3
    q.put(res)

def parser(q):
    url = 'http://www.dytt8.net'
    html = urllib.urlopen(url).read()
    soup = bs(html,'lxml')
    urls=soup.findAll('a')
    for url in urls:
        q.put(url)

if __name__=='__main__':
    # t1 = td.Thread(target=job,args=(100,2))
    # t1.start()
    # t1.join()
    # m1=mp.Process(target=job,args=(30,80))
    # m1.start()
    # m1.join()
    # q = mp.Queue()
    # p1 = mp.Process(target=job,args=(q,))
    # p2 = mp.Process(target=job, args=(q,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    # res1 = q.get()
    # res2 = q.get()
    # print(res1+res2)
    q = mp.Queue()
    p1 = mp.Process(target=parser,args=(q,))
    p1.start()
    p1.join()
    res1 = q.get()
    print(res1)

