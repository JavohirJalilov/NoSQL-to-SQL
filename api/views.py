from django.http import HttpRequest, JsonResponse
from .models import Smartphones
import json

def smartphones(request: HttpRequest) -> JsonResponse:
    smartphones = Smartphones.objects.all()

    result = []
    for i in smartphones:
        result.append({
            "id": i.pk,
            "name": i.name,
            "price": i.price,
            "memory": i.memory,
            "ram": i.ram,
            "color": i.color,
        })

    return JsonResponse({'result': result})


def add_smartphone(request: HttpRequest) -> JsonResponse:
    if request.method=='POST':
        data = request.body.decode()
        data_json = json.loads(data)

        smartphone = Smartphones(
            price=data_json['price'],
            memory=data_json['memory'],
            ram=data_json['ram'],
            color=data_json['color'],
            img_url=data_json['img_url'],
            name=data_json['name'],
            model=data_json['model'],
        )
        smartphone.save()

        return JsonResponse({"result": "OK"})
    return JsonResponse({"result": "failed, only POST request"})


def get_smartphone(request: HttpRequest,id) -> JsonResponse:
    smartphones = Smartphones.objects.all()
    
    for i in smartphones:
        if i.id==id:
            result={
            "id": i.id,
            "name": i.name,
            "price": i.price,
            }

    return JsonResponse({"result": result})



def del_smartphone(request: HttpRequest,id) -> JsonResponse:
    smartphones = Smartphones.objects.all()

    for i in smartphones:
        if i.id==id:
            i.delete()
            return JsonResponse({"result": "OK"})
    
    return JsonResponse({"result": "not found"})



def upd_smartphone(request: HttpRequest,id) -> JsonResponse:
    if request.method == 'POST':
        data = request.body.decode()
        data_json = json.loads(data)

        smartphones = Smartphones.objects.all()

        for i in smartphones:
            if i.id==id:
                i.price=data_json.get('price', i.price)
                i.memory=data_json.get('memory', i.memory)
                i.ram=data_json.get('ram', i.ram)
                i.color=data_json.get('color', i.color)
                i.img_url=data_json.get('img_url', i.img_url)
                i.name=data_json.get('name', i.name)
                i.model=data_json.get('model', i.model)

                i.save()

                return JsonResponse({"result": "OK"})

        return JsonResponse({"result": "not found"})
