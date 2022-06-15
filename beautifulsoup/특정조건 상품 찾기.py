import requests
from bs4 import BeautifulSoup
import re

count=1
for page in range(1,6):
    url='https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor='.format(page)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')   #받아온 res의 text를 lxml으로 파싱해서 저장한 객체가 soup.

    items = soup.find_all("li",{"class":re.compile("^search-product")})

    for item in items:  #items는 여러개의 li 리스트. 포문 돌려서 하나의 li (하나의 item)씩 처리.
        name = item.find("div",{"class":"name"}).get_text()
        price = item.find("strong",{"class":"price-value"}).get_text()
        pro_url = item.find("a")['href']
        
        # 평점이 없는 경우 발생
        rating = item.find("em",{"class":"rating"})   #일단 찾아봤더니 그게 넌타입일 수 있다. 넌타입 존재 자체로 에러가 나진 않는다.
        if rating:
            # rating의 text부분만 추출
            rate = rating.get_text()
        else:
            continue      #그런데 넌타입을 가지고 뭔가를 적용하려고 하면 에러가 나니까, 넌타입일 경우는 스킵하라고 컨티뉴 쓰는 것.
                        #else에서 continue를 만나면  아래로 진행못하고 위로 올라가서 다음 item (포문의 다음 번째) 진행.
         

        # 상품평
        totalcount = item.find("span",{"class":"rating-total-count"})
        if totalcount:
            tcnt = totalcount.get_text()
            tcnt = tcnt[1:-1]  # (20) -> 20    : 맨처음번꺼 빼고 그 다음부터, 맨 마지막꺼(-1) 전까지.
            
            if int(tcnt)>=1000 and float(rate) >=5.0:
                print("[ {} ]".format(count))
                print("상품명 : ",name)
                print("상품가격 : ",price)  
                print("평점 : ",rating.get_text())
                print("상품평 : ",tcnt)
                print("https://www.coupang.com"+pro_url)
                print("-"*10)
                count += 1
            else:
                continue    
        else:
            continue   #상품평 없으면 넘어가고 다음 아이템 해라.