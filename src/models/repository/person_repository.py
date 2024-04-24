
from src.models.entities.person import Person

class __PersonRepository:
    def __init__(self) -> None:
        self.__people = []
    
    # É uma ação para armazenar dentro do Banco de Dados; xlsx ou qualquer outro lugar
    def registry_person(self, person: Person) -> None:
        self.__people.append(person)
        
    # Repository para fazer uma acao ou armazenamento dentro do banco     
    def find_person_by_name (self, name: str) -> Person:
        for person in self.__people:
            if person.name == name:
                return person
        return None
    
person_repository = __PersonRepository()