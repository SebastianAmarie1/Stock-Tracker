
from django.urls import path

from . import views

app_name = "stock"

urlpatterns = [
    #add paths to different URLs and then links them to the view
    path('', views.stock, name='stock'),
    path('api/stocks/', views.stocks_api),
    path('api/stocks/<int:stock_id>/', views.stocks_api_indv, name="recepie api indv")
]