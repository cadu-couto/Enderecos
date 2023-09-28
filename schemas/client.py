from pydantic import BaseModel


class ClientIdSchema(BaseModel):
    client_id: str = "eb753b7c-69aa-4f75-977e-28bd42c63261"

class documentNumberSchema(BaseModel):
    document_number: str = "55544433310"