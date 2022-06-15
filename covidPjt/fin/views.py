from django.shortcuts import render
import requests
import json
import xmltodict
from fin.models import Covid


# Create your views here.


def chart(request):
    covidData()
    return render(request, 'chart.html')

def plot(request):
    return render(request, 'plot.html')


def covidData():
    # m_servicekey= 'kPvWkLn8zX%2FrcSryaV88GKZw89YENVfrgvH06AuvYSrXsHOx6r705chjRSn%2F%2BjrdwYpeOPms5YcVRuYID5eWkA%3D%3D'
    # url='http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey={}&pageNo=1&numOfRows=10&startCreateDt=20200120&endCreateDt=20220119'.format(m_servicekey)
    # response =requests.get(url)

    #수찬꺼
    url='http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=JvU2PSq9lh1mHsrlM5p7uq9GeNuR4KrBvrHcZO0jIb7unq5lANtM0HkaDA35GqYh3vhuWTXxlWrXqE8AZiqVSA%3D%3D&pageNo=1&numOfRows=1000&startCreateDt=20200120&endCreateDt=20220119'
    
    
    response= requests.get(url)
    contents=response.text    #xml형식의 텍스트를
    dictionary = xmltodict.parse(contents)   # dic형식으로 만들고
    json_str= json.dumps(dictionary)   #이렇게 했는데 str타입이 나와?
    json_ob= json.loads(json_str)   #이렇게 해야 json dict 객체로 만들어서
    covidData= json_ob['response']['body']['items']['item'] #해당 키 내의 벨류값 찾아옴
    # print(json_ob)
    # print(covidData)
    # print(type(json_ob))

    # print(json_ob)
    # print(covidData)


    for i in covidData:
        date= i['stateDt']
        deathCnt= i['deathCnt']
        decideCnt= i['decideCnt']
        qs = Covid(date=date,intdate=int(date), deathCnt=int(deathCnt), decideCnt=int(decideCnt))
        qs.save()