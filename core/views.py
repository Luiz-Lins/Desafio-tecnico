import json
from http import HTTPStatus

from django.http import HttpResponse, JsonResponse

from core.models import Pessoa


def pessoa(request):
    pessoa = Pessoa.objects.all()
    return HttpResponse('Hello Django')


def create_pessoa(request):
    payload = json.loads(request.body)
    pessoa = Pessoa.objects.create(**payload)
    data = {
        'nome': pessoa.nome,
        'email': pessoa.email,
        'dt_nascimento': pessoa.data_nascimento,
    }
    return JsonResponse(data, status=HTTPStatus.CREATED)


def read_pessoa(request):
    pass


def udpdate_pessoa(request):
    pass


def delete_pessoa(request, Pessoa):
    Pessoa.delete()
    return HttpResponse(status=HTTPStatus.NO_CONTENT)