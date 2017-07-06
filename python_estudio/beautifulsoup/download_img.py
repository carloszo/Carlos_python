
import urllib2
from bs4 import BeautifulSoup
import urlparse,os,requests,shutil,re
#get links of main page
def get_indexurls():
    url = 'https://www.4493.com/xingganmote/index-1.htm'
    urllist = [ 'https://www.4493.com/xingganmote/index-%d.htm'%i for i in range(1,10) ]
    res =requests.get(url)
    soup = BeautifulSoup(res.text)
    for a in soup.find_all('a',href=re.compile('\/.*\/\d{6}\/\d.*\.htm')):
        newurl = a['href']
        full_url = urlparse.urljoin(url,newurl)
        urllist.append(full_url)
    return urllist

#get urls of image page
def url_manage(url):
    urllist = []
    for i in range(1,11):
        new_url = urlparse.urljoin(url,'%d.htm'%i)
        urllist.append(new_url)
    return urllist


#download images
def download(urllist):
    for url in urllist:
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, 'html.parser', from_encoding='gb2312')
            imgurl = soup.find_all('img')[0]['src']
            fname = imgurl.split('/')[-1]
            res2 = requests.get(imgurl, stream=True)
            with open('fotos/'+fname, 'wb') as f:
                shutil.copyfileobj(res2.raw, f)
                print 'crawled'+fname
            f.close()
            del res2
        except:
            print "error"
#download()
#url = 'https://www.4493.com/xingganmote/124977/1.htm'
#urllist = url_manage(url)
#download(urllist)
#firstlist = get_indexurls()
#for url in firstlist:
    #urllist = url_manage(url)
    #download(urllist)
urllist = ['https://www.4493.com/xingganmote/index-%d.htm' % i for i in range(1, 10)]
print urllist