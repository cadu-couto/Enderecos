from sqlalchemy import Column, String, Integer
from model.base import Base
from typing import List


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    client_id = Column(String(36), unique=True)
    name = Column(String(50))
    document_number = Column(String(13))
    document_type = Column(String(50))

    def __repr__(self):
        return f'{self.name}'


def get_client_list(clients: List[Client]):
    result = []
    for client in clients:
        result.append({
            "client_id": client.client_id,
            "name": client.name,
            "document_number": client.document_number,
            "document_type": client.document_type,
            "daddress_id": client.address_id,
        })
    return {"clients": result}


def get_client(client: Client):
        return  {"client_id": client.client_id,
                "name": client.name,
                "document_number": client.document_number,
                "document_type": client.document_type,
                "daddress_id": client.address_id}

