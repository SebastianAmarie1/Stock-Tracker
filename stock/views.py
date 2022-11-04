from django.shortcuts import render

from django.http import JsonResponse, HttpRequest
import json
from . import models

# Create your views here.
def stock(request):
    return render(request, "stock_page.html", {})

def stocks_api(request: HttpRequest) -> HttpRequest:
    #when this view is called it checks the method to see if it is GET or POST
    if request.method == "GET":
        #If GER then it will send a JSON response with all the infromation from the model
        return JsonResponse({
            'stocks': [
                stock.to_dict()
                for stock in models.Stock.objects.all()
            ]
        })
    if request.method == "POST":
        #Otherwise if the method is POST you get the information send from the body and 
        #create a model with the relevant information. Finally return the model.
        body = json.loads(request.body)
        print(body)
        stock = models.Stock.objects.create(
            item_name= body['name'],
            in_stock =body['in_stock'],
            price = body['price'],
            quantity = body['quantity'],
            email_of_user = body['email'],
        )
    
        return JsonResponse({
            'stocks': [
                stock.to_dict()
                for stock in models.Stock.objects.all()
            ]
        }) 

def stocks_api_indv(request: HttpRequest, stock_id: int) -> HttpRequest:
    #this will check for a HTTP request with a id in teh URL
    if request.method == "DELETE":
        #If its delete, we get the ID and grab the model and delete it. Finally we return the model back.
        deleting = models.Stock.objects.get(id=stock_id)
        deleting.delete()
        return JsonResponse({
                'stocks': [
                    stock.to_dict()
                    for stock in models.Stock.objects.all()
                ]
            }) 

    if request.method == "PUT":
        #if PUT then insert the data in the body into the model with the coresponding ID.
        #Finally return the model through JSON
        updating = json.loads(request.body)
        models.Stock.objects.filter(id=stock_id).update(
            item_name=updating['name'],
            in_stock = updating['in_stock'],
            price = updating['price'],
            quantity = updating['quantity'],
            email_of_user = updating['email'],)
        return JsonResponse({
                'stocks': [
                    stock.to_dict()
                    for stock in models.Stock.objects.all()
                ]
            }) 
    print("NOT WORKING")