from ast import Raise
from typing import Dict
from src.models.entities.person import Person
from src.models.repository.person_repository import person_repository

class PeopleFinderController:
    def find_by_name(self, person_finder_information: Dict) -> Dict:
        try:
            self.__validate_filds(person_finder_information)
            person = self.__find_person(person_finder_information)
            response = self.__format_response(person)
            return {"success": True, "message": response}
        
        except Exception as e:
            return {"success": False, "error": str(e)}
        
    def __validate_filds(self, person_finder_information: Dict) -> None:
        if not isinstance(person_finder_information["name"], str):
            raise Exception ('Campo Name invalido!')
        
    def __find_person(self, person_finder_information: Dict) -> Person:
        name = person_finder_information["name"]
        
        person = person_repository.find_person_by_name(name)
        
        if not person:
            raise Exception ('Pessoa nao encontrada!')
        
        return person
        
    def __format_response(self, person: Person)->Dict:
        return{
            "count": 1,
            "type": "Person",
            "infos": {
                "name": person.name,
                "age": person.age,
                "height": person.height
            }
        }