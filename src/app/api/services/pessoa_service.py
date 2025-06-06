def getPessoaName(id_pessoa, pessoas_domicilio):
    for pessoa in pessoas_domicilio:
        if pessoa["id_pessoa"] == id_pessoa:
            return pessoa["nome_pessoa"]
    return "Pessoa desconhecida"
