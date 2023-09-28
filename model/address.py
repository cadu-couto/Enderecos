from sqlalchemy import Column, Integer, String, ForeignKey
from model.base import Base



class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    address_id = Column(String(36), unique=True )
    type = Column(String(20))
    cep = Column(String(8))
    street = Column(String(50))
    number =  Column(String(10))
    complement = Column(String(50))
    neighborhood = Column(String(50))
    city = Column(String(100))
    state = Column(String(2))
    client_id = Column(String(36))

    def __repr__(self):
        return f'{self.street}, {self.number}, {self.complement}, {self.neighborhood}, {self.city}-{self.state}, cep {self.cep[:5]}-{self.cep[-3:]}'