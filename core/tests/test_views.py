from multiprocessing.connection import Client
from core.views import delete_pessoa


def test_create_pessoa(client: Client, created_pessoa=None):
    data = {
        "nome": 'Luiz Lins',
        "email": 'luizlins22@gmail.com',
        "dt_nascimento": '29/11/1990',
    }
    response = client.post('/api/pessoa/', data=data, content_type='application/json')

    assert response.status_code == 200
    assert created_pessoa == created_pessoa

def test_delete_pessoa(client: Client):
    data = {
        "nome": 'Luiz Lins',
        "email": 'luizlins22@gmail.com',
        "dt_nascimento": '29/11/1990',
    }
    response = client.delete('/api/pessoa/', data=data)

    assert response.status_code == 200
    assert delete_pessoa == delete_pessoa