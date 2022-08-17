from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random


pages = set()
random.seed(datetime.datetime.now())
#Truy xuất danh sách tất cả các liên kết Nội bộ được tìm thấy trên một trang
def getInternalLinks(bs, includeUrl):
    #includeUrl chính là domain
    # Tiếp túc lấy trang web gốc tìm link nội bộ
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []
    # Tìm tất cả các liên kết bắt đầu bằng "/"
    for link in bs.find_all('a', href=re.compile('^(/|.*'+includeUrl+')')):
        #Nếu link không phải link trống
        if link.attrs['href'] is not None:
            #Nếu link không phải link đã được tìm qua
            if link.attrs['href'] not in internalLinks:
                # nếu link bắt đầu bằng '/', bắt đầu của một link nội bộ
                if(link.attrs['href'].startswith('/')):
                    # Thêm vào với link đầy đủ
                    internalLinks.append(includeUrl+link.attrs['href'])
        # Nesu là link trống vẫn lấy link thêm vào link nội bộ
        else:
            internalLinks.append(link.attrs['href'])
            return internalLinks
    
# Truy xuất danh sách tất cả các liên kết bên ngoài được tìm thấy trên một trang
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    # Tìm tất cả các liên kết bắt đầu bằng "http"
    # không chứa URL hiện tại
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
                return externalLinks
def getRandomExternalLink(startingPage):
    #Chạy link Homepage được truyền vào
    html = urlopen(startingPage)
    bs = BeautifulSoup(html, 'html.parser')
    # Truyền vào Func Elements và .netloc (ở đây netloc là 'oreilly.com' )
    #Phương thức urlparse là phân tích link
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    #Trả về một link đầy đủ và không trùng với link đã duyệt qua

    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')
        #Nếu không tìm thấy link liên kết ngoài bên ngoài Homepage, tiếp tục tìm kiếm các link nội bộ bên trong trang
        domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
        # phương thúc urlparse 
        # .scheme lấy http hoặc www
        # .net lấy phần network location
        internalLinks = getInternalLinks(bs, domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]
#Thuc hien dau tien 
def followExternalOnly(startingSite):
    #chạy func getRandomExternalLink()
    externalLink = getRandomExternalLink(startingSite)
    #chạy xong in RandomExternalLink được trả về
    print('Random external link is: {}'.format(externalLink))
    #Tiếp tục chạy link được trả về
    followExternalOnly(externalLink)
#Nhập homepage
followExternalOnly('http://oreilly.com')