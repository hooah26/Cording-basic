from django.shortcuts import redirect, render
from board.models import Fboard
from django.db.models import Q, F
from django.core.paginator import Paginator
from member.models import Member
from django.db.models import Max, Min, Avg
import urllib  #한글 인코딩
import requests #웹스크롤링
import json


def publicData(request):
    nowpage= request.GET.get('nowpage',1)
    m_serviceKey='kPvWkLn8zX%2FrcSryaV88GKZw89YENVfrgvH06AuvYSrXsHOx6r705chjRSn%2F%2BjrdwYpeOPms5YcVRuYID5eWkA%3D%3D'
    # url = 'http://api.visitkorea.or.kr/openapi/service/rest/PhotoGalleryService/galleryList'
    url = 'http://api.visitkorea.or.kr/openapi/service/rest/PhotoGalleryService/galleryList?serviceKey={}&pageNo={}&numOfRows=10&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'.format(m_serviceKey, nowpage)
    # params ={'serviceKey' : m_serviceKey, 'pageNo' : '1', 'numOfRows' : '10', 'MobileOS' : 'ETC', 'MobileApp' : 'AppTest', 'arrange' : 'A' }
    response = requests.get(url)
    contents=response.text  #json형식의 텍스트를
    json_ob= json.loads(contents)   #json형식의 객체로
    publicData= json_ob['response']['body']['items']['item']
    print(publicData)
    context={'publicData':publicData}
    return render(request, 'publicData.html', context)


def publicData2(request):
    nowpage= request.GET.get('nowpage',1)
    m_serviceKey='kPvWkLn8zX%2FrcSryaV88GKZw89YENVfrgvH06AuvYSrXsHOx6r705chjRSn%2F%2BjrdwYpeOPms5YcVRuYID5eWkA%3D%3D'
    url='https://api.odcloud.kr/api/apnmOrg/v1/list?page={}&perPage=10&serviceKey={}'.format(nowpage,m_serviceKey)
    response=requests.get(url)
    contents=response.text
    json_ob=json.loads(contents)
    publicData2=json_ob['data']
    context={'publicData2':publicData2}
    return render(request, 'publicData2.html', context)




# 게시판리스트
def blist(request):
    nowpage = int(request.GET.get('nowpage',1))  # 현재페이지 받음, 없을때 1 고정
    
    if request.method == 'GET':
        
        
        
        qs = Fboard.objects.all().order_by('-b_group', 'b_step')
        # 모든게시글을 받아서 페이지 분기
        paginator = Paginator(qs,10)  # 30개 1-10,2-10,3-10 / 10개씩 들어가있음.
        blist = paginator.get_page(nowpage)
        context={'blist':blist, 'nowpage':nowpage}
        return render(request,'blist.html',context) 
    else:
        category = request.POST.get('category')
        searchword = request.POST.get('searchword')
        # title검색
        if category == 'title':
            qs = Fboard.objects.filter(b_title__contains=searchword)
            # 모든게시글을 받아서 페이지 분기
            paginator = Paginator(qs,10)           # 30개 1-10,2-10,3-10
            blist = paginator.get_page(nowpage)
            context={'blist':blist,'category':category,'searchword':searchword, 'nowpage':nowpage}
            return render(request,'blist.html',context)
            
        elif category == 'content':    
            qs = Fboard.objects.filter(b_content__contains=searchword)
            # 모든게시글을 받아서 페이지 분기
            paginator = Paginator(qs,10)           # 30개 1-10,2-10,3-10
            blist = paginator.get_page(nowpage)
            context={'blist':blist,'category':category,'searchword':searchword, 'nowpage':nowpage}
            return render(request,'blist.html',context)
        
        elif category == 'all':
            # a and b
            # qs = Fboard.objects.filter(b_title__contains=searchword,b_content__contains=searchword)
            # a or b
            qs = Fboard.objects.filter(Q(b_title__contains=searchword) | Q(b_content__contains=searchword))
            # 모든게시글을 받아서 페이지 분기
            paginator = Paginator(qs,10)           # 30개 1-10,2-10,3-10
            blist = paginator.get_page(nowpage)       # paginator
            context={'blist':blist,'category':category,'searchword':searchword, 'nowpage':nowpage}
            return render(request,'blist.html',context)
        

    



# 뷰페이지
def bview(request,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    qs.b_hit += 1
    qs.save()
    context={'board':qs}
    return render(request,'bview.html',context)

# 수정페이지
def bmodify(request,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    context={'board':qs}
    return render(request,'bmodify.html',context)

# 수정페이지저장
def bmodifyOk(request):
    b_no = request.POST.get('b_no')
    b_title = request.POST.get('b_title')
    b_content = request.POST.get('b_content')
    # 파일 가져오기
    b_img = request.FILES.get('b_img','')
    # img 파일이 없는 경우에는 ''(빈칸)으로 연결한다.
    print("files :" , request.FILES)
    qs = Fboard.objects.get(b_no=b_no)
    qs.b_title = b_title
    qs.b_content = b_content
    qs.b_img = b_img
    qs.save()
    # Fboard.objects.create(b_id=id,b_title=title,b_content=content)
    # context = {"board":qs}
    return render(request,'bview.html',{"board":qs})
    # return redirect('board:bview')

# 게시판글쓰기
def bwrite(request):
    return render(request,'bwrite.html')

# 게시판글쓰기저장
def bwriteOk(request):
    id = request.POST.get('id')
    member = Member.objects.get(m_id = id)
    title = request.POST.get('title')
    content = request.POST.get('content')
    img = request.FILES.get('img','')
    # img 파일이 없는 경우에는 ''(빈칸)으로 연결한다.
    print("files :" , request.FILES)
    
     #  aggregate = Max, Min, Avg 
    no = Fboard.objects.aggregate(i= Max('b_no'))
    print(no)   # no 는 {'i': 28}
    max_no = no['i'] 
    max_no+= 1
    b_no = max_no
    
    qs = Fboard(b_no=b_no,member=member,b_title=title, b_content=content, b_group= b_no, b_img=img)
    qs.save() 
    # Fboard.objects.create(b_id=id,b_title=title,b_content=content)
    return redirect('board:blist')

# 게시글 삭제
def bdelete(request,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    qs.delete()
    return redirect('board:blist')



def breply(request,b_no):
    qs = Fboard.objects.get(b_no=b_no)
    context = {"board":qs}


    return render(request, 'breply.html', context)



def breplyOk(request):
    #  aggregate = Max, Min, Avg 
    no = Fboard.objects.aggregate(max_b_no= Max('b_no'))
    max_no = no['max_b_no'] 
    max_no+= 1
    b_no = max_no
    
    #부모의 정보
    
    b_group = int(request.POST.get('b_group'))
    b_step = int(request.POST.get('b_step'))
    b_indent = int(request.POST.get('b_indent'))
    
    
    id = request.POST.get('id')
    member = Member.objects.get(m_id = id)
    title = request.POST.get('title')
    content = request.POST.get('content')
    img = request.FILES.get('img','')
    # img 파일이 없는 경우에는 ''(빈칸)으로 연결한다.
    
    
    Fboard.objects.filter(b_group=b_group, b_step__gt=b_step).update(b_step=F('b_step')+1)
    
    
    qs = Fboard(b_no=b_no,member=member,b_title=title, b_content=content, b_group= b_group, b_step=b_step+1, b_indent= b_indent+1, b_img=img)
    qs.save() 
    # Fboard.objects.create(b_id=id,b_title=title,b_content=content)
    return redirect('board:blist')


