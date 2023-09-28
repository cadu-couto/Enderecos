from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from model.base import Base
from model.client import Client, get_client_list, get_client
from model.address import Address



# conexão com o banco
engine = create_engine('postgresql+psycopg2://cadu:@localhost/parking', echo=True)


# seção com o banco
Session = sessionmaker(bind=engine)


# criação do banco, em caso não exista
if not database_exists(engine.url):
    create_database(engine.url)


# criação das tabelas do banco
Base.metadata.create_all(engine)