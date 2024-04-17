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