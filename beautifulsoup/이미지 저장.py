import requests
from bs4 import BeautifulSoup   #이미지 소스도 html에서 구문분석으로 가져오는 거니까 beautifulsoup이 필요하다.

for page in range(2017,2022):
    url="https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(page)
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    # img url이 있는 링크 검색
    imgs = soup.find_all("img",{"class":"thumb_img"})

    # 역대 순위 5개를 가져옴.
    for idx,img in enumerate(imgs):
        img_url = img['src']  #img의 src속성의 값 (=url)을 가져온다.
        img_res = requests.get(img_url)  #img_res의 타입은 requests의 객체.
        img_res.raise_for_status()  #img url 주소를 requests로 가져온 객체의 content는 단순 url 스트링이 아니라, 이미지 파일이다. 
                                    
        
        # 파일 저장
        with open("movie_{}년도_{}위.jpg".format(page,idx+1),"wb") as f:
            f.write(img_res.content)    #url은 이미지가 있는 곳이고, 이미지 파일은 다르다. requests의 객체의 content로 가져와야한다.
        
        # 이미지 5개가 다운로드 되면 종료
        if(idx==4):
            break