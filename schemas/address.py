from pydantic import BaseModel


class AddressSchema(BaseModel):
    address_id: str = "2e3b946d-e27b-46dc-b9b5-11ef5497b655"
    type: str = "suport"
    cep: str = "22000-000"
    street: str = "Avenida Exemplo"
    number: str = "1000"
    complement: str = "APT 1000"
    neighborhood: str = "Bairro"
    city: str = "Rio de Janeiro"
    state: str = "RJ"
    client_id: str = "eb753b7c-69aa-4f75-977e-28bd42c63261"


class AddressIdSchema(BaseModel):
    address_id: str = "eb753b7c-69aa-4f75-977e-28bd42c63261"