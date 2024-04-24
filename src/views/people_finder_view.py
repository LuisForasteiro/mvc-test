from typing import Dict
import os

class PeopleFinderView:
    def find_person_view(self) -> Dict:
        os.system('cls||clear')
        
        print('Buscar Pessoa\n\n')
        name = input('Informe o nome da pessoa: ')
        
        person_finder_information = {
            "name": name
        }
        
        return person_finder_information
    
    def find_person_success(self, message: Dict) -> None:
        os.system('cls||clear')
        
        success_message = f"""
        
        Usuario enconrado com sucesso!
        
        Tipo: {message['type']}
        Registros: {message['count']}
        Infos: 
            Name: {message['infos']['name']}
            Age: {message['infos']['age']}
            Height: {message['infos']['height']}
        """
        print(success_message)
        
    def find_person_fail(self, error: str) -> None:
        os.system('cls||clear')
        
        fail_message = f"""
        Falaha ao encontrar usuario!
        ERROR: {error}
        
        """
        print(fail_message)