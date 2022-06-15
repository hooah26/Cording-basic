
from . import views
from django.urls import include, path


app_name = 'fin'


urlpatterns = [
    path('chart/', views.chart, name= 'chart' ),
    path('plot/', views.plot, name= 'plot' ),
]
