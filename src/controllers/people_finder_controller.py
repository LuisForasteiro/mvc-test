from typing import Dict


class PeopleFinderController:
    def find_by_name(self, person_finder_information: Dict) -> Dict:
        try:
            self.__validate_filds(person_finder_information)
            # buscar em banco de dados
            response = self.__format_response(None)
            return {"success": True, "message": response}
            
        except Exception as e:
            return {"success": False, "error": str(e)}
        
    def __validate_filds(self, person_finder_information: Dict) -> None:
        if not isinstance(person_finder_information["name"], str):
            raise Exception ('Campo Name invalido!')
        
    def __format_response(self, person: any)->Dict:
        return{
            "count": 1,
            "type": "Person",
            "infos": {
                "name": "Meu nome teste"
            }
        }