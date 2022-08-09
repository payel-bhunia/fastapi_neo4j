from pickle import STRING
from typing import Union
from neo4j import GraphDatabase
import os

from fastapi import FastAPI


class PersonDetails:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    @staticmethod
    def _return_data(tx):
        result = tx.run("MATCH (p:Person) return {name:p.name,age:p.age} as res")
        return result.values()

    @staticmethod
    def _create_data(tx, name, age):
        result = tx.run("CREATE (p:Person{name:$name,age:$age})", name=name, age=age)
        return result.values()


app = FastAPI()
uri = os.getenv('NEO4J_URI')
user = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
obj = PersonDetails(uri, user, password)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/data")
def read_item():
    with obj.driver.session() as session:
        result = session.write_transaction(obj._return_data)
        return result


@app.get("/name/{name}")
def read_item(age: int, name: Union[str, None]):
    with obj.driver.session() as session:
        session.write_transaction(obj._create_data, name, age)
        return "created"
