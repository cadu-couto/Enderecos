from flask_openapi3 import OpenAPI, Info, Tag
from sqlalchemy.exc import IntegrityError
from model import Client, Address, Session, get_client_list
import logging
from schemas import *
from flask_cors import CORS
import json
import uuid
from google_maps import get_distance_from_googlemaps




info = Info(title="MVP - Endereços", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

search_client_tag = Tag(name="Busca por Cliente", description="Busca por cliente pelo Número do Documento (CPF)")
address_tag = Tag(name="Endereço", description="Gestão de Endereço")


class Res:
    status: bool
    msg: str

    def __init__(self, status, msg):
        self.status = status
        self.msg = msg


class AddressDistance:

    def __init__(self, address, distance_km, distance):
        self.address = address
        self.distance_km = distance_km
        self.distance = distance


#listar todos os clientes cadastrados
@app.get('/clients', summary="List todos os clientes", tags=[search_client_tag])
def get_clients():
    session = Session()
    clients = session.query(Client).all()
    if not clients:
        return {"clients": []}, 200
    else:
        print(f"Qauntidade de clientes encontrados: {len(clients)}")
        print(clients)
        return get_client_list(clients), 200


#listar todos os clientes cadastrados
@app.post('/client/search', summary="Busca Cliente pelo número do documento", tags=[search_client_tag])
def search_client(form: documentNumberSchema):
    res = {"sucess": True,
           "msg": "ok",
           "client": ""}
    print(f"Busca Cliente")
    session = Session()
    client = session.query(Client).filter(Client.document_number == form.document_number).first()
    if client is None:
        res["sucess"] = False
        res["msg"] = "Número do documento não encontrado."
        return res, 404
    res['client'] = {"name": client.name,
                     "document_number": client.document_number,
                     "document_type": client.document_type,
                     "client_id": client.client_id}
    return res, 200


# listar todos os clientes cadastrados
@app.post('/address',
          summary="Inclui um novo endereço",
          tags=[address_tag])
def create_address(form: AddressSchema):
    res = { "sucess": True,
            "msg": "ok",
            "address": ""}
    address = Address(  address_id = uuid.uuid4(),
                        type = form.type,
                        cep = form.cep,
                        street = form.street,
                        number =  form.number,
                        complement = form.complement,
                        neighborhood = form.neighborhood,
                        state = form.state,
                        city = form.city,
                        client_id = form.client_id)
    try:
        session = Session()
        session.add(address)
        session.commit()
        logging.info(f"Novo encedereço criado: '{address}'")
        res["address"] = str(address)
        return res , 200
    except IntegrityError as e:
        error_msg = "Erro na criação do endereço"
        logging.info(f"Erro: {error_msg}")
        return {"message": error_msg}, 409
    except Exception as e:
        error_msg = f"Erro na criação do endereço. {e}"
        logging.info(f"Erro: {error_msg}")
        return {"message": error_msg}, 400


# listar todos os clientes cadastrados
@app.put('/address',
          summary="Alteração de um endereço",
          tags=[address_tag])
def update_address(form: AddressSchema):
    res = { "sucess": True,
            "msg": "ok",
            "address": ""}
    session = Session()
    address = session.query(Address).filter(Address.address_id == form.address_id).first()
    if address is None:
        res["sucess"] = False
        res["msg"] = "Endereço não localizado"
        return res, 404
    address.type = form.type
    address.cep = form.cep
    address.street = form.street
    address.number = form.number
    address.complement = form.complement
    address.neighborhood = form.neighborhood
    address.state = form.state
    address.city = form.city
    address.client_id = form.client_id
    session.commit()
    res["address"] = str(address)
    return res, 200


# listar todos os clientes cadastrados
@app.post('/address/shortest_distance_to_suport',
          summary="Lista as lojas de suporte com a distância do endereço do cliente.",
          tags=[address_tag])
def get_shortest_distance_to_suport(form: ClientIdSchema):
    res = Res(status=True, msg="ok");
    session = Session()
    address = session.query(Address).filter(Address.client_id == form.client_id).first()
    if address is None:
        res.status = False
        res.msg = "Cliente selecionado não possui  endereço cadastrado."
        return json.dumps(res.__dict__), 200
    address_destiny_list = session.query(Address).filter(Address.type == 'suport')
    adrress_distance_list = shortest_distance_to_suport(address_origen=address, address_destiny_list=address_destiny_list)
    return adrress_distance_list, 200


@app.post('/client/address',
          summary="Lista Endereço de um cliente",
          tags=[address_tag])
def get_address_by_client_id(form: ClientIdSchema):
    res = {"sucess": True,
           "msg": "ok",
           "address": ""}
    session = Session()
    address = session.query(Address).filter(Address.client_id == form.client_id).first()
    if address is None:
        res['sucess'] = False
        res['msg'] = "Cliente selecionado não possui endereço cadastrado."
        return res, 404

    res['address'] = {  "address_id": address.address_id,
                        "type": address.type,
                        "cep": address.cep,
                        "street": address.street,
                        "number": address.number,
                        "complement": address.complement,
                        "neighborhood": address.neighborhood,
                        "state": address.state,
                        "city": address.city }
    return res, 200



def shortest_distance_to_suport(address_origen, address_destiny_list):
    adrress_distance_list = []
    for address_destiny in address_destiny_list:
        distance = get_distance_from_googlemaps(str(address_origen), str(address_destiny))
        adrress_distance = {    "address": str(address_destiny),
                                "distance_km": distance['distance']['text'],
                                 "distance": distance['distance']['value']}
        adrress_distance_list.append(adrress_distance)
    return adrress_distance_list



# listar todos os clientes cadastrados
@app.delete('/address',
          summary="Apaga um determinado Endereço",
          tags=[address_tag])
def del_address(form: AddressIdSchema):
    res = { "sucess": True,
            "msg": "ok" }
    session = Session()
    count = session.query(Address).filter(Address.address_id == form.address_id).delete()
    session.commit()
    if count == 0:
        res["sucess"] = False
        res["msg"] = "Endereço não localizado"
        return res, 200
    return res, 200













