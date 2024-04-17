def introduction_page():
    message = """
        Sistema cadastral

        *Cadastrar Pessoa - 1
        *Buscar Pessoa por Nome -2 
        *Sair - 5
    """
    
    print(message)
    command = input("Comando: ")
    
    return command