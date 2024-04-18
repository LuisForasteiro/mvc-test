from typing import Dict

class PeopleRegisterController:
    def register(self, new_person_informations: Dict) -> Dict:
        try:
            self.__validate_fields(new_person_informations)
            # enviar para o models para o cadastro de dados
            response = self.__format_response(new_person_informations)
            return {"success": True, "message": response}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def __validate_fields(self, new_person_informations: Dict) -> None:
        if not isinstance(new_person_informations["name"], str):
            raise Exception ('Campo Nome incorreto')

        try:
            int(new_person_informations["age"])
        except: 
            raise Exception('Campo idade incorreto')
        
        try:
            int(new_person_informations['height'])
        except: raise Exception('Campo altura incorreto')
        
        
    def __format_response(self, new_person_informations : Dict) -> Dict:
        return {"count": 1, 
                "type": "Person",
                "attributes": new_person_informations
                }
        